# Standard library imports.
import asyncio
import warnings

# Third party imports.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListView

# Local application imports.
from Comms.Serial.config import USING_COBS
if USING_COBS:
    from Comms.Parsers.cobs_parser import COBSParser
else:
    from Comms.Parsers.dle_parser import DLEParser
from Comms.Serial.port_handler import PortHandler
from Enums.enum_msg import MessageID
from UI.ui_custom_widgets import NoFocus
from UI.ui_signal_slot import SignalSlot
from UI.ui_styling import Colours
from Utilities.messages import buildMessage
from Utilities.metrics_handler import processMetrics


class UIComms:
    """
    Class for handling all aspects of communication, whether that be UI interaction or the data itself being received or transmitted.
    Manages the setup and control of serial comms and Bluetooth comms.
    Integrates with the Qt event loop and signal-slot system to ensure thread-safe updates to the GUI.
    """

    def __init__(self, main_window, event_loop):
        """
        Initialises the UIComms class.

        Args:
            main_window:    Reference to the main window, used for accessing UI elements.
            event_loop:     Reference to the main thread's asyncio event loop. Required to safely schedule function calls from this background thread back to the main async thread, for example, to add a received message to an asyncio.Queue.
        """
        self.main_window = main_window

        # Initialise all attributes.
        self.event_loop = event_loop
        self.message_queue = asyncio.Queue()  # Queue for messages to be processed.

        # Create signal-slot connections.
        self.signal_slot = SignalSlot()
        self.signal_slot.primary_console_signal.connect(self.main_window.ui_console.logPrimaryConsole) # Done here as the intent is to be used for all comms logging.
        self.signal_slot.secondary_console_signal.connect(self.main_window.ui_console.logSecondaryConsole) # Done here as the intent is to be used for all comms logging.

        # Comms tab setup and handler when the tab is changed.
        self.main_window.ui.commsTab.currentChanged.connect(self.commsTabChanged)
        self.commsTabChanged(self.main_window.ui.commsTab.currentIndex())


    def commsTabChanged(self, index):
        """
        Called whenever the current tab in the commsTab widget changes.
        Sets up or tears down communication handlers based on the selected tab.

        Args:
            index: The index of the newly selected tab.
        """
        # Reset shared byte counters when switching tabs.
        self.rx_bytes = 0
        self.tx_bytes = 0

        if index == 0: # Serial tab selected. This is the default tab.
            if hasattr(self, "bluetooth_handler"):
                try:
                    if self.bluetooth_handler.connected():
                        self.bluetooth_handler.close()
                    self.bluetooth_handler.stop()  # Stop the thread.
                except Exception as e:
                    print(f"E1: {__file__}: {e}")
                del self.bluetooth_handler  # Remove reference.

            self.serialComms = True
            self.bluetoothComms = False

            self.last_serial_ports = [] # Cache of last discovered ports for manual mode.

            # Disconnect previous signal connections to avoid duplicates.
            if hasattr(self, "serialConnectClicked"):
                self.disconnectSignal(self.main_window.ui.serialConnectButton.clicked, self.serialConnectClicked)
            if hasattr(self, "radioButtonHandler"):
                self.disconnectSignal(self.main_window.ui.serialAutoButton.toggled, self.radioButtonHandler)
                self.disconnectSignal(self.main_window.ui.serialManualButton.toggled, self.radioButtonHandler)
            if hasattr(self, "updateComPortBox"):
                self.disconnectSignal(self.signal_slot.com_port_signal, self.updateComPortBox)
            if hasattr(self, "incrementSerialBytes"):
                self.disconnectSignal(self.signal_slot.serial_bytes_signal, self.incrementSerialBytes)
            if hasattr(self, "updateStatus"):
                self.disconnectSignal(self.signal_slot.status_signal, self.updateStatus)

            # Create the serial port handler and start the background thread.
            self.serial_port_handler = PortHandler(self,  # Pass self so PortHandler can access ui_comms for signal-slot and UI updates.
                                                self.event_loop)
            self.serial_port_handler.start()

            # Connect UI elements to their handlers.
            self.main_window.ui.serialConnectButton.clicked.connect(self.serialConnectClicked)
            self.main_window.ui.serialAutoButton.toggled.connect(self.radioButtonHandler)
            self.main_window.ui.serialManualButton.toggled.connect(self.radioButtonHandler)

            self.signal_slot.com_port_signal.connect(self.updateComPortBox)
            self.signal_slot.serial_bytes_signal.connect(self.incrementSerialBytes)
            self.signal_slot.status_signal.connect(self.updateStatus)

            # Trigger additional functions to set up the UI for use.
            self.radioButtonHandler()
            self.populateBaudRateBox()
            self.setSerialStyleSheetUIComms()
        elif index == 1:
            if hasattr(self, "serial_port_handler"):
                try:
                    if self.serial_port_handler.connected():
                        self.serial_port_handler.close()
                    self.serial_port_handler.stop()  # Stop the thread.
                except Exception as e:
                    print(f"E2: {__file__}: {e}")
                del self.serial_port_handler  # Remove reference.

            self.serialComms = False
            self.bluetoothComms = True


    def disconnectSignal(self, signal, slot):
        """
        Disconnects a signal from a slot, ignoring errors and warnings if the signal was not connected in the first place.
        """
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            try:
                signal.disconnect(slot)
            except (TypeError, RuntimeError):
                pass  # Signal was not connected, ignore.


    ########### Message Handling Methods ##########


    def handleMessage(self, message):
        """
        Called whenever there is a new message to handle.
        This method receives the message and dispatches it to the relevant UI class that requires the data.

        Args:
            message: The latest message from the queue to handle.
        """
        msg_id = message[0]
        if msg_id not in MessageID._value2member_map_:
            return

        msg_id = MessageID(msg_id)
        msgBytes = bytes(message) # Message is a list, convert to bytes for unpacking later on.

        authPending = self.main_window.ui_authentication.authRequired() and not self.main_window.ui_authentication.isAuthenticated()
        if authPending:
            match msg_id:
                case MessageID.HANDSHAKE:
                    self.main_window.ui_authentication.processHandshake(msgBytes)
                case MessageID.AUTHENTICATE:
                    self.main_window.ui_authentication.processAuthentication(msgBytes)
                case _:
                    return
        else:
            match msg_id:
                case MessageID.HEARTBEAT:
                    self.main_window.ui_panel.heartbeatReceived()
                case MessageID.METRIC_EVENT:
                    processMetrics(self, msgBytes)
                case MessageID.METRIC_ADC_STATUS:
                    self.main_window.ui_adc.updateADCTable(msgBytes)
                case MessageID.METRIC_GPIO_INPUT_STATUS:
                    self.main_window.ui_gpio.updateInputTable(msgBytes)
                case MessageID.METRIC_GPIO_OUTPUT_STATUS:
                    self.main_window.ui_gpio.updateOutputTable(msgBytes)
                case _:
                    print(f"Unhandled message ID: 0x{msg_id.value:X}")


    def sendMessage(self, msg_id, format, payload, dest, mode, debug_message=False, debug_encoded=False):
        """
        Sends a message to the serial port.

        Args:
            msg_id:         The message ID to send.
            format:         The format of the payload to send.
            payload:        The payload to send.
            dest:           The destination of the message.
            mode:           The mode of the message.
            debug_message:  If True, the message contents will be printed for debugging purposes.
            debug_encoded:  If true, the encoded message contents will be printed for debugging purposes.

        Returns:
            True if the message was sent successfully, False otherwise.
        """
        # Do not allow sending of non authenticated messages if authentication is required.
        if self.main_window.ui_authentication.authRequired() and not self.main_window.ui_authentication.isAuthenticated() and msg_id not in (MessageID.HANDSHAKE, MessageID.AUTHENTICATE):
            return False
        else:
            if self.serialComms:
                if not self.serial_port_handler.connected() or not self.serial_port_handler.serial_handler.isCommunicating():
                    print(f"Failed to send message 0x{msg_id.value:02X}: Port closed or communication stopped.")
                    return False
                message = buildMessage(msg_id, format, payload, dest, mode)
                encoded_message = self.serial_port_handler.serial_handler.protocol_parser.encodeMessage(message)
                if debug_message:
                    if USING_COBS:
                        COBSParser.debugMessage(message, is_encoded=False)
                    else:
                        DLEParser.debugMessage(message, is_encoded=False)
                if debug_encoded:
                    if USING_COBS:
                        COBSParser.debugMessage(encoded_message)
                    else:
                        DLEParser.debugMessage(encoded_message)
                return self.serial_port_handler.serial_handler.writeMessage(encoded_message)


    ##########################################
    ########## Serial Comms Methods ##########
    ##########################################


    ########## Serial UI Configuring Methods ##########


    def populateBaudRateBox(self):
        """
        Populates the baud rate box with available baud rates.
        """
        baudRates = [9600, 19200, 38400, 57600, 115200]
        self.main_window.ui.serialBaudRateBox.clear()
        self.main_window.ui.serialBaudRateBox.addItems([str(rate) for rate in baudRates])

        # Centre the text for every item.
        for i in range(self.main_window.ui.serialBaudRateBox.count()):
            self.main_window.ui.serialBaudRateBox.setItemData(i, int(Qt.AlignCenter), Qt.TextAlignmentRole)

        # Set default selection to 115200.
        default_baud_index = self.main_window.ui.serialBaudRateBox.findText("115200")
        if default_baud_index != -1:
            self.main_window.ui.serialBaudRateBox.setCurrentIndex(default_baud_index)


    def setSerialStyleSheetUIComms(self):
        """
        Sets the style sheet for the serial UIComms items.
        Only applies additional styling here that cannot be set in QtCreator.
        """
        for box in (self.main_window.ui.serialComPortBox, self.main_window.ui.serialBaudRateBox):
            box.setMaxVisibleItems(10)

            # Create and set a dedicated view to set how the drop-down list looks.
            list_view = QListView(box)
            list_view.setAttribute(Qt.WA_StyledBackground, True) # Force the background to be painted from the style sheet.
            list_view.setStyleSheet(f"""
                                    QListView,
                                    QAbstractItemView{{
                                        color: {Colours.BLACK.name()};             /* Text colour */
                                        background: {Colours.WHITE.name()};        /* Background colour */
                                        border: 1px solid {Colours.BLACK.name()};  /* Border colour */
                                    }}
                                    QListView::item{{
                                        padding: 4px 8px;           /* Item padding */
                                        min-height: 15px;           /* Minimum item height */
                                    }}
                                    QListView::item:hover,
                                    QListView::item:selected{{
                                        color: {Colours.BLACK.name()};             /* Text colour */
                                        background: {Colours.PALE_GREEN.name()};   /* Background colour */
                                    }}
                                    """)
            list_view.setItemDelegate(NoFocus(list_view)) # Prevent focus rectangle around items in the drop down boxes.
            box.setView(list_view)


    ########## Serial Connection Methods ##########


    def radioButtonHandler(self):
        """
        Determines what radio button has been selected and acts accordingly.
        If auto mode is selected, enables auto-connect and disables the manual connect button.
        If manual mode is selected, enables manual connect, enables the connect button, and refreshes the list of available ports.
        """
        if self.main_window.ui.serialAutoButton.isChecked():
            self.serial_port_handler.setAutoConnect()
            # Serial connect button is disabled when auto serial is selected, also update button style sheet.
            self.main_window.ui.serialConnectButton.setEnabled(False)
            self.main_window.ui.serialConnectButton.setStyleSheet(f"""
                                                                color: {Colours.BLACK.name()};                  /* Text colour */
                                                                border: 2px solid {Colours.BLACK.name()};       /* Thick black solid border */
                                                                border-radius: 5px;                             /* Rounded corners */
                                                                background-color: {Colours.LIGHT_PINK.name()};  /* Background colour */
                                                                """)
            self.main_window.ui.serialConnectButton.setText("Select Manual")
        else:
            if self.main_window.ui.serialManualButton.isChecked():
                self.serial_port_handler.setManualConnect()
                if not self.serial_port_handler.connected():
                    # Enable serial connect button, set style sheet to handle the connect option. If already connected, this is handled in updateStatus.
                    self.main_window.ui.serialConnectButton.setEnabled(True)
                    self.main_window.ui.serialConnectButton.setStyleSheet(f"""
                                                                        color: {Colours.BLACK.name()};                  /* Text colour */
                                                                        border: 2px solid {Colours.BLACK.name()};       /* Thick black solid border */
                                                                        border-radius: 5px;                             /* Rounded corners */
                                                                        background-color: {Colours.PALE_GREEN.name()};  /* Background colour */
                                                                        """)
                    self.main_window.ui.serialConnectButton.setText("Connect")
                    self.serial_port_handler.refreshPorts()  # Force refresh of available ports when switching to manual mode, not doing this will sometimes cause a stale list of ports.


    def serialConnectClicked(self):
        """
        Acts on the serial button being clicked for manual mode only.
        If manual mode is selected and not currently connected, attempts to open the selected COM port.
        If already connected, closes the connection.
        """
        if self.main_window.ui.serialManualButton.isChecked():
            # We should only connect to the port if we are not already connected.
            if not self.serial_port_handler.connected():
                self.serial_port_handler.open(self.main_window.ui.serialComPortBox.currentText())
            else:
                self.serial_port_handler.close()


    ########## Serial Thread Methods ##########


    def updateComPortBox(self, ports):
        """
        Called every 500 ms by PortHandler.
        Updates the COM port box with either the connected port if in auto mode, or a list of available ports to connect to if in manual mode.

        Args:
            ports: A list where the first element contains all discovered ports, and the second element is the connected port (if connected, else None).
        """
        if self.main_window.ui.serialManualButton.isChecked():
            # Only update if not connected.
            if not self.serial_port_handler.connected():
                current_port = self.main_window.ui.serialComPortBox.currentText()
                discovered_ports = sorted(ports[0]) # Sort all discovered ports alphabetically.

                # Only update if the list of discovered ports has changed or the box is empty.
                if discovered_ports != self.last_serial_ports or self.main_window.ui.serialComPortBox.count() == 0:
                    self.main_window.ui.serialComPortBox.clear()
                    self.main_window.ui.serialComPortBox.addItems(discovered_ports)

                    # Centre text on new items.
                    for i in range(self.main_window.ui.serialComPortBox.count()):
                        self.main_window.ui.serialComPortBox.setItemData(i, int(Qt.AlignCenter), Qt.TextAlignmentRole)

                    self.last_serial_ports = discovered_ports.copy()

                    """
                    Finds the index of the current port string in the combo box.
                    If the port is present, selects it; otherwise, selects the first available port if any items exist.
                    If both fail, the box remains empty.
                    """
                    index = self.main_window.ui.serialComPortBox.findText(current_port)
                    if index != -1:
                        self.main_window.ui.serialComPortBox.setCurrentIndex(index)
                    elif self.main_window.ui.serialComPortBox.count() > 0:
                        self.main_window.ui.serialComPortBox.setCurrentIndex(0)
        else:
            if self.main_window.ui.serialAutoButton.isChecked():
                # Gather all strings displayed in the COM port box.
                discovered_ports = [self.main_window.ui.serialComPortBox.itemText(i) for i in range(self.main_window.ui.serialComPortBox.count())]
                # Only update if the connected port has changed (very unlikely to change) unless changing from None.
                if ports[1] and (len(discovered_ports) != 1 or discovered_ports[0] != ports[1]):
                    self.main_window.ui.serialComPortBox.clear()
                    self.main_window.ui.serialComPortBox.addItem(ports[1])
                    self.main_window.ui.serialComPortBox.setItemData(0, int(Qt.AlignCenter), Qt.TextAlignmentRole)
                else:
                    # Clear the box if the port has been disconnected.
                    if not ports[1] and len(discovered_ports) > 0:
                        self.main_window.ui.serialComPortBox.clear()


    ########## Serial Connection Status Methods ##########


    def updateStatus(self, connected):
        """
        Called whenever a port has been connected or disconnected. Acts on a status change from the PortHandler.

        Args:
            connected: True if the port is connected, False otherwise.
        """
        self.last_serial_ports = [] # Reset port cache on status change.
        if connected:
            # As soon as we connect, restart the heartbeat timers.
            self.main_window.ui_panel.heartbeatReceived() # Update timer to prevent immediate timeout.
            self.main_window.ui_panel.startHeartbeatTimer()
            self.main_window.ui_panel.startLEDHeartbeatTimer()
            self.main_window.ui.serialStatus.setText("Connected")
            self.main_window.ui.serialStatus.setStyleSheet(f"""
                                                            color: {Colours.BLACK.name()};                  /* Text colour */
                                                            background-color: {Colours.PALE_GREEN.name()};  /* Background colour */
                                                            border: 1px solid {Colours.BLACK.name()};       /* Thin black solid border */
                                                            border-radius: 5px;                             /* Rounded corners */
                                                            padding: 5px;                                   /* Adds space around the text */
                                                            padding-top: 3px;                               /* Adjusts the padding at the top */
                                                            padding-bottom: 3px;                            /* Adjusts the padding at the bottom */
                                                            line-height: 20px;                              /* Ensures proper vertical alignment of text */
                                                            """)
            if self.main_window.ui.serialManualButton.isChecked():
                self.main_window.ui.serialConnectButton.setText("Disconnect")
                self.main_window.ui.serialConnectButton.setStyleSheet(f"""
                                                                    color: {Colours.BLACK.name()};                  /* Text colour */
                                                                    border: 2px solid {Colours.BLACK.name()};       /* Thick black solid border */
                                                                    border-radius: 5px;                             /* Rounded corners */
                                                                    background-color: {Colours.LIGHT_PINK.name()};  /* Background colour */
                                                                    """)
            if self.main_window.ui_authentication.authRequired():
                self.main_window.ui_authentication.sendHandshake()
        else:
            self.main_window.ui_panel.stopHeartbeatTimer()
            self.main_window.ui_panel.stopLEDHeartbeatTimer()
            self.main_window.ui.serialStatus.setText("Not Connected")
            self.main_window.ui.serialStatus.setStyleSheet(f"""
                                                            color: {Colours.BLACK.name()};                  /* Text colour */
                                                            background-color: {Colours.LIGHT_PINK.name()};  /* Background colour */
                                                            border: 1px solid {Colours.BLACK.name()};       /* Thin black solid border */
                                                            border-radius: 5px;                             /* Rounded corners */
                                                            padding: 5px;                                   /* Adds space around the text */
                                                            padding-top: 3px;                               /* Adjusts the padding at the top */
                                                            padding-bottom: 3px;                            /* Adjusts the padding at the bottom */
                                                            line-height: 20px;                              /* Ensures proper vertical alignment of text */
                                                            """)
            if self.main_window.ui.serialManualButton.isChecked():
                self.main_window.ui.serialConnectButton.setText("Connect")
                self.main_window.ui.serialConnectButton.setStyleSheet(f"""
                                                                    color: {Colours.BLACK.name()};                  /* Text colour */
                                                                    border: 2px solid {Colours.BLACK.name()};       /* Thick black solid border */
                                                                    border-radius: 5px;                             /* Rounded corners */
                                                                    background-color: {Colours.PALE_GREEN.name()};  /* Background colour */
                                                                    """)
            self.rx_bytes = 0
            self.main_window.ui.serialRxBytes.setText(f"{self.rx_bytes}")
            self.tx_bytes = 0
            self.main_window.ui.serialTxBytes.setText(f"{self.tx_bytes}")
            self.main_window.ui_authentication.setAuthentication(False)


    ########## Serial Bytes Methods ##########


    def incrementSerialBytes(self, num_bytes, incoming):
        """
        Called whenever serial bytes are either transmitted or received.
        Increments the amount of bytes and displays it on the GUI.

        Args:
            num_bytes: The number of bytes to increment by.
            incoming:  True if RX bytes, False if TX bytes.
        """
        if incoming:
            self.rx_bytes += num_bytes
            value = self.rx_bytes
            object = self.main_window.ui.serialRxBytes
        else:
            self.tx_bytes += num_bytes
            value = self.tx_bytes
            object = self.main_window.ui.serialTxBytes

        units = ["B", "KB", "MB", "GB", "TB"]
        unit_index = 0

        while value >= 1024 and unit_index < len(units) - 1:
            value /= 1024
            unit_index += 1

        # Byte values are shown as integers for bytes, and to two decimal places for larger units.
        object.setText(f"{value:.2f} {units[unit_index]}" if units[unit_index] != "B" else f"{value} {units[unit_index]}")
