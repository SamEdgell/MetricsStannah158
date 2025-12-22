# Third party imports.
from PySide6.QtCore import QTimer

# Local application imports.
from Enums.enum_msg import MessageID, MsgMode, SrcDest


class UIX06:
    """
    Class for handling X06 data.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        self.main_window.ui.enableX06MessagesButton.toggled.connect(self.handleX06Button)
        self.isEnabled = False


    def handleX06Button(self):
        """
        The X06 radio button has been clicked.
        """
        if self.main_window.ui.enableX06MessagesButton.isChecked():
            self.isEnabled = True
            self.requestADCData(self.isEnabled)
            self.requestGPIOData(self.isEnabled)
        else:
            self.isEnabled = False
            self.requestADCData(self.isEnabled)
            self.requestGPIOData(self.isEnabled)


    def requestADCData(self, start):
        """
        Starts or stops sending requests for ADC X06 data.

        Args:
            start: To start timer or stop it.
        """
        if start:
            self.getADCStatus = QTimer()
            self.getADCStatus.timeout.connect(lambda: self.mainWindow.ui_comms.sendMessage(MessageID.ADC_STATUS, "", [], SrcDest.SRC_DEST_X01, MsgMode.GET))
            self.getADCStatus.timeout.connect(lambda: self.mainWindow.ui_comms.sendMessage(MessageID.ADC_STATUS, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET))
            self.getADCStatus.start(800)
        else:
            self.getADCStatus.stop()


    def requestGPIOData(self, start):
        """
        Starts or stops sending requests for GPIO X06 data.

        Args:
            start: To start timer or stop it.
        """
        if start:
            self.getInputStatus = QTimer()
            self.getInputStatus.timeout.connect(lambda: self.mainWindow.ui_comms.sendMessage(MessageID.GPIO_INPUT_STATUS, "", [], SrcDest.SRC_DEST_X01, MsgMode.GET))
            self.getInputStatus.timeout.connect(lambda: self.mainWindow.ui_comms.sendMessage(MessageID.GPIO_INPUT_STATUS, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET))
            self.getInputStatus.start(800)

            self.getOutputStatus = QTimer()
            self.getOutputStatus.timeout.connect(lambda: self.mainWindow.ui_comms.sendMessage(MessageID.GPIO_OUTPUT_STATUS, "", [], SrcDest.SRC_DEST_X01, MsgMode.GET))
            self.getOutputStatus.timeout.connect(lambda: self.mainWindow.ui_comms.sendMessage(MessageID.GPIO_OUTPUT_STATUS, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET))
            self.getOutputStatus.start(800)
        else:
            self.getInputStatus.stop()
            self.getOutputStatus.stop()