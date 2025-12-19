# Standard library imports.
from time import time

# Third party imports.
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout

# Local application imports.
from Enums.enum_calls_demands import CallType, DiagnosticCall
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from UI.ui_colour_creator import UIColourCreator
from UI.ui_config import UIConfig
from UI.ui_custom_widgets import ScalableLabel
from UI.ui_key_wiring import UIKeyWiring
from UI.ui_rail_map import UIRailMap
from UI.ui_styling import Colours, Styles
from UI.ui_system import UISystem
from UI.ui_x06 import UIX06
from Utilities.utils import resource_path


class UIPanel:
    """
    Class for the UI panel. Handles navigation within the main application panel and additional feature such as heartbeat etc.
    """

    def __init__(self, main_window):
        """
        Initialises the UIPanel class.

        Args:
            main_window: Reference to the main window, used for accessing UI elements.
        """
        self.main_window = main_window

        # Fit and centre the Metrics logo within the image frame.
        self.image_label = ScalableLabel(self.main_window.ui.imageFrame)
        self.image_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(resource_path("Images/Metrics-Stannah-Logo.png"))
        self.image_label.setPixmap(pixmap)
        image_frame_layout = QVBoxLayout(self.main_window.ui.imageFrame)
        image_frame_layout.addWidget(self.image_label)

        # Connect buttons to their respective functions.
        self.main_window.ui.ADCIOPageButton.clicked.connect(lambda:          self.goToADCIO())
        self.main_window.ui.colourPalettePageButton.clicked.connect(lambda:  self.goToColourPalette())
        self.main_window.ui.configurationPageButton.clicked.connect(lambda:  self.goToConfiguration())
        self.main_window.ui.keyWiringPageButton.clicked.connect(lambda:      self.goToKeyWiring())
        self.main_window.ui.railMappingPageButton.clicked.connect(lambda:    self.goToRailMapping())
        self.main_window.ui.systemPageButton.clicked.connect(lambda:         self.goToSystem())
        self.main_window.ui.x06PageButton.clicked.connect(lambda:            self.goToX06())
        self.main_window.ui.chairFoldPageButton.clicked.connect(lambda:      self.goToChairFold())
        self.main_window.ui.footrestPageButton.clicked.connect(lambda:       self.goToFootrest())
        self.main_window.ui.mainDrivePageButton.clicked.connect(lambda:      self.goToMainDrive())
        self.main_window.ui.swivelPageButton.clicked.connect(lambda:         self.goToSwivel())

        self.main_window.ui.testButton1.clicked.connect(lambda:              self.buttonTest1())
        self.main_window.ui.testButton2.clicked.connect(lambda:              self.buttonTest2())
        self.main_window.ui.testButton3.clicked.connect(lambda:              self.buttonTest3())
        self.main_window.ui.testButton4.clicked.connect(lambda:              self.buttonTest4())
        self.main_window.ui.testButton5.clicked.connect(lambda:              self.buttonTest5())

        self.main_window.ui.carriageLeftCallButton.clicked.connect(lambda:   self.sendCall(MessageID.CALL_REQUEST, CallType.CARRIAGE_LEFT))
        self.main_window.ui.carriageRightCallButton.clicked.connect(lambda:  self.sendCall(MessageID.CALL_REQUEST, CallType.CARRIAGE_RIGHT))
        self.main_window.ui.carriageUpCallButton.clicked.connect(lambda:     self.sendCall(MessageID.CALL_REQUEST, CallType.CARRIAGE_UP))
        self.main_window.ui.carriageDownCallButton.clicked.connect(lambda:   self.sendCall(MessageID.CALL_REQUEST, CallType.CARRIAGE_DOWN))
        self.main_window.ui.chairFoldCallButton.clicked.connect(lambda:      self.sendCall(MessageID.CALL_REQUEST, CallType.CHAIR_FOLD))
        self.main_window.ui.chairPartFoldCallButton.clicked.connect(lambda:  self.sendCall(MessageID.CALL_REQUEST, CallType.CHAIR_PARTIAL_FOLD))
        self.main_window.ui.chairUnfoldCallButton.clicked.connect(lambda:    self.sendCall(MessageID.CALL_REQUEST, CallType.CHAIR_UNFOLD))
        self.main_window.ui.footrestFoldCallButton.clicked.connect(lambda:   self.sendCall(MessageID.CALL_REQUEST, CallType.FOOTREST_FOLD))
        self.main_window.ui.footrestUnfoldCallButton.clicked.connect(lambda: self.sendCall(MessageID.CALL_REQUEST, CallType.FOOTREST_UNFOLD))
        self.main_window.ui.swivelLeftCallButton.clicked.connect(lambda:     self.sendCall(MessageID.CALL_REQUEST, CallType.SWIVEL_OUT_LEFT))
        self.main_window.ui.swivelCentreCallButton.clicked.connect(lambda:   self.sendCall(MessageID.CALL_REQUEST, CallType.SWIVEL_IN))
        self.main_window.ui.swivelRightCallButton.clicked.connect(lambda:    self.sendCall(MessageID.CALL_REQUEST, CallType.SWIVEL_OUT_RIGHT))
        self.main_window.ui.noCallButton.clicked.connect(lambda:             self.sendCall(MessageID.CALL_REQUEST, CallType.NO_CALL_TYPE))

        self.main_window.ui.localLeftCallButton.clicked.connect(lambda:      self.sendCall(MessageID.SOFTWARE_CALL, DiagnosticCall.LOCAL_LEFT))
        self.main_window.ui.localRightCallButton.clicked.connect(lambda:     self.sendCall(MessageID.SOFTWARE_CALL, DiagnosticCall.LOCAL_RIGHT))
        self.main_window.ui.remoteUpCallButton.clicked.connect(lambda:       self.sendCall(MessageID.SOFTWARE_CALL, DiagnosticCall.REMOTE_UP))
        self.main_window.ui.remoteDownCallButton.clicked.connect(lambda:     self.sendCall(MessageID.SOFTWARE_CALL, DiagnosticCall.REMOTE_DOWN))

        self.main_window.ui.repeatCallButton.clicked.connect(lambda:         self.repeatCall())

        self.repeating_call = False
        self.call_to_repeat = None
        self.repeating_call_timer = QTimer()
        self.repeating_call_timer.timeout.connect(self.sendPeriodicCall)
        self.flash_call_button_timer = QTimer()
        self.flash_call_button_timer.timeout.connect(self.flashCallButton)

        self.main_window.ui.carriageLeftCallButton.setAutoRepeat(True)
        self.main_window.ui.carriageRightCallButton.setAutoRepeat(True)
        self.main_window.ui.carriageUpCallButton.setAutoRepeat(True)
        self.main_window.ui.carriageDownCallButton.setAutoRepeat(True)
        self.main_window.ui.chairFoldCallButton.setAutoRepeat(True)
        self.main_window.ui.chairPartFoldCallButton.setAutoRepeat(True)
        self.main_window.ui.chairUnfoldCallButton.setAutoRepeat(True)
        self.main_window.ui.footrestFoldCallButton.setAutoRepeat(True)
        self.main_window.ui.footrestUnfoldCallButton.setAutoRepeat(True)
        self.main_window.ui.swivelLeftCallButton.setAutoRepeat(True)
        self.main_window.ui.swivelCentreCallButton.setAutoRepeat(True)
        self.main_window.ui.swivelRightCallButton.setAutoRepeat(True)
        self.main_window.ui.localLeftCallButton.setAutoRepeat(True)
        self.main_window.ui.localRightCallButton.setAutoRepeat(True)
        self.main_window.ui.remoteUpCallButton.setAutoRepeat(True)
        self.main_window.ui.remoteDownCallButton.setAutoRepeat(True)

        # Set the initial page of the stacked widget.
        self.main_window.ui.stackedWidget.setCurrentIndex(0)

        # Connect the stacked widget's page change signal to update button styles.
        self.main_window.ui.stackedWidget.currentChanged.connect(self.updateButtons)

        # Update button styles to reflect the current page.
        self.updateButtons()

        # Heartbeat setup.
        self.heartbeat_poll_time_ms = 4000
        self.heartbeat_timeout_s    = 8
        self.led_heartbeat_time_ms  = 500
        self.heartbeat_receive_time = 0
        self.heartbeat              = False
        self.send_heartbeat_timer   = QTimer()
        self.led_heartbeat_timer    = QTimer()

        self.send_heartbeat_timer.timeout.connect(self.sendHeartbeat)
        self.led_heartbeat_timer.timeout.connect(self.toggleHeartbeatLED)


    def goToADCIO(self):
        """
        Changes the current stacked widget to the ADC/IO page.
        """
        self.main_window.ui.stackedWidget.setCurrentIndex(0)
        self.updateButtons()


    def goToColourPalette(self):
        """
        Changes the current stacked widget to the colour palette page.
        """
        if self.main_window.ui_colour_creator is None:
            self.main_window.ui_colour_creator = UIColourCreator(self.main_window)
        self.main_window.ui.stackedWidget.setCurrentIndex(1)
        self.updateButtons()


    def goToConfiguration(self):
        """
        Changes the current stacked widget to the configuration page.
        """
        if self.main_window.ui_config is None:
            self.main_window.ui_config = UIConfig(self.main_window)
        self.main_window.ui.stackedWidget.setCurrentIndex(2)
        self.updateButtons()


    def goToKeyWiring(self):
        """
        Changes the current stacked widget to the key wiring page.
        """
        if self.main_window.ui_key_wiring is None:
            self.main_window.ui_key_wiring = UIKeyWiring(self.main_window)
        self.main_window.ui.stackedWidget.setCurrentIndex(3)
        self.updateButtons()


    def goToRailMapping(self):
        """
        Changes the current stacked widget to the rail mapping page.
        """
        if self.main_window.ui_rail_map is None:
            self.main_window.ui_rail_map = UIRailMap(self.main_window)
        self.main_window.ui.stackedWidget.setCurrentIndex(4)
        self.updateButtons()


    def goToSystem(self):
        """
        Changes the current stacked widget to the system page.
        """
        if self.main_window.ui_system is None:
            self.main_window.ui_system = UISystem(self.main_window)
        self.main_window.ui.stackedWidget.setCurrentIndex(5)
        self.updateButtons()


    def goToX06(self):
        """
        Changes the current stacked widget to the X06 page.
        """
        if self.main_window.ui_x06 is None:
            self.main_window.ui_x06 = UIX06(self.main_window)
        self.main_window.ui.stackedWidget.setCurrentIndex(6)
        self.updateButtons()


    def goToChairFold(self):
        """
        Changes the current stacked widget to the chair fold page.
        """
        self.main_window.ui.stackedWidget.setCurrentIndex(7)
        self.updateButtons()


    def goToFootrest(self):
        """
        Changes the current stacked widget to the footrest page.
        """
        self.main_window.ui.stackedWidget.setCurrentIndex(8)
        self.updateButtons()


    def goToMainDrive(self):
        """
        Changes the current stacked widget to the main drive page.
        """
        self.main_window.ui.stackedWidget.setCurrentIndex(9)
        self.updateButtons()


    def goToSwivel(self):
        """
        Changes the current stacked widget to the swivel page.
        """
        self.main_window.ui.stackedWidget.setCurrentIndex(10)
        self.updateButtons()


    def updateButtons(self):
        """
        Updates the style of all buttons based on which one is active.
        """
        # Map page indices to their corresponding navigation buttons.
        buttons = {
            0:  self.main_window.ui.ADCIOPageButton,
            1:  self.main_window.ui.colourPalettePageButton,
            2:  self.main_window.ui.configurationPageButton,
            3:  self.main_window.ui.keyWiringPageButton,
            4:  self.main_window.ui.railMappingPageButton,
            5:  self.main_window.ui.systemPageButton,
            6:  self.main_window.ui.x06PageButton,
            7:  self.main_window.ui.chairFoldPageButton,
            8:  self.main_window.ui.footrestPageButton,
            9: self.main_window.ui.mainDrivePageButton,
            10: self.main_window.ui.swivelPageButton
        }

        # Reset all buttons.
        for button in buttons.values():
            button.setStyleSheet(Styles.BUTTON_INACTIVE)

        # Set the active button.
        current_index = self.main_window.ui.stackedWidget.currentIndex()
        if current_index in buttons:
            buttons[current_index].setStyleSheet(Styles.BUTTON_ACTIVE)


    def sendCall(self, call_ID, call):
        """
        Sends a call request of a specific ID and type.

        @param call_ID: Message ID for the call (software or diagnostic)
        @param call: Diag call type.
        """
        # Repeat call if selected.
        if self.repeating_call:
            self.main_window.ui.repeatCallButton.setStyleSheet(Styles.BUTTON_FLASH_ON) # Start flashing with green
            self.main_window.ui.repeatCallButton.setText(f"Repeating {self.convertCurrentCall(call_ID, call)} - Press to stop")
            self.call_to_repeat = call_ID, call
            self.repeating_call_timer.start(100)
            self.flash_call_button_timer.start(500)
        else:
            self.main_window.ui_comms.sendMessage(call_ID, "B", [call.value], SrcDest.SRC_DEST_X04, MsgMode.SET)


    def convertCurrentCall(self, call_type, call):
        """
        Converts call type to a string for the repeat call button.

        @param call_type: Diagnostic or software call.
        @param call: Call type.
        @return: String representation of call type.
        """
        if MessageID.CALL_REQUEST == call_type:
            if CallType.doesValueExist(call.value):
                return CallType.getName(call.value)
        else:
            if DiagnosticCall.doesValueExist(call.value):
                return DiagnosticCall.getName(call.value)

        return "Unknown call"


    def repeatCall(self):
        """
        Acts on the repeat call button being pressed.
        """
        # Reset the current call and timers.
        self.repeating_call_timer.stop()
        self.flash_call_button_timer.stop()
        if self.repeating_call:
            # Stop repeating call.
            self.main_window.ui.repeatCallButton.setStyleSheet(f"""
                                                            QPushButton {{
                                                                color: {Colours.BLACK.name()};                  /* Text color */
                                                                border: 2px solid {Colours.BLACK.name()};       /* Border color */
                                                                border-radius: 5px;                             /* Rounded corners */
                                                                background-color: {Colours.PALE_GREEN.name()};  /* Green background */
                                                            }}
                                                            """)
            self.main_window.ui.repeatCallButton.setText("Click to repeat a call")
            self.repeating_call = False
            self.call_to_repeat = None
        else:
            # Start repeating call.
            self.main_window.ui.repeatCallButton.setStyleSheet(f"""
                                                                QPushButton {{
                                                                    color: {Colours.BLACK.name()};                  /* Text color */
                                                                    border: 2px solid {Colours.BLACK.name()};       /* Border color */
                                                                    border-radius: 5px;                             /* Rounded corners */
                                                                    background-color: {Colours.LIGHT_PINK.name()};  /* Red background */
                                                                }}
                                                                """)
            self.main_window.ui.repeatCallButton.setText("Select a call to repeat")
            self.repeating_call = True


    def sendPeriodicCall(self):
        """
        Sends periodic call if call to repeat is active.
        """
        if self.call_to_repeat is not None:
            self.main_window.ui_comms.sendMessage(self.call_to_repeat[0], "B", [self.call_to_repeat[1].value], SrcDest.SRC_DEST_X04, MsgMode.SET)


    def flashCallButton(self):
        """
        When a call is repeated, the button will flash.
        """
        if self.repeating_call:
            current_style = self.main_window.ui.repeatCallButton.styleSheet()
            new_style = Styles.BUTTON_FLASH_OFF if current_style == Styles.BUTTON_FLASH_ON else Styles.BUTTON_FLASH_ON
            self.main_window.ui.repeatCallButton.setStyleSheet(new_style)


    def buttonTest1(self):
        """
        Test button 1 action.
        """
        self.main_window.ui_misc.updateECodeChanged(bytes(0x5E))
        self.main_window.ui_console.logDebugConsole("Test button 1 pressed")


    def buttonTest2(self):
        """
        Test button 2 action.
        """
        self.main_window.ui_console.logDebugConsole("Test button 2 pressed")


    def buttonTest3(self):
        """
        Test button 3 action.
        """
        self.main_window.ui_console.logDebugConsole("Test button 3 pressed")


    def buttonTest4(self):
        """
        Test button 4 action.
        """
        self.main_window.ui_console.logDebugConsole("Test button 4 pressed")


    def buttonTest5(self):
        """
        Test button 5 action.
        """
        self.main_window.ui_console.logDebugConsole("Test button 5 pressed")


    ########## Heartbeat Methods ##########


    def heartbeatReceived(self):
        """
        Updates the heartbeat receive timer to the current time.
        """
        self.heartbeat_receive_time = time()


    def sendHeartbeat(self):
        """
        Sends a heartbeat message to the connected device.
        """
        self.main_window.ui_comms.sendMessage(MessageID.HEARTBEAT, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ)


    def startHeartbeatTimer(self):
        """
        Starts the heartbeat timer.
        """
        self.send_heartbeat_timer.start(self.heartbeat_poll_time_ms)


    def startLEDHeartbeatTimer(self):
        """
        Starts the LED heartbeat timer.
        """
        self.led_heartbeat_timer.start(self.led_heartbeat_time_ms)


    def stopHeartbeatTimer(self):
        """
        Stops the heartbeat timer.
        """
        self.send_heartbeat_timer.stop()


    def stopLEDHeartbeatTimer(self):
        """
        Stops the LED heartbeat timer.
        """
        self.led_heartbeat_timer.stop()
        self.setHeartbeatLED(False)  # Ensure the LED is turned off when stopping the timer.


    def toggleHeartbeatLED(self):
        """
        Toggles the heartbeat LED in the GUI.
        """
        if self.main_window.ui_comms.serial_port_handler.serial_handler is None: # This may need to be more robust and use hasattr checks.
            is_healthy = False
        else:
            is_healthy = (self.main_window.ui_comms.serial_port_handler.serial_handler.isCommunicating() and
                        (time() - self.heartbeat_receive_time) < self.heartbeat_timeout_s)

        self.setHeartbeatLED(is_healthy)


    def setHeartbeatLED(self, healthy):
        """
        Updates the heartbeat LED in the GUI to reflect the current heartbeat state.

        Args:
            healthy:    Toggle the LED if healthy, else force it off.
        """
        if healthy:
            self.heartbeat = not self.heartbeat # Still receiving, toggle the LED state.
        else:
            self.heartbeat = False # Force the LED to turn off if we have lost heartbeat comms.

        self.main_window.ui.heartbeatLED.setChecked(self.heartbeat)