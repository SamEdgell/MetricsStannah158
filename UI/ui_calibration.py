# Local application imports.
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from Enums.enum_system_drives import SystemDrive


class UICalibration:
    """
    Class for the calibration.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        self.driveData = {
            "Chair":    {"dest": SrcDest.SRC_DEST_X01, "driveID": SystemDrive.SYS_DRIVE_CHAIR_FOLD.value},
            "Footrest": {"dest": SrcDest.SRC_DEST_X04, "driveID": SystemDrive.SYS_DRIVE_FOOTREST.value},
            "Main":     {"dest": SrcDest.SRC_DEST_X04, "driveID": SystemDrive.SYS_DRIVE_MAIN_DRIVE.value},
            "Swivel":   {"dest": SrcDest.SRC_DEST_X01, "driveID": SystemDrive.SYS_DRIVE_SWIVEL.value}
        }

        for drive in self.driveData.keys():
            startButton     = getattr(self.main_window.ui, f"start{drive}CalButton")
            acceptButton    = getattr(self.main_window.ui, f"accept{drive}CalButton")
            rejectButton    = getattr(self.main_window.ui, f"reject{drive}CalButton")
            autoButton      = getattr(self.main_window.ui, f"auto{drive}CalButton")
            manualButton    = getattr(self.main_window.ui, f"manual{drive}CalButton")

            startButton.clicked.connect(lambda checked, d=drive: self.startCalibration(d))
            acceptButton.clicked.connect(lambda checked, d=drive: self.acceptCalibration(d))
            rejectButton.clicked.connect(lambda checked, d=drive: self.rejectCalibration(d))

            autoButton.toggled.connect(lambda checked, d=drive: self.autoCalibration(d, checked))
            manualButton.toggled.connect(lambda checked, d=drive: self.manualCalibration(d, checked))


    def startCalibration(self, drive):
        """
        Starts the calibration process for the specified component.

        Args:
            drive: The component to calibrate.
        """
        data = self.driveData.get(drive)
        if data:
            self.main_window.ui_comms.sendMessage(MessageID.CALIBRATION_REQUEST, "B", [data["driveID"]], data["dest"], MsgMode.SET)


    def acceptCalibration(self, drive):
        """
        Accepts the calibration process for the specified component.

        Args:
            drive: The component to accept calibration for.
        """
        data = self.driveData.get(drive)
        if data:
            self.main_window.ui_comms.sendMessage(MessageID.END_CALIBRATION, "B", [True], data["dest"], MsgMode.SET)


    def rejectCalibration(self, drive):
        """
        Rejects the calibration process for the specified component.

        Args:
            drive: The component to reject calibration for.
        """
        data = self.driveData.get(drive)
        if data:
            self.main_window.ui_comms.sendMessage(MessageID.END_CALIBRATION, "B", [False], data["dest"], MsgMode.SET)


    def autoCalibration(self, drive, checked):
        """
        Selects auto calibration for the specified component.

        Args:
            drive: The component to select auto calibration for.
            checked: The toggled signal.
        """
        if checked:
            getattr(self.main_window.ui, f"accept{drive}CalButton").setEnabled(False)
            getattr(self.main_window.ui, f"reject{drive}CalButton").setEnabled(False)


    def manualCalibration(self, drive, checked):
        """
        Selects manual calibration for the specified component.

        Args:
            drive: The component to select manual calibration for.
            checked: The toggled signal.
        """
        if checked:
            getattr(self.main_window.ui, f"accept{drive}CalButton").setEnabled(True)
            getattr(self.main_window.ui, f"reject{drive}CalButton").setEnabled(True)