import asyncio

from datetime import datetime
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from messages import buildMessage, unpackMessage
from metrics_handler import processMetrics
from PySide6 import QtCore
from Serial.port_handler import PortHandler
from Serial.protocol_parser import ProtocolParser
from time import time
from UI.ui_signal_slot import SignalSlot
from UI.ui_styling import CSS


class UIComms:
    """
    Class for handling all aspects of serial communication, whether that be UI interaction or the data itself being received or transmitted.
    Manages the setup and control of serial port connections, message handling, authentication, heartbeat monitoring, and byte counters.
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

        # Set up the style sheet first as it has no dependencies.
        self.setStyleSheetUIComms()

        # Initialise all attributes.
        self.event_loop = event_loop
        self.message_queue = asyncio.Queue()  # Queue for messages to be processed.
        self.rx_bytes = 0
        self.tx_bytes = 0
        self.last_ports = []

        # Heartbeat setup.
        self.heartbeat_poll_time_ms = 4000
        self.heartbeat_timeout_s    = 8
        self.led_heartbeat_time_ms  = 500
        self.heartbeat_receive_time = 0
        self.heartbeat              = False
        self.send_heartbeat_timer   = QtCore.QTimer()
        self.led_heartbeat_timer    = QtCore.QTimer()

        # Create signal-slot connections and threaded objects.
        self.signal_slot = SignalSlot()
        self.signal_slot.com_port_signal.connect(self.updateComPortBox)
        self.signal_slot.primary_console_signal.connect(self.main_window.ui_console.logPrimaryConsole)
        self.signal_slot.rx_bytes_signal.connect(self.incrementRXBytes)
        self.signal_slot.secondary_console_signal.connect(self.main_window.ui_console.logSecondaryConsole)
        self.signal_slot.status_signal.connect(self.updateStatus)
        self.signal_slot.tx_bytes_signal.connect(self.incrementTXBytes)

        # Create the serial port handler and start the background thread.
        self.serial_port_handler = PortHandler(self,  # Pass self so PortHandler can access ui_comms for signal-slot and UI updates.
                                               self.event_loop)
        self.serial_port_handler.start()

        # Connect UI elements to their handlers.
        self.main_window.ui.serialConnectButton.clicked.connect(self.serialConnectClicked)
        self.main_window.ui.autoSerialButton.toggled.connect(self.radioButtonHandler)
        self.main_window.ui.manualSerialButton.toggled.connect(self.radioButtonHandler)
        self.main_window.ui.authenticateButton.toggled.connect(self.handleAuthenticateButton)

        self.send_heartbeat_timer.timeout.connect(self.sendHeartbeat)
        self.led_heartbeat_timer.timeout.connect(self.toggleHeartbeatLED)

        # Set the desired initial authentication state.
        self.auth_required = False
        self.authenticated = False

        # Update the authentication button state but do not call the handler.
        self.main_window.ui.authenticateButton.blockSignals(True)
        self.main_window.ui.authenticateButton.setChecked(self.auth_required)
        self.main_window.ui.authenticateButton.blockSignals(False)

        self.updateAuthenticationStatus(self.authenticated)

        # Trigger additional functions to set up the UI.
        self.radioButtonHandler()
        self.populateBaudRateBox()


    def setStyleSheetUIComms(self):
        """
        Sets the style sheet for the UIComms items.
        Only applies additional styling here that cannot be set in QtCreator.
        """
        for box in [self.main_window.ui.comPortBox, self.main_window.ui.baudRateBox]:
            box.setMaxVisibleItems(10)
            box.setStyleSheet("""
                                QComboBox {
                                    color: #000000;                     /* Text colour */
                                    background-color: #FFFFFF;          /* Background colour */
                                    border: 1px solid black;            /* Thin black solid border */
                                    border-radius: 5px;                 /* Optional: rounded corners */
                                    padding-left: 16px;                 /* Pads left to look centred */
                                    line-height: 20px;                  /* Ensures proper vertical alignment of text */
                                    outline: none;                      /* Remove focus outline */
                                }
                                QComboBox QAbstractItemView {
                                    color: #000000;                     /* Text colour for drop-down items */
                                    background-color: #FFFFFF;          /* Background colour for drop-down items */
                                    border: 1px solid black;            /* Thin black solid border */
                                    border-radius: 5px;                 /* Rounded corners for drop-down items */
                                    outline: none;                      /* Remove focus outline */
                                }
                                QComboBox QAbstractItemView::item {
                                    padding-left: 5px;                  /* Ensures consistent left padding for all items, prevents text shifting when selected */
                                    border-radius: 5px;                 /* Rounded corners for drop-down items */
                                }
                                QComboBox QAbstractItemView::item:hover {
                                    color: #000000;                     /* Text colour for drop-down items */
                                    background-color: #FFAB7B;          /* Background colour when hovered */
                                    outline: none;                      /* Remove focus outline */
                                }
                                QComboBox QAbstractItemView::item:selected {
                                    background: #FFAB7B;                /* Background colour for the selected item when the popup is open and item is active (hovered or focused) */
                                    color: #000000;                     /* Text colour for the selected item */
                                    padding-left: 5px;                  /* Maintains same left padding for selected item, avoids selection shift */
                                }
                                QComboBox QAbstractItemView::item:selected:!active {
                                    background: #FFFFFF;                /* Background colour for the selected item when the popup is open but item is not active (not hovered) */
                                    color: #000000;                     /* Text colour for the selected item when not active */
                                }
                                QComboBox QAbstractItemView QScrollBar:vertical {
                                    width: 0px;                         /* Hides the vertical scroll bar */
                                }
                                QComboBox::drop-down {
                                    width: 0px;                         /* Hides the drop-down button area */
                                    border: none;                       /* Removes border from drop-down button */
                                    background: none;                   /* Removes background from drop-down button */
                                    padding: 0;                         /* Removes padding from drop-down button */
                                    margin: 0;                          /* Removes margin from drop-down button */
                                }
                                QComboBox::down-arrow {
                                    width: 0px;                         /* Hides the down arrow by setting width to zero */
                                    height: 0px;                        /* Hides the down arrow by setting height to zero */
                                    image: none;                        /* Removes the down arrow image */
                                }
                                """)


    def populateBaudRateBox(self):
        """
        Populates the baud rate box with available baud rates.
        """
        baudRates = [9600, 19200, 38400, 57600, 115200]
        self.main_window.ui.baudRateBox.clear()
        self.main_window.ui.baudRateBox.addItems([str(rate) for rate in baudRates])
        # Set default selection to 115200.
        default_baud_index = self.main_window.ui.baudRateBox.findText("115200")
        if default_baud_index != -1:
            self.main_window.ui.baudRateBox.setCurrentIndex(default_baud_index)


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

        authPending = self.main_window.ui_demo is None and self.auth_required and not self.authenticated
        if authPending:
            match msg_id:
                case MessageID.HANDSHAKE:
                    self.processHandshake(msgBytes)
                case MessageID.AUTHENTICATE:
                    self.processAuthentication(msgBytes)
                case _:
                    return
        else:
            match msg_id:
                case MessageID.HEARTBEAT:
                    self.heartbeatReceived()
                case MessageID.METRICS_EVENT:
                    processMetrics(self, msgBytes)
                case MessageID.ADC_STATUS:
                    self.main_window.ui_adc.updateADCTable(msgBytes)
                case MessageID.GPIO_INPUTS_STATUS:
                    self.main_window.ui_gpio.updateInputTable(msgBytes)
                case MessageID.GPIO_OUTPUTS_STATUS:
                    self.main_window.ui_gpio.updateOutputTable(msgBytes)
                case _:
                    print(f"Unhandled message ID: 0x{msg_id.value:X}")


    def sendMessage(self, msg_id, format, payload, dest, mode, decode=False):
        """
        Sends a message to the serial port.

        Args:
            msg_id:   The message ID to send.
            format:   The format of the payload to send.
            payload:  The payload to send.
            dest:     The destination of the message.
            mode:     The mode of the message.
            decode:   If True, the message will be decoded and returned, otherwise it will be sent to the serial port.

        Returns:
            True if the message was sent successfully, False otherwise.
        """
        # Do not allow sending of non authenticated messages if authentication is required.
        if self.auth_required and not self.authenticated and msg_id not in [MessageID.HANDSHAKE, MessageID.AUTHENTICATE]:
            return False
        else:
            if not self.serial_port_handler.connected() or not self.serial_port_handler.serial_handler.isCommunicating():
                print(f"Failed to send message 0x{msg_id.value:02X}: Port closed or communication stopped.")
                return False
            message = buildMessage(msg_id, format, payload, dest, mode)
            encoded_message = ProtocolParser.encodeMessage(message)
            if decode:
                ProtocolParser.decodeMessage(encoded_message)
            return self.serial_port_handler.serial_handler.writeMessage(encoded_message)


    ########## Auto/Serial Connection Methods ##########


    def inDemoMode(self):
        """
        Returns whether demo mode is currently active. Implemented here so that PortHandler can check this status before attempting to open a port.
        This instance (UIComms) is passed to port handler on initialisation. There is no way to pass a reference of the demo UI class to PortHandler directly as it is created after PortHandler.

        Returns:
            True if active, False otherwise.
        """
        if self.main_window.ui_demo is not None:
            if self.main_window.ui_demo.isActive():
                self.main_window.ui_console.logDebugConsole(f"Cannot open port because demo mode is active.")
                return True
        return False


    def radioButtonHandler(self):
        """
        Determines what radio button has been selected and acts accordingly.
        If auto mode is selected, enables auto-connect and disables the manual connect button.
        If manual mode is selected, enables manual connect, enables the connect button, and refreshes the list of available ports.
        """
        if self.main_window.ui.autoSerialButton.isChecked():
            # Do not allow switching to auto mode if demo mode is active.
            if not self.inDemoMode():
                self.serial_port_handler.setAutoConnect()
                # Serial connect button is disabled when auto serial is selected, also update button style sheet.
                self.main_window.ui.serialConnectButton.setEnabled(False)
                self.main_window.ui.serialConnectButton.setStyleSheet("""
                                                                    color: #000000;                     /* Text colour */
                                                                    border: 2px solid #000000;          /* Thick black solid border */
                                                                    border-radius: 5px;                 /* Rounded corners */
                                                                    background-color: #FFA2A7;          /* Background colour */
                                                                    """)
                self.main_window.ui.serialConnectButton.setText("Select Manual")
            else:
                # Deny this button request, temporarily block the signal to prevent recursion.
                self.main_window.ui.autoSerialButton.blockSignals(True)
                self.main_window.ui.autoSerialButton.setChecked(False)
                self.main_window.ui.autoSerialButton.blockSignals(False)
                self.main_window.ui.manualSerialButton.setChecked(True)
        else:
            if self.main_window.ui.manualSerialButton.isChecked():
                self.serial_port_handler.setManualConnect()
                if not self.serial_port_handler.connected():
                    # Enable serial connect button, set style sheet to handle the connect option. If already connected, this is handled in updateStatus.
                    self.main_window.ui.serialConnectButton.setEnabled(True)
                    self.main_window.ui.serialConnectButton.setStyleSheet("""
                                                                        color: #000000;                 /* Text colour */
                                                                        border: 2px solid #000000;      /* Thick black solid border */
                                                                        border-radius: 5px;             /* Rounded corners */
                                                                        background-color: #A6FFA7;      /* Background colour */
                                                                        """)
                    self.main_window.ui.serialConnectButton.setText("Connect")
                    self.serial_port_handler.refreshPorts()  # Force refresh of available ports when switching to manual mode, not doing this will sometimes cause a stale list of ports.


    def serialConnectClicked(self):
        """
        Acts on the serial button being clicked for manual mode only.
        If manual mode is selected and not currently connected, attempts to open the selected COM port.
        If already connected, closes the connection.
        """
        if self.main_window.ui.manualSerialButton.isChecked():
            # We should only connect to the port if we are not already connected and we are not in demo mode.
            if not self.serial_port_handler.connected() and not self.inDemoMode():
                self.serial_port_handler.open(self.main_window.ui.comPortBox.currentText())
            else:
                self.serial_port_handler.close()


    ########### Thread Management ##########


    def updateComPortBox(self, ports):
        """
        Called every 500 ms by PortHandler.
        Updates the COM port box with either the connected port if in auto mode, or a list of available ports to connect to if in manual mode.

        Args:
            ports: A list where the first element contains all discovered ports, and the second element is the connected port (if connected, else None).
        """
        if self.main_window.ui.manualSerialButton.isChecked():
            # Only update if not connected.
            if not self.serial_port_handler.connected():
                current_port = self.main_window.ui.comPortBox.currentText()
                discovered_ports = sorted(ports[0]) # Sort all discovered ports alphabetically.

                # Only update if the list of discovered ports has changed.
                if discovered_ports != self.last_ports:
                    self.main_window.ui.comPortBox.clear()
                    self.main_window.ui.comPortBox.addItems(discovered_ports)
                    self.last_ports = discovered_ports.copy()

                    """
                    Finds the index of the current port string in the combo box.
                    If the port is present, selects it; otherwise, selects the first available port if any items exist.
                    If both fail, the box remains empty.
                    """
                    index = self.main_window.ui.comPortBox.findText(current_port)
                    if index != -1:
                        self.main_window.ui.comPortBox.setCurrentIndex(index)
                    elif self.main_window.ui.comPortBox.count() > 0:
                        self.main_window.ui.comPortBox.setCurrentIndex(0)
        else:
            if self.main_window.ui.autoSerialButton.isChecked():
                # Gather all strings displayed in the COM port box.
                discovered_ports = [self.main_window.ui.comPortBox.itemText(i) for i in range(self.main_window.ui.comPortBox.count())]

                # Only update if the connected port has changed (very unlikely to change) unless changing from None.
                if ports[1] and (len(discovered_ports) != 1 or discovered_ports[0] != ports[1]):
                    self.main_window.ui.comPortBox.clear()
                    self.main_window.ui.comPortBox.addItem(ports[1])
                else:
                    # Clear the box if the port has been disconnected.
                    if not ports[1] and len(discovered_ports) > 0:
                        self.main_window.ui.comPortBox.clear()


    ############ Port Connection Methods ##########


    def updateStatus(self, connected):
        """
        Called whenever a port has been connected or disconnected. Acts on a status change from the PortHandler.

        Args:
            connected: True if the port is connected, False otherwise.
        """
        self.last_ports = [] # Reset port cache on status change.
        if connected:
            # As soon as we connect, restart the heartbeat timers.
            self.heartbeat_receive_time = time() # Reset timer to prevent immediate timeout.
            self.send_heartbeat_timer.start(self.heartbeat_poll_time_ms)
            self.led_heartbeat_timer.start(self.led_heartbeat_time_ms)
            self.main_window.ui.statusLineEdit.setText("Connected")
            self.main_window.ui.statusLineEdit.setStyleSheet("""
                                                            color: #000000;                   /* Text colour */
                                                            background-color: #A6FFA7;        /* Background colour */
                                                            border: 1px solid black;          /* Thin black solid border */
                                                            border-radius: 5px;               /* Rounded corners */
                                                            padding: 5px;                     /* Adds space around the text */
                                                            padding-top: 3px;                 /* Adjusts the padding at the top */
                                                            padding-bottom: 3px;              /* Adjusts the padding at the bottom */
                                                            line-height: 20px;                /* Ensures proper vertical alignment of text */
                                                            """)
            if self.main_window.ui.manualSerialButton.isChecked():
                self.main_window.ui.serialConnectButton.setText("Disconnect")
                self.main_window.ui.serialConnectButton.setStyleSheet("""
                                                                    color: #000000;                 /* Text colour */
                                                                    border: 2px solid #000000;      /* Thick black solid border */
                                                                    border-radius: 5px;             /* Rounded corners */
                                                                    background-color: #FFA2A7;      /* Background colour */
                                                                    """)
            if self.auth_required:
                self.sendHandshake()
        else:
            self.send_heartbeat_timer.stop()
            self.led_heartbeat_timer.stop()
            self.main_window.ui.statusLineEdit.setText("Not Connected")
            self.main_window.ui.statusLineEdit.setStyleSheet("""
                                                            color: #000000;                   /* Text colour */
                                                            background-color: #FFA2A7;        /* Background colour */
                                                            border: 1px solid black;          /* Thin black solid border */
                                                            border-radius: 5px;               /* Rounded corners */
                                                            padding: 5px;                     /* Adds space around the text */
                                                            padding-top: 3px;                 /* Adjusts the padding at the top */
                                                            padding-bottom: 3px;              /* Adjusts the padding at the bottom */
                                                            line-height: 20px;                /* Ensures proper vertical alignment of text */
                                                            """)
            if self.main_window.ui.manualSerialButton.isChecked():
                self.main_window.ui.serialConnectButton.setText("Connect")
                self.main_window.ui.serialConnectButton.setStyleSheet("""
                                                                    color: #000000;                 /* Text colour */
                                                                    border: 2px solid #000000;      /* Thick black solid border */
                                                                    border-radius: 5px;             /* Rounded corners */
                                                                    background-color: #A6FFA7;      /* Background colour */
                                                                    """)
            self.rx_bytes = 0
            self.main_window.ui.rxByteLineEdit.setText(f"{self.rx_bytes}")
            self.tx_bytes = 0
            self.main_window.ui.txByteLineEdit.setText(f"{self.tx_bytes}")
            self.authenticated = False
            self.updateAuthenticationStatus(self.authenticated)


    ############ Authentication Methods ##########


    def calcAuth(self, auth_val):
        """
        Calculates the authentication key.

        Args:
            auth_val: The authorisation value.

        Returns:
            The calculated authentication key as an integer.
        """
        auth_val_calc = (auth_val ^ 0x5355505244415645) % 0x200052C8 # PC
        return auth_val_calc


    def handleAuthenticateButton(self):
        """
        Enables or disables the need for authentication based on the button click.
        """
        self.auth_required = self.main_window.ui.authenticateButton.isChecked()

        if self.auth_required and self.serial_port_handler.connected():
            self.sendHandshake()

        self.updateAuthenticationStatus(self.authenticated)


    def processAuthentication(self, msg):
        """
        Called when an authentication message is received.

        Args:
            msg: The authentication message.
        """
        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: red;{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Received authentication{CSS.END_STYLE}")

        status_msg = ""

        match MsgMode(msg[5]): # Note, mode is the 5th element as it's not unpacked yet.
            case MsgMode.NACK:
                status_msg = "Authentication NACK received"
            case MsgMode.REQ_ACK:
                status_msg = "Authentication REQ_ACK received"
            case MsgMode.SET_ACK:
                status_msg = "Authentication SET_ACK received"
                self.authenticated = True
                self.updateAuthenticationStatus(self.authenticated)
            case _:
                status_msg = "Authentication Unknown"

        if status_msg:
            self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: red;{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - {status_msg}{CSS.END_STYLE}")

        # If we are authenticated, a heartbeat is immediately sent to the processor.
        if self.authenticated:
            self.heartbeat_receive_time = time() # Needs to be reset again once authenticated. If not, the original time at initialisation is taken and a timeout occurs.
            self.sendHeartbeat()
            self.led_heartbeat_timer.start(self.led_heartbeat_time_ms)


    def processHandshake(self, msg):
        """
        Called when a handshake message is received.

        Args:
            msg: The handshake message.
        """
        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: red;{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Received handshake{CSS.END_STYLE}")

        match MsgMode(msg[5]): # Note, mode is the 5th element as it's not unpacked yet.
            case MsgMode.NACK:
                status_msg = "Handshake NACK received"
            case MsgMode.REQ_ACK:
                status_msg = "Handshake REQ_ACK received"
            case MsgMode.SET_ACK:
                status_msg = "Handshake SET_ACK received"
            case _:
                _, payload = unpackMessage("Q", msg)
                auth_val = payload[0]
                self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: red;{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Auth Value: {auth_val}{CSS.END_STYLE}")
                auth_calc = self.calcAuth(auth_val)
                self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: red;{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Auth Calc: {auth_calc}{CSS.END_STYLE}")
                if self.sendMessage(MessageID.AUTHENTICATE, "Q", [auth_calc], SrcDest.SRC_DEST_ECU1, MsgMode.SET):
                    status_msg = "Sending authentication"

        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: red;{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - {status_msg}{CSS.END_STYLE}")


    def sendHandshake(self):
        """
        Sends a handshake in an attempt to authenticate with the device.
        """
        if self.sendMessage(MessageID.HANDSHAKE, "BBB", [SrcDest.SRC_DEST_PC.value, 1, 0], SrcDest.SRC_DEST_ECU1, MsgMode.SET):
            status_msg = "Sending handshake"
        else:
            status_msg = "Unable to send handshake"

        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: red;{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - {status_msg}{CSS.END_STYLE}")


    def updateAuthenticationStatus(self, authenticated):
        """
        Updates the authentication status text box.

        Args:
            authenticated: True if authenticated, False otherwise.
        """
        if not self.auth_required:
            self.main_window.ui.authenticateLineEdit.setStyleSheet("""
                                                                    color: #000000;             /* Text colour */
                                                                    background-color: #FFE200;  /* Background colour */
                                                                    border: 1px solid black;    /* Thin black solid border */
                                                                    border-radius: 5px;         /* Optional: rounded corners */
                                                                    padding: 5px;               /* Adds space around the text */
                                                                    padding-top: 3px;           /* Adjusts the padding at the top */
                                                                    padding-bottom: 3px;        /* Adjusts the padding at the bottom */
                                                                    line-height: 20px;          /* Ensures proper vertical alignment of text */
                                                                """)
            self.main_window.ui.authenticateLineEdit.setText("Not Required")
        else:
            if authenticated:
                self.main_window.ui.authenticateLineEdit.setStyleSheet("""
                                                                        color: #000000;             /* Text colour */
                                                                        background-color: #A6FFA7;  /* Background colour */
                                                                        border: 1px solid black;    /* Thin black solid border */
                                                                        border-radius: 5px;         /* Optional: rounded corners */
                                                                        padding: 5px;               /* Adds space around the text */
                                                                        padding-top: 3px;           /* Adjusts the padding at the top */
                                                                        padding-bottom: 3px;        /* Adjusts the padding at the bottom */
                                                                        line-height: 20px;          /* Ensures proper vertical alignment of text */
                                                                    """)
                self.main_window.ui.authenticateLineEdit.setText("Authenticated")
            else:
                self.main_window.ui.authenticateLineEdit.setStyleSheet("""
                                                                        color: #000000;             /* Text colour */
                                                                        background-color: #FFA2A7;  /* Background colour */
                                                                        border: 1px solid black;    /* Thin black solid border */
                                                                        border-radius: 5px;         /* Optional: rounded corners */
                                                                        padding: 5px;               /* Adds space around the text */
                                                                        padding-top: 3px;           /* Adjusts the padding at the top */
                                                                        padding-bottom: 3px;        /* Adjusts the padding at the bottom */
                                                                        line-height: 20px;          /* Ensures proper vertical alignment of text */
                                                                    """)
                self.main_window.ui.authenticateLineEdit.setText("Not Authenticated")


    ############ Byte Count Methods ##########


    def incrementRXBytes(self, num_bytes):
        """
        Called whenever new data is received over serial.
        Increments the amount of received bytes and displays it on the GUI.

        Args:
            num_bytes: The number of RX bytes to increment by.
        """
        self.rx_bytes += num_bytes

        units = ["B", "KB", "MB", "GB", "TB"]
        value = self.rx_bytes
        unit_index = 0

        while value >= 1024 and unit_index < len(units) - 1:
            value /= 1024
            unit_index += 1

        # Byte values are shown as integers for bytes, and to two decimal places for larger units.
        self.main_window.ui.rxByteLineEdit.setText(f"{value:.2f} {units[unit_index]}" if units[unit_index] != "B" else f"{value} {units[unit_index]}")


    def incrementTXBytes(self, num_bytes):
        """
        Called whenever new data is transmitted over serial.
        Increments the amount of transmitted bytes and displays it on the GUI.

        Args:
            num_bytes: The number of TX bytes to increment by.
        """
        self.tx_bytes += num_bytes

        units = ["B", "KB", "MB", "GB", "TB"]
        value = self.tx_bytes
        unit_index = 0

        while value >= 1024 and unit_index < len(units) - 1:
            value /= 1024
            unit_index += 1

        # Byte values are shown as integers for bytes, and to two decimal places for larger units.
        self.main_window.ui.txByteLineEdit.setText(f"{value:.2f} {units[unit_index]}" if units[unit_index] != "B" else f"{value} {units[unit_index]}")


    ########## Heartbeat Methods ##########


    def heartbeatReceived(self):
        """
        Updates the time when a heartbeat message is received.
        """
        self.heartbeat_receive_time = time()


    def sendHeartbeat(self):
        """
        Sends a heartbeat every 4 seconds.
        """
        self.sendMessage(MessageID.HEARTBEAT, "", [], SrcDest.SRC_DEST_ECU1, MsgMode.REQ)


    def toggleHeartbeatLED(self):
        """"
        Toggles the heartbeat LED in the GUI.
        """
        if self.serial_port_handler.serial_handler is None:
            is_healthy = False
        else:
            is_healthy = (self.serial_port_handler.serial_handler.isCommunicating() and
                        (time() - self.heartbeat_receive_time) < self.heartbeat_timeout_s)

        if is_healthy:
            self.heartbeat = not self.heartbeat # Still receiving, toggle the LED state.
        else:
            self.heartbeat = False # Force the LED to remain off if we have lost heartbeat comms.
            self.led_heartbeat_timer.stop()

        self.main_window.ui.heartbeatLED.setChecked(self.heartbeat)