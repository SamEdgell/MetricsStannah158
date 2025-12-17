# Standard library imports.
import threading
import multiprocessing
from time import time

# Third party imports.
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout

# Local application imports.
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from UI.ui_colour_creator import UIColourCreator
from UI.ui_custom_widgets import ScalableLabel
from UI.ui_styling import Styles
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
        self.main_window.ui.ADCIOPageButton.clicked.connect(lambda: self.goToADCIO())
        self.main_window.ui.colourPalettePageButton.clicked.connect(lambda: self.goToColourPalette())
        self.main_window.ui.testButton1.clicked.connect(lambda: self.buttonTest1())
        self.main_window.ui.testButton2.clicked.connect(lambda: self.buttonTest2())
        self.main_window.ui.testButton3.clicked.connect(lambda: self.buttonTest3())
        self.main_window.ui.testButton4.clicked.connect(lambda: self.buttonTest4())
        self.main_window.ui.testButton5.clicked.connect(lambda: self.buttonTest5())

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
        # As the colour creator component is not compulsory initialised, create one if it doesn't exist.
        if self.main_window.ui_colour_creator is None:
            self.main_window.ui_colour_creator = UIColourCreator(self.main_window)
        self.main_window.ui.stackedWidget.setCurrentIndex(1)
        self.updateButtons()


    def updateButtons(self):
        """
        Updates the style of all buttons based on which one is active.
        """
        # Map page indices to their corresponding navigation buttons.
        buttons = {
            0:  self.main_window.ui.ADCIOPageButton,
            1:  self.main_window.ui.colourPalettePageButton,
        }

        # Reset all buttons.
        for button in buttons.values():
            button.setStyleSheet(Styles.BUTTON_INACTIVE)

        # Set the active button.
        current_index = self.main_window.ui.stackedWidget.currentIndex()
        if current_index in buttons:
            buttons[current_index].setStyleSheet(Styles.BUTTON_ACTIVE)


    def buttonTest1(self):
        """
        Test button 1 action.
        """
        self.main_window.ui_console.logDebugConsole("Test button 1 pressed")
        from Utilities.plotter import createPlot # imported here to import only when needed. Prevents slower load time.
        if 0: # TODO Fix for future when PySide6 supports multithreading better.
            # Only run for 3.14t
            plot_thread = threading.Thread(target=createPlot, args=("PIDLogs/FR_PIDData_20250624_085727.csv",))
            plot_thread.daemon = True # Ensure the thread exits when the plot is closed.
            plot_thread.start()
        else:
            plot_process = multiprocessing.Process(target=createPlot, args=("PIDLogs/FR_PIDData_20250624_085727.csv",))
            plot_process.daemon = True # Ensure the process exits when the plot is closed.
            plot_process.start()


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
        self.main_window.ui_comms.sendMessage(MessageID.HEARTBEAT, "", [], SrcDest.SRC_DEST_ECU1, MsgMode.REQ)


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
        """"
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