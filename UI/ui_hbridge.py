# Standard library imports.
from functools import partial

# Local application imports.
from Enums.enum_diag import DiagRequests
from Enums.enum_drive_control import DriveControlDir
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from Enums.enum_system_drives import SystemDrive


class UIHBridge():
    """
    Class for the H-bridge UI.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        # Sliders go back to zero when released by default unless the hold button is checked.
        for prefix in ["chair", "footrest", "main", "swivel"]:
            left_hold = getattr(self.main_window.ui, f"{prefix}HoldLeftDutyButton")
            right_hold = getattr(self.main_window.ui, f"{prefix}HoldRightDutyButton")
            left_slider = getattr(self.main_window.ui, f"{prefix}LeftBridgeDuty")
            right_slider = getattr(self.main_window.ui, f"{prefix}RightBridgeDuty")

            # Prevent clicks from being registered to move the slider.
            left_slider.setPageStep(0)
            right_slider.setPageStep(0)

            # Set slider value to 0 when released if the hold button is not checked.
            left_slider.sliderReleased.connect(partial(lambda hold, slider: slider.setValue(0) if not hold.isChecked() else None, left_hold, left_slider))
            right_slider.sliderReleased.connect(partial(lambda hold, slider: slider.setValue(0) if not hold.isChecked() else None, right_hold, right_slider))
            left_hold.clicked.connect(partial(lambda hold, slider: slider.setValue(0) if not hold.isChecked() else None, left_hold, left_slider))
            right_hold.clicked.connect(partial(lambda hold, slider: slider.setValue(0) if not hold.isChecked() else None, right_hold, right_slider))

            # Update the text box when the slider is moved.
            left_slider.valueChanged.connect(lambda value, p=prefix: getattr(self.main_window.ui, f"{p}LeftBridgeText").setText(f"{value}%"))
            right_slider.valueChanged.connect(lambda value, p=prefix: getattr(self.main_window.ui, f"{p}RightBridgeText").setText(f"{value}%"))

            # Transmit message with new duty.
            left_slider.valueChanged.connect(lambda value, p=prefix, dir=DriveControlDir.LEFT: self.updateDuty(p, dir, value))
            right_slider.valueChanged.connect(lambda value, p=prefix, dir=DriveControlDir.RIGHT: self.updateDuty(p, dir, value))

        # Allow changing of sliders min/max values via text box.
        for prefix in ["Chair", "Footrest", "Main", "Swivel"]:
            max_pwm = getattr(self.main_window.ui, f"max{prefix}PWM")
            min_pwm = getattr(self.main_window.ui, f"min{prefix}PWM")

            max_pwm.editingFinished.connect(lambda p=prefix: (self.main_window.ui.update_slider_min_max(p, True), max_pwm.clearFocus()))
            min_pwm.editingFinished.connect(lambda p=prefix: (self.main_window.ui.update_slider_min_max(p, False), min_pwm.clearFocus()))


    def update_slider_min_max(self, prefix, is_max):
        """
        User has changed the min/max values of the slider. Update the slider min/max values accordingly.

        Args:
            prefix: Prefix of the slider to update.
            is_max: True if the user is changing the max value, False if the user is changing the min value.
        """
        if prefix == "Chair":
            left_slider = self.main_window.ui.chairLeftBridgeDuty
            right_slider = self.main_window.ui.chairRightBridgeDuty
            text = self.main_window.ui.maxChairPWM if is_max else self.main_window.ui.minChairPWM
        elif prefix == "Footrest":
            left_slider = self.main_window.ui.footrestLeftBridgeDuty
            right_slider = self.main_window.ui.footrestRightBridgeDuty
            text = self.main_window.ui.maxFootrestPWM if is_max else self.main_window.ui.minFootrestPWM
        elif prefix == "Main":
            left_slider = self.main_window.ui.mainLeftBridgeDuty
            right_slider = self.main_window.ui.mainRightBridgeDuty
            text = self.main_window.ui.maxMainPWM if is_max else self.main_window.ui.minMainPWM
        elif prefix == "Swivel":
            left_slider = self.main_window.ui.swivelLeftBridgeDuty
            right_slider = self.main_window.ui.swivelRightBridgeDuty
            text = self.main_window.ui.maxSwivelPWM if is_max else self.main_window.ui.minSwivelPWM
        else:
            print("Unknown prefix")
            return

        try:
            value = int(text.text())
            if is_max:
                left_slider.setMaximum(value)
                right_slider.setMaximum(value)
            else:
                left_slider.setMinimum(value)
                right_slider.setMinimum(value)

            # When either sliders max/min are adjusted, both sliders are set to the minimum value.
            left_slider.setValue(left_slider.minimum())
            right_slider.setValue(right_slider.minimum())

        except ValueError as e:
            print(f"E1: {__file__}: {e}")


    def updateDuty(self, drive, dir, duty):
        """
        Transmits message to update the drive duty

        Args:
            drive: The chosen drive.
            dir: Which side of the bridge to drive.
            duty: The new duty.
        """
        enableButton = getattr(self.main_window.ui, f"enable{drive.capitalize()}BridgeButton")
        if drive == "chair":
            dest = SrcDest.SRC_DEST_X01
            drive = SystemDrive.SYS_DRIVE_CHAIR_FOLD.value
        elif drive == "footrest":
            dest = SrcDest.SRC_DEST_X04
            drive = SystemDrive.SYS_DRIVE_FOOTREST.value
        elif drive == "main":
            dest = SrcDest.SRC_DEST_X04
            drive = SystemDrive.SYS_DRIVE_MAIN_DRIVE.value
        else:
            dest = SrcDest.SRC_DEST_X01
            drive = SystemDrive.SYS_DRIVE_SWIVEL.value

        if dir == DriveControlDir.LEFT:
            duty = -duty

        if enableButton.isChecked():
            self.main_window.ui_console.logDebugConsole(f"{SystemDrive(drive).name}, {dir.name}, {duty}")
            self.main_window.ui_comms.sendMessage(MessageID.DIAGNOSTIC_REQUEST, "H4i", [DiagRequests.DIAG_REQ_MANUAL_DUTY.value, duty, drive, 0, 0], dest, MsgMode.SET)
