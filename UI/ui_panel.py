from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout
from UI.ui_colour_creator import UIColourCreator
from UI.ui_custom_widgets import ScalableLabel
from UI.ui_demo import UIDemo
from UI.ui_styling import Styles


class UIPanel:
    """
    Class for the UI panel. Handles navigation within the main application panel.
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
        pixmap = QPixmap("Images/Metrics-Stannah-Logo.png")
        self.image_label.setPixmap(pixmap)
        image_frame_layout = QVBoxLayout(self.main_window.ui.imageFrame)
        image_frame_layout.addWidget(self.image_label)

        # Connect buttons to their respective functions.
        self.main_window.ui.ADCIOPageButton.clicked.connect(lambda: self.goToADCIO())
        self.main_window.ui.colourPalettePageButton.clicked.connect(lambda: self.goToColourPalette())
        self.main_window.ui.enableDemoModeButton.toggled.connect(self.handleDemoMode)
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


    def handleDemoMode(self):
        """
        Handles toggling of the demo mode button.
        """
        if self.main_window.ui.enableDemoModeButton.isChecked():
            # Prevent demo mode from running if a serial port is connected.
            if self.main_window.ui_comms.serial_port_handler.connected():
                self.main_window.ui_console.logDebugConsole("Demo mode cannot be enabled whilst a serial port is connected.")

                # Temporarily block the signal to prevent recursion.
                self.main_window.ui.enableDemoModeButton.blockSignals(True)
                self.main_window.ui.enableDemoModeButton.setChecked(False)
                self.main_window.ui.enableDemoModeButton.blockSignals(False)
            else:
                if self.main_window.ui_demo is None:
                    self.main_window.ui_demo = UIDemo(self.main_window)
                self.main_window.ui_demo.start()
        else:
            if self.main_window.ui_demo is not None:
                self.main_window.ui_demo.stop()
                self.main_window.ui_demo = None