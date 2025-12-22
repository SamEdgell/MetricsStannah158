# Standard library imports.
import re
from datetime import datetime
from enum import Enum, unique

# Local application imports.
from Enums.enum_calls_demands import BreakReasons, CallSource, CallType, DemandStates
from Enums.enum_drive_control import DriveControlDir, DriveSpeedProfiles
from Enums.enum_drive_state_machine import DriveState, MovingDriveState
from Enums.enum_drive_tests import DriveTest
from Enums.enum_ecodes import ECodes
from Enums.enum_errors import ErrorType
from Enums.enum_gpio import InputsX04, InputsX01, LogicState, OutputsX04, OutputsX01
from Enums.enum_metrics import MetricSubcodes
from Enums.enum_msg import MsgMode, SrcDest
from Enums.enum_rmu import RMUStates
from Enums.enum_system import OperationalMode, SystemState, UpDirection
from Enums.enum_uuid import UUID
from UI.ui_styling import Colours, CSS
from Utilities.messages import unpackMessage


"""
Metrics handler expects to receive messages in the following format:

Message Header:
    Message ID (1 byte) | Size (2 bytes) | Source (1 byte) | Destination (1 byte) | Mode (1 byte) | SRID (2 bytes)
Metric Payload:
    Metric Subcode (2 bytes) | Timestamp (8 bytes) | Sequence Number (2 bytes) | UUID (4 bytes) | Mode (4 bytes) | Data1 (4 bytes) | Data2 (4 bytes) | Data3 (4 bytes) | Data4 (4 bytes)
"""
METRIC_PAYLOAD_FORMAT = "HQH6I"


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@unique
class MessageStyleCode(Enum):
    """
    Enum for style codes used to display metric messages on the UIConsole.
    Inherits from Python's Enum to provide a set of unique, type-safe constants that are used as keys for CSS styling and message formatting.
    """
    COMPONENT_FAULT         = 0x0000

    DRIVE_STATE_CHANGE      = 0x0040
    DRIVE_MAIN              = 0x0043

    CALL                    = 0x0050
    DEMAND_STATE_CHANGE     = 0x0052
    DEMAND_BREAK_REASON     = 0x0053

    DRIVE_TESTS             = 0x0100

    BRAKE                   = 0x0240

    CALIBRATION             = 0x0300

    # Non Metric specific styles Below.
    TEST                    = 0xFFF8
    WARNING                 = 0xFFF9
    PASS                    = 0xFFFA
    DEFAULT                 = 0xFFFB
    ERROR                   = 0xFFFC
    SEQUENCE_NUMBER         = 0xFFFD
    TIME_STAMP_EVEN         = 0xFFFE
    TIME_STAMP_ODD          = 0xFFFF


# All possible style codes for the metric messages displayed on the UIConsole.
CSS_STYLE = {
    MessageStyleCode.COMPONENT_FAULT:           f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",

    MessageStyleCode.DRIVE_STATE_CHANGE:        f"color: {Colours.BLACK.name()}; background-color: {Colours.PASTEL_PINK.name()};",
    MessageStyleCode.DRIVE_MAIN:                f"color: {Colours.BLACK.name()}; background-color: {Colours.LIME_GREEN.name()};",
    MessageStyleCode.CALL:                      f"color: {Colours.BLACK.name()}; background-color: {Colours.PERIWINKLE.name()};",
    MessageStyleCode.DEMAND_STATE_CHANGE:       f"color: {Colours.AMBER.name()}; background-color: {Colours.FOREST_GREEN.name()};",
    MessageStyleCode.DEMAND_BREAK_REASON:       f"color: {Colours.BLACK.name()}; background-color: {Colours.GOLDEN_YELLOW.name()};",
    MessageStyleCode.DRIVE_TESTS:               f"color: {Colours.BLACK.name()}; background-color: {Colours.BRIGHT_CYAN.name()};",
    MessageStyleCode.BRAKE:                     f"color: {Colours.BLACK.name()}; background-color: {Colours.ELECTRIC_LIME.name()};",
    MessageStyleCode.CALIBRATION:               f"color: {Colours.BLACK.name()}; background-color: {Colours.LAVENDER.name()};",

    # Non Metric specific styles Below.
    MessageStyleCode.TEST:                      f"color: {Colours.BLACK.name()}; background-color: {Colours.YELLOW.name()};",
    MessageStyleCode.WARNING:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.MARIGOLD.name()};",
    MessageStyleCode.PASS:                      f"color: {Colours.BLACK.name()}; background-color: {Colours.KELLY_GREEN.name()};",
    MessageStyleCode.DEFAULT:                   f"color: {Colours.BLACK.name()};",
    MessageStyleCode.ERROR:                     f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",
    MessageStyleCode.SEQUENCE_NUMBER:           f"color: {Colours.GARNET.name()}",
    MessageStyleCode.TIME_STAMP_EVEN:           f"color: {Colours.BLACK.name()}; background-color: {Colours.GOLD.name()};",
    MessageStyleCode.TIME_STAMP_ODD:            f"color: {Colours.BLACK.name()}; background-color: {Colours.BABY_BLUE.name()};",
}


# Maps a metric subcode to a CSS style code and the desired string to be displayed on the console for that subcode. Further CSS styling of placeholders is handled inside the customisePlaceholders function.
METRIC_SUBCODE_MAPPER = {
    # Subcode Member                                        CSS Style                                   String
    MetricSubcodes.METRIC_INVALID:                          [MessageStyleCode.ERROR,                    "METRIC_INVALID"],

    MetricSubcodes.METRIC_POWER_UP:                         [MessageStyleCode.PASS,                     "System Powered Up"],
    MetricSubcodes.METRIC_EXCEPTION:                        [MessageStyleCode.DEFAULT,                  "Restarted: {0:ErrorType} - Line: {1}, Address: 0x{2:x8}, Tick Count: {3}ms"],
    MetricSubcodes.METRIC_GENERIC_OUTPUT:                   [MessageStyleCode.DEFAULT,                  "Generic Output: {0} {1} {2} {2}"],
    MetricSubcodes.METRIC_SEPARATOR:                        [MessageStyleCode.DEFAULT,                  "-------------------------------------------------------------------"],
    MetricSubcodes.METRIC_TASK_OVERRUN_DUE_FS:              [MessageStyleCode.ERROR,                    "Task Overrun: {0} {1} {2}"],
    MetricSubcodes.METRIC_RESTART_FILENAME:                 [MessageStyleCode.DEFAULT,                  "Restarted: {0:CHAR4} {1:CHAR4} {2:CHAR4} {3:CHAR4}"],
    MetricSubcodes.METRIC_TIME_POWERED_OFF:                 [MessageStyleCode.DEFAULT,                  "ECU Time Powered Off: {0:PoweredOff}"],

    MetricSubcodes.METRIC_INPUT_STATE_CHANGE:               [MessageStyleCode.DEFAULT,                  "GPIO {0:GPIO_INPUTS} = {1:LOGIC_STATE}"],
    MetricSubcodes.METRIC_OUTPUT_STATE_CHANGE:              [MessageStyleCode.DEFAULT,                  "GPIO {0:GPIO_OUTPUTS} = {1:LOGIC_STATE}"],
    MetricSubcodes.METRIC_INPUT_DEB_FAULT:                  [MessageStyleCode.ERROR,                    "GPIO Debounce Fault: {0:GPIO_INPUTS}"],
    MetricSubcodes.METRIC_OUTPUT_DEB_FAULT:                 [MessageStyleCode.ERROR,                    "GPIO Debounce Fault: {0:GPIO_OUTPUTS}"],

    MetricSubcodes.METRIC_SYS_OPERATIONAL_STATE:            [MessageStyleCode.DEFAULT,                  "System State Changed: {0:SystemState}"],
    MetricSubcodes.METRIC_HARDWARE_LAYER_INIT:              [MessageStyleCode.DEFAULT,                  "Hardware Layer Initialised"],
    MetricSubcodes.METRIC_SERVICE_LAYER_INIT:               [MessageStyleCode.DEFAULT,                  "Service Layer Initialised"],
    MetricSubcodes.METRIC_CONTROL_LAYER_INIT:               [MessageStyleCode.DEFAULT,                  "Control Layer Initialised"],
    MetricSubcodes.METRIC_TASK_SETUP_COMPLETE:              [MessageStyleCode.DEFAULT,                  "Tasks Setup Complete"],
    MetricSubcodes.METRIC_COMPONENT_FAULT:                  [MessageStyleCode.COMPONENT_FAULT,          "Faulted: [{UUID1}] [{0:ECodes}] [{3:SUBCODE}]"],
    MetricSubcodes.METRIC_OPERATIONAL_MODE:                 [MessageStyleCode.DEFAULT,                  "Operational Mode Changed: {0:OperationalMode}"],
    MetricSubcodes.METRIC_HANDING_LINK_UNKNOWN:             [MessageStyleCode.ERROR,                    "Handling Link Unknown"],

    MetricSubcodes.METRIC_SD_CARD_PRESENT:                  [MessageStyleCode.DEFAULT,                  "SD Card Present"],
    MetricSubcodes.METRIC_SD_CARD_NOT_PRESENT:              [MessageStyleCode.ERROR,                    "SD Card Not Present"],
    MetricSubcodes.METRIC_SD_CARD_MOUNT_OK:                 [MessageStyleCode.DEFAULT,                  "SD Card Mounted"],
    MetricSubcodes.METRIC_SD_CARD_MOUNT_FAILED:             [MessageStyleCode.ERROR,                    "SD Card Not Mounted"],

    MetricSubcodes.METRIC_RMU_STATE_CHANGE:                 [MessageStyleCode.WARNING,                  "RMU State Changed: {0:RMUStates}"],

    MetricSubcodes.METRIC_DRIVE_STATE:                      [MessageStyleCode.DRIVE_STATE_CHANGE,       "{UUID}: {0:DriveState}"],
    MetricSubcodes.METRIC_DRIVE_PROFILER_SPEED_CHG:         [MessageStyleCode.DEFAULT,                  "Drive Profiler Speed Changed."],
    MetricSubcodes.METRIC_DRIVE_MAIN_RECOVERED_POS:         [MessageStyleCode.DRIVE_MAIN,               "Main Drive Position Recovered: {0:s32}"],
    MetricSubcodes.METRIC_DRIVE_MAIN_START_POS:             [MessageStyleCode.DRIVE_MAIN,               "Main Drive Start Position: {0:s32}"],
    MetricSubcodes.METRIC_DRIVE_MAIN_TARGET_POS:            [MessageStyleCode.DRIVE_MAIN,               "Main Drive Target Position: {0:s32}"],
    MetricSubcodes.METRIC_DRIVE_MAIN_MAX_SPEED:             [MessageStyleCode.DRIVE_MAIN,               "Main Drive Max Speed: {0:DriveSpeedProfiles}"],
    MetricSubcodes.METRIC_DRIVE_MAIN_HB_BRIDGE_USED:        [MessageStyleCode.DRIVE_MAIN,               "Main Drive Bridge: {0:DriveControlDir}"],
    MetricSubcodes.METRIC_DRIVE_MAIN_NO_TARGET_POS:         [MessageStyleCode.DRIVE_MAIN,               "Main Drive No Target Position Set."],
    MetricSubcodes.METRIC_DRIVE_MAIN_DEMAND_REMOVED:        [MessageStyleCode.DRIVE_MAIN,               "Main Drive Demand Removed."],
    MetricSubcodes.METRIC_DRIVE_MAIN_SAFETY_STOP:           [MessageStyleCode.ERROR,                    "Main Drive Safety Stop."],

    MetricSubcodes.METRIC_CALL_PLACED:                      [MessageStyleCode.CALL,                     "Call Placed. {0:CallSource} - {1:CallType}"],
    MetricSubcodes.METRIC_CALL_REMOVED:                     [MessageStyleCode.CALL,                     "Call Removed."],
    MetricSubcodes.METRIC_DEMAND_STATE_CHANGE:              [MessageStyleCode.DEMAND_STATE_CHANGE,      "Demand: {0:DemandStates}"],
    MetricSubcodes.METRIC_DEMAND_BREAK_REASON:              [MessageStyleCode.DEMAND_BREAK_REASON,      "Demand Break: {0:BreakReasons}"],

    MetricSubcodes.METRIC_FILE_LOAD_ERROR:                  [MessageStyleCode.ERROR,                    "Last Fault Corruption"],

    # ---------- Drive Tests Start ----------
    MetricSubcodes.METRIC_DT_STARTED_PRE:                   [MessageStyleCode.DRIVE_TESTS,              "{UUID} Pre-Run Started"],
    MetricSubcodes.METRIC_DT_STARTED_POST:                  [MessageStyleCode.DRIVE_TESTS,              "{UUID} Post-Run Started"],
    MetricSubcodes.METRIC_DT_STOPPED:                       [MessageStyleCode.DRIVE_TESTS,              "{UUID} Test Stopped"],
    MetricSubcodes.METRIC_DT_ABORTED:                       [MessageStyleCode.ERROR,                    "{UUID} Aborted"],
    MetricSubcodes.METRIC_DT_PASSED:                        [MessageStyleCode.PASS,                     "{UUID} Passed"],
    MetricSubcodes.METRIC_DT_FAILED:                        [MessageStyleCode.ERROR,                    "{UUID} Failed"],
    MetricSubcodes.METRIC_DT_STARTED:                       [MessageStyleCode.DRIVE_TESTS,              "{UUID} Test Started: {0:DriveTest}"],
    MetricSubcodes.METRIC_DT_TIMEOUT:                       [MessageStyleCode.ERROR,                    "{UUID} Timeout"],

    # Test 1 - Supply Volts
    MetricSubcodes.METRIC_DT_F_01_SUPL_NO_VOLTS:            [MessageStyleCode.ERROR,                    "PRC[1]: No Supply Voltage. {0:Volts}V, Min = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_01_SUPL_TOO_LOW:             [MessageStyleCode.ERROR,                    "PRC[1]: Supply Voltage Too Low. {0:Volts}V, Min = {2:Volts}V"],
    MetricSubcodes.METRIC_DT_F_01_SUPL_TOO_HIGH:            [MessageStyleCode.ERROR,                    "PRC[1]: Supply Voltage Too High. {0:Volts}V, Max = {2:Volts}V"],
    MetricSubcodes.METRIC_DT_P_01_SUPL_IN_RANGE:            [MessageStyleCode.PASS,                     "PRC[1]: Supply Voltage Pass. {0:Volts}V, Range = {1:Volts}V - {2:Volts}V"],

    # Test 2 - Left Drive Low
    MetricSubcodes.METRIC_DT_P_02_L_DRV_V_LOW:              [MessageStyleCode.PASS,                     "PRC[2]: Left Drive Volts Low. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_02_L_DRV_V_MID:              [MessageStyleCode.ERROR,                    "PRC[2]: Left Drive Volts Mid-range. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_02_L_DRV_V_HIGH:             [MessageStyleCode.ERROR,                    "PRC[2]: Left Drive Volts High. {0:Volts}V, Max = {1:Volts}V"],

    # Test 2 - Right Drive Low
    MetricSubcodes.METRIC_DT_P_02_R_DRV_V_LOW:              [MessageStyleCode.PASS,                     "PRC[2]: Right Drive Volts Low. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_02_R_DRV_V_MID:              [MessageStyleCode.ERROR,                    "PRC[2]: Right Drive Volts Mid-range. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_02_R_DRV_V_HIGH:             [MessageStyleCode.ERROR,                    "PRC[2]: Right Drive Volts High. {0:Volts}V, Max = {1:Volts}V"],

    # Test 3 - Left Drive Mid
    MetricSubcodes.METRIC_DT_P_03_L_DRV_V_MID_S1:           [MessageStyleCode.PASS,                     "PRC[3]: Left Drive Volts Mid-range. {0:Volts}V, Range = {1:Volts}V - {2:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_L_BOT_FET_SHORT_S1:       [MessageStyleCode.ERROR,                    "PRC[3]: Left Drive Volts Low. {0:Volts}V, Min = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_L_DRV_V_HIGH_S1:          [MessageStyleCode.ERROR,                    "PRC[3]: Left Drive Volts High. {0:Volts}V, Max = {1:Volts}V"],

    # Test 3 - Right Drive Mid
    MetricSubcodes.METRIC_DT_P_03_R_DRV_V_MID_S2:           [MessageStyleCode.PASS,                     "PRC[3]: Right Drive Volts Mid-range. {0:Volts}V, Range = {1:Volts}V - {2:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_R_BOT_FET_SHORT_S2:       [MessageStyleCode.ERROR,                    "PRC[3]: Right Drive Volts Low. {0:Volts}V, Min = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_R_DRV_V_HIGH_S2:          [MessageStyleCode.ERROR,                    "PRC[3]: Right Drive Volts High. {0:Volts}V, Max = {1:Volts}V"],

    # Test 3 - Left Drive Low
    MetricSubcodes.METRIC_DT_P_03_L_DRV_V_LOW_S4:           [MessageStyleCode.PASS,                     "PRC[3]: Left Drive Volts Low. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_L_BOT_FET_OPEN_S4:        [MessageStyleCode.ERROR,                    "PRC[3]: Left Drive Volts Mid-range. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_L_DRV_V_HIGH_S4:          [MessageStyleCode.ERROR,                    "PRC[3]: Left Drive Volts High. {0:Volts}V, Max = {1:Volts}V"],

    # Test 3 - Right Drive Low
    MetricSubcodes.METRIC_DT_P_03_R_DRV_V_LOW_S5:           [MessageStyleCode.PASS,                     "PRC[3]: Right Drive Volts Low. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_R_BOT_FET_OPEN_S5:        [MessageStyleCode.ERROR,                    "PRC[3]: Right Drive Volts Mid-range. {0:Volts}V, Max = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_03_R_DRV_V_HIGH_S5:          [MessageStyleCode.ERROR,                    "PRC[3]: Right Drive Volts High. {0:Volts}V, Max = {1:Volts}V"],

    MetricSubcodes.METRIC_DT_P_03_MOTOR_DETECTED:           [MessageStyleCode.PASS,                     "PRC[3]: Motor Detected."],
    MetricSubcodes.METRIC_DT_F_03_MOTOR_NOT_DET:            [MessageStyleCode.ERROR,                    "PRC[3]: Motor Not Detected."],

    MetricSubcodes.METRIC_DT_P_04_SKIP_LEFT_CHECK:          [MessageStyleCode.PASS,                     "PRC[4]: Skipped Left Top FET Check."],
    MetricSubcodes.METRIC_DT_P_04_SKIP_RIGHT_CHECK:         [MessageStyleCode.PASS,                     "PRC[4]: Skipped Right Top FET Check."],

    MetricSubcodes.METRIC_DT_P_04_L_DRV_V_HIGH:             [MessageStyleCode.PASS,                     "PRC[4]: Left Top FET On. {0:Volts}V, Min = {2:Volts}V"],
    MetricSubcodes.METRIC_DT_F_04_L_DRV_V_LOW:              [MessageStyleCode.ERROR,                    "PRC[4]: Left Top FET On. {0:Volts}V, Min = {2:Volts}V"],
    MetricSubcodes.METRIC_DT_F_04_L_DRV_V_MID_RAIL:         [MessageStyleCode.ERROR,                    "PRC[4]: Left Top FET On. {0:Volts}V, Min = {2:Volts}V"],

    MetricSubcodes.METRIC_DT_P_04_R_DRV_V_HIGH:             [MessageStyleCode.PASS,                     "PRC[4]: Right Top FET On. {0:Volts}V, Min = {2:Volts}V"],
    MetricSubcodes.METRIC_DT_F_04_R_DRV_V_LOW:              [MessageStyleCode.ERROR,                    "PRC[4]: Right Top FET On. {0:Volts}V, Min = {2:Volts}V"],
    MetricSubcodes.METRIC_DT_F_04_R_DRV_V_MID_RAIL:         [MessageStyleCode.ERROR,                    "PRC[4]: Right Top FET On. {0:Volts}V, Min = {2:Volts}V"],

    MetricSubcodes.METRIC_DT_P_11_SUPL_NO_VOLTS:            [MessageStyleCode.PASS,                     "PRC[11]: No Supply Voltage. {0:Volts}V, Min = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_11_SUPL_V_MID_RAIL:          [MessageStyleCode.ERROR,                    "PRC[11]: Supply Voltage Low. {0:Volts}V, Min = {1:Volts}V"],
    MetricSubcodes.METRIC_DT_F_11_SUPL_V_HIGH:              [MessageStyleCode.ERROR,                    "PRC[11]: Supply Voltage High. {0:Volts}V, Min = {1:VX1000}V"],
    MetricSubcodes.METRIC_DT_F_11_SKIPPED:                  [MessageStyleCode.DRIVE_TESTS,              "PRC[11]: Supply Voltage Test Skipped."],
    # ---------- Drive Tests End ----------

    MetricSubcodes.METRIC_RMM_MAP_LOADED:                   [MessageStyleCode.DEFAULT,                  "Rail Map Loaded"],
    MetricSubcodes.METRIC_RMM_MAP_LOAD_FAILED:              [MessageStyleCode.ERROR,                    "Rail Map Load Failed"],
    MetricSubcodes.METRIC_RMM_MAP_SAVED:                    [MessageStyleCode.DEFAULT,                  "Rail Map Saved"],
    MetricSubcodes.METRIC_RMM_MAP_SAVE_FAILED:              [MessageStyleCode.ERROR,                    "Rail Map Save Failed"],
    MetricSubcodes.METRIC_RMM_MAP_SORTED:                   [MessageStyleCode.DEFAULT,                  "Rail Map Sorted"],
    MetricSubcodes.METRIC_RMM_MAP_DELETE_ENTRY:             [MessageStyleCode.DEFAULT,                  "Rail Map Delete Entry"],
    MetricSubcodes.METRIC_RMM_MAP_FIND_STOPS:               [MessageStyleCode.DEFAULT,                  "Finding Rail Map Stop Positions"],
    MetricSubcodes.METRIC_RMM_MAP_LOAD_FAILED_FRM_CHK:      [MessageStyleCode.ERROR,                    "Rail Map Loaded, Format Check Failed"],

    MetricSubcodes.METRIC_CFG_FILE_SAVED:                   [MessageStyleCode.DEFAULT,                  "Config File Saved"],
    MetricSubcodes.METRIC_CFG_FILE_SAVE_FAILED:             [MessageStyleCode.ERROR,                    "Config File Save Failed"],

    MetricSubcodes.METRIC_BRK_RELEASED:                     [MessageStyleCode.BRAKE,                    "Brake Released"],
    MetricSubcodes.METRIC_BRK_ENGAGED:                      [MessageStyleCode.BRAKE,                    "Brake Engaged"],
    MetricSubcodes.METRIC_BRK_SHUTDOWN_VBUS_LOW:            [MessageStyleCode.ERROR,                    "Brake VBus Low"],
    MetricSubcodes.METRIC_BRK_SHUTDOWN_WRONG_STATE:         [MessageStyleCode.ERROR,                    "Brake Wrong State"],
    MetricSubcodes.METRIC_BRK_PENDING:                      [MessageStyleCode.BRAKE,                    "Brake State Change Pending"],

    # ---------- Calibration Start ----------
    MetricSubcodes.METRIC_CAL_MAIN_DRIVE_PREP:              [MessageStyleCode.CALIBRATION,              "Main Calibration: PREP"],
    MetricSubcodes.METRIC_CAL_MAIN_HANDING:                 [MessageStyleCode.CALIBRATION,              "Main Calibration: HANDING"],
    MetricSubcodes.METRIC_CAL_MAIN_HANDING_RESULT:          [MessageStyleCode.CALIBRATION,              "Main Calibration: Handing Result: {0:UpDir}"],
    MetricSubcodes.METRIC_CAL_MAIN_MOVING:                  [MessageStyleCode.CALIBRATION,              "Main Calibration: MOVING"],
    MetricSubcodes.METRIC_CAL_MAIN_DOWN_POS:                [MessageStyleCode.CALIBRATION,              "Main Calibration: Bottom End Position: {0:s32}"],
    MetricSubcodes.METRIC_CAL_MAIN_UP_POS:                  [MessageStyleCode.CALIBRATION,              "Main Calibration: Top End Position: {0:s32}"],
    MetricSubcodes.METRIC_CAL_MAIN_FINALISING:              [MessageStyleCode.CALIBRATION,              "Main Calibration: FINALISE"],
    MetricSubcodes.METRIC_CAL_MAIN_NEW_SLOWING_ZONE:        [MessageStyleCode.CALIBRATION,              "Main Calibration: Slowing Zone: {0:s32}, {1:s32}, {2:s32}, {3:s32}"],
    MetricSubcodes.METRIC_CAL_MAIN_NEW_CHARGE_POINT:        [MessageStyleCode.CALIBRATION,              "Main Calibration: Charge/Park Point: {0:s32}, {1:s32}, {2:s32}, {3:s32}"],
    MetricSubcodes.METRIC_CAL_MAIN_NEW_HALF_FOLD_ZONE:      [MessageStyleCode.CALIBRATION,              "Main Calibration: Half Zone: {0:s32}, {1:s32}, {2:s32}, {3:s32}"],
    MetricSubcodes.METRIC_CAL_MAIN_COMPLETED:               [MessageStyleCode.CALIBRATION,              "Main Calibration: Completed"],
    MetricSubcodes.METRIC_CAL_CHARGE_ZONE_CROSSING:         [MessageStyleCode.CALIBRATION,              "Main Calibration: Charge Point {0:LOGIC_STATE} Pos: {1:s32}"],
    MetricSubcodes.METRIC_CAL_CHARGE_ZONE_END:              [MessageStyleCode.CALIBRATION,              "Main Calibration: Charge Zone End - Pos: {0:s32} size: {1:s32}"],
    MetricSubcodes.METRIC_CAL_CHARGE_ZONE_REJECTED:         [MessageStyleCode.CALIBRATION,              "Main Calibration: Charge Rejected - size: {1:s32}"],
    MetricSubcodes.METRIC_CAL_SAFETY_EDGE:                  [MessageStyleCode.CALIBRATION,              "Main Calibration: Safety Edge - Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_MOVE_STARTED:                 [MessageStyleCode.CALIBRATION,              "Main Calibration: Move Started - Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_MOVE_ENDED:                   [MessageStyleCode.CALIBRATION,              "Main Calibration: Move Ended - Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_HANDING_ERROR:                [MessageStyleCode.ERROR,                    "Main Calibration: Handing Link Detection Error"],
    MetricSubcodes.METRIC_CAL_SLOW_ZONE_START:              [MessageStyleCode.CALIBRATION,              "Main Calibration: Slow Zone START: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SLOW_ZONE_END:                [MessageStyleCode.CALIBRATION,              "Main Calibration: Slow Zone END: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SLOW_ZONE_TOO_SHORT:          [MessageStyleCode.CALIBRATION,              "Main Calibration: Slow Zone Too Short: {0:RMM_ZONE}mm"],
    MetricSubcodes.METRIC_CAL_SLOW_ZONE_WIDTH:              [MessageStyleCode.CALIBRATION,              "Main Calibration: Slow Zone - Width: {0:RMM_ZONE}mm"],
    MetricSubcodes.METRIC_CAL_PART_UNFOLD_ZONE_START:       [MessageStyleCode.CALIBRATION,              "Main Calibration: Part Unfold Zone START: {0:s32}"],
    MetricSubcodes.METRIC_CAL_PART_UNFOLD_ZONE_END:         [MessageStyleCode.CALIBRATION,              "Main Calibration: Part Unfold Zone END: {0:s32}"],
    MetricSubcodes.METRIC_CAL_PART_UNFOLD_ZONE_SHORT:       [MessageStyleCode.CALIBRATION,              "Main Calibration: Part Unfold Zone Too Short: {0:RMM_ZONE}mm"],
    MetricSubcodes.METRIC_CAL_PART_UNFOLD_ZONE_WIDTH:       [MessageStyleCode.CALIBRATION,              "Main Calibration: Part Unfold Zone Width: {0:RMM_ZONE}mm"],

    MetricSubcodes.METRIC_CAL_SWIVEL_DRIVE_PREP:            [MessageStyleCode.CALIBRATION,              "Swivel Calibration: PREP"],
    MetricSubcodes.METRIC_CAL_SWIVEL_DRIVE_LEFT:            [MessageStyleCode.CALIBRATION,              "Swivel Calibration: LEFT"],
    MetricSubcodes.METRIC_CAL_SWIVEL_DRIVE_RIGHT:           [MessageStyleCode.CALIBRATION,              "Swivel Calibration: RIGHT"],
    MetricSubcodes.METRIC_CAL_SWIVEL_DRIVE_FINALISE:        [MessageStyleCode.CALIBRATION,              "Swivel Calibration: FINALISE"],
    MetricSubcodes.METRIC_CAL_SWIVEL_STALL_LEFT_POS:        [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Left Limit: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SWIVEL_STALL_RIGHT_POS:       [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Right Limit: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SWIVEL_CENTRE_POS:            [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Centre Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SWIVEL_CAL_INPUT_POS:         [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Calibration Vals: L:{0:s32} R:{1:s32} C:{2:s32}"],
    MetricSubcodes.METRIC_CAL_SWIVEL_DRIVE_CENTRE:          [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Drive to Centre"],
    MetricSubcodes.METRIC_CAL_SWIVEL_COMPLETED:             [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Completed"],
    MetricSubcodes.METRIC_CAL_SWIVEL_LEFT_POS_FINAL:        [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Final Left Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SWIVEL_RIGHT_POS_FINAL:       [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Final Right Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SWIVEL_CENTRE_POS_FINAL:      [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Final Centre Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_SWIVEL_RAW_OFFSET_FINAL:      [MessageStyleCode.CALIBRATION,              "Swivel Calibration: Final Raw Offset: {0:s32}"],

    MetricSubcodes.METRIC_CAL_FR_DRIVE_PREP:                [MessageStyleCode.CALIBRATION,              "Footrest Calibration: PREP"],
    MetricSubcodes.METRIC_CAL_FR_DRIVE_UNFOLD:              [MessageStyleCode.CALIBRATION,              "Footrest Calibration: UNFOLD"],
    MetricSubcodes.METRIC_CAL_FR_DRIVE_FOLD:                [MessageStyleCode.CALIBRATION,              "Footrest Calibration: FOLD"],
    MetricSubcodes.METRIC_CAL_FR_DRIVE_FINALISE:            [MessageStyleCode.CALIBRATION,              "Footrest Calibration: FINALISE"],
    MetricSubcodes.METRIC_CAL_FR_STALL_UNFOLD_POS:          [MessageStyleCode.CALIBRATION,              "Footrest Calibration: Unfold Raw Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_FR_STALL_FOLD_POS:            [MessageStyleCode.CALIBRATION,              "Footrest Calibration: Fold Raw Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_FR_COMPLETED:                 [MessageStyleCode.CALIBRATION,              "Footrest Calibration: Completed"],
    MetricSubcodes.METRIC_CAL_FR_UNFOLD_POS_FINAL:          [MessageStyleCode.CALIBRATION,              "Footrest Calibration: Final Unfold Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_FR_FOLD_POS_FINAL:            [MessageStyleCode.CALIBRATION,              "Footrest Calibration: Final Fold Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_FR_RAW_OFFSET_FINAL:          [MessageStyleCode.CALIBRATION,              "Footrest Calibration: Final Raw Offset: {0:s32}"],

    MetricSubcodes.METRIC_CAL_CF_DRIVE_PREP:                [MessageStyleCode.CALIBRATION,              "Chair Calibration: PREP"],
    MetricSubcodes.METRIC_CAL_CF_DRIVE_UNFOLD:              [MessageStyleCode.CALIBRATION,              "Chair Calibration: UNFOLD"],
    MetricSubcodes.METRIC_CAL_CF_DRIVE_FOLD:                [MessageStyleCode.CALIBRATION,              "Chair Calibration: FOLD"],
    MetricSubcodes.METRIC_CAL_CF_DRIVE_FINALISE:            [MessageStyleCode.CALIBRATION,              "Chair Calibration: FINALISE"],
    MetricSubcodes.METRIC_CAL_CF_STALL_UNFOLD_POS:          [MessageStyleCode.CALIBRATION,              "Chair Calibration: Unfold Raw Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_CF_STALL_FOLD_POS:            [MessageStyleCode.CALIBRATION,              "Chair Calibration: Fold Raw Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_CF_COMPLETED:                 [MessageStyleCode.CALIBRATION,              "Chair Calibration: Completed"],
    MetricSubcodes.METRIC_CAL_CF_UNFOLD_POS_FINAL:          [MessageStyleCode.CALIBRATION,              "Chair Calibration: Final Unfold Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_CF_FOLD_POS_FINAL:            [MessageStyleCode.CALIBRATION,              "Chair Calibration: Final Fold Pos: {0:s32}"],
    MetricSubcodes.METRIC_CAL_CF_RAW_OFFSET_FINAL:          [MessageStyleCode.CALIBRATION,              "Chair Calibration: Final Raw Offset: {0:s32}"],

    MetricSubcodes.METRIC_ROT_ENC_AS5600_MAGNET_LOW:        [MessageStyleCode.ERROR,                    "Rotary Encoder AS5600 Magnet Low: {0}"],
    MetricSubcodes.METRIC_ROT_ENC_AS5600_MAGNET_HIGH:       [MessageStyleCode.ERROR,                    "Rotary Encoder AS5600 Magnet High: {0}"],
}
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@unique
class PlaceholderStyleCode(Enum):
    """
    Enum for placeholder style codes used to display metric messages on the UIConsole.
    Inherits from Python's Enum to provide a set of unique, type-safe constants that are used as keys for the PLACEHOLDER_STYLE dictionary,
    determining the CSS styling for each placeholder type.
    """
    DEFAULT              = 0
    PASS                 = 1
    WARNING              = 2
    ERROR                = 3

    GPIO_LOW             = 10
    GPIO_HIGH            = 11

    BG_APRICOT           = 20


# Further CSS style codes for the placeholders in the metric message.
PLACEHOLDER_STYLE = {
    PlaceholderStyleCode.DEFAULT:                       f"color: {Colours.BLACK.name()};",
    PlaceholderStyleCode.PASS:                          f"color: {Colours.BLACK.name()}; background-color: {Colours.KELLY_GREEN.name()};",
    PlaceholderStyleCode.WARNING:                       f"color: {Colours.BLACK.name()}; background-color: {Colours.MARIGOLD.name()};",
    PlaceholderStyleCode.ERROR:                         f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",

    PlaceholderStyleCode.GPIO_LOW:                      f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",
    PlaceholderStyleCode.GPIO_HIGH:                     f"color: {Colours.BLACK.name()}; background-color: {Colours.KELLY_GREEN.name()};",

    PlaceholderStyleCode.BG_APRICOT:                    f"color: {Colours.BLACK.name()}; background-color: {Colours.APRICOT.name()};",
}
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def processMetrics(app_instance, msg):
    """
    Processes a Metric message received from the serial port.

    Args:
        app_instance:   App instance to emit the formatted metric message to the UIConsole.
        msg:            The metric message to handle.
    """
    # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
    if MsgMode(msg[5]) == MsgMode.OUT:
        header, metric_payload = unpackMessage(METRIC_PAYLOAD_FORMAT, msg)
        source = header[2]
        seq_num = metric_payload[2]

        # Style the timestamp.
        timestamp = formatTimestamp(seq_num)

        # Style the metric message.
        metric_message = formatMetricMessage(header, metric_payload)

        # Build string to emit to the UIConsole.
        console_string = timestamp + metric_message

        # Emit the string to the appropriate console.
        if SrcDest(source) == SrcDest.SRC_DEST_X04:
            # Emit to primary console.
            app_instance.signal_slot.primary_console_signal.emit(console_string)
        elif SrcDest(source) == SrcDest.SRC_DEST_X01:
            # Emit to secondary console.
            app_instance.signal_slot.secondary_console_signal.emit(console_string)


def styleString(style, whitespace_amount, string):
    """
    Styles a string with the given CSS style and surrounding whitespace.

    Args:
        style:              The CSS style.
        whitespace_amount:  The amount of whitespaces to add on each side.
        string:             The string to append.

    Returns:
        The formatted string with CSS styling and whitespace.
    """
    whitespace_str = CSS.WHITE_SPACE * whitespace_amount
    formatted_string = (
        f"{CSS.START_STYLE}{style}{CSS.START_STYLE_END}"
        f"{whitespace_str}{string}{whitespace_str}"
        f"{CSS.END_STYLE}"
    )
    return formatted_string


def formatTimestamp(seq_num):
    """
    Formats the string with a timestamp and sequence number using CSS styling.

    Args:
        seq_num: The sequence number of the message.

    Returns:
        The formatted timestamp string.
    """
    # Choose the timestamp style based on whether the sequence number is odd or even.
    if seq_num % 2:
        time_stamp_style = CSS_STYLE.get(MessageStyleCode.TIME_STAMP_ODD)
    else:
        time_stamp_style = CSS_STYLE.get(MessageStyleCode.TIME_STAMP_EVEN)

    # Format the current time with the chosen style.
    time_string = styleString(time_stamp_style, 0, f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}")

    # Format the sequence number with the chosen style.
    sequence_number_string = styleString(CSS_STYLE.get(MessageStyleCode.SEQUENCE_NUMBER), 0, f"{seq_num:0X}")

    # Combine the timestamp and sequence number, separated by white spaces.
    timestamp_string = time_string + CSS.WHITE_SPACE + sequence_number_string + CSS.WHITE_SPACE

    return timestamp_string


def formatMetricMessage(header, payload):
    """
    Formats the Metric message based on its subcode.

    Args:
        header:     The metric message header information.
        payload:    The metric message to format.

    Returns:
        The formatted metric message as a styled string.
    """
    subcode = payload[0]

    # Check if the metric subcode is recognised.
    if MetricSubcodes.doesValueExist(subcode):
        # Returns the member of the metric subcode based on its value.
        subcode_member = MetricSubcodes.getMember(subcode)

        # Map the style/string of the subcode member.
        subcode_member_style, subcode_member_string = METRIC_SUBCODE_MAPPER.get(subcode_member, (None, None))

        if subcode_member_style and subcode_member_string:
            # Get the CSS style for the metric subcode.
            message_CSS_style = CSS_STYLE.get(subcode_member_style)

            if message_CSS_style:
                try:
                    # Customise any placeholders within the message.
                    formatted_string = formatPlaceholders(subcode_member_string, header, payload)
                except Exception as e:
                    # Error occurred during formatting of a placeholder within the message.
                    formatted_string = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder Formatting Error: 0x{subcode:0X}, {e}")

                # Return the formatted message, either the customised placeholders or the error string.
                return styleString(message_CSS_style, 0, formatted_string)
            else:
                # Return error - CSS style not found for the message.
                return styleString(CSS_STYLE.get(MessageStyleCode.ERROR), 1, f"CSS_STYLE Error: 0x{subcode:0X}")
        else:
            # Return error - Subcode member style/string not found in the mapper.
            return styleString(CSS_STYLE.get(MessageStyleCode.ERROR), 1, f"METRIC_SUBCODE_MAPPER Error: 0x{subcode:0X}")
    else:
        # Return error - Metric subcode is not recognised.
        return styleString(CSS_STYLE.get(MessageStyleCode.ERROR), 1, f"Unknown Metric Subcode: 0x{subcode:0X}")


def formatPlaceholders(subcode_member_string, header, payload):
    """
    Scans the METRIC_SUBCODE_MAPPER string for placeholders and customises them accordingly, if no customisation is provided for the placeholder, the raw value will be used.
    If there are no placeholders, the raw string will be returned.

    Args:
        subcode_member_string:  The METRIC_SUBCODE_MAPPER string to scan for placeholders and format.
        header:                 The metric message header information.
        payload:                The metric message payload to alter for the string.

    Returns:
        The customised placeholder string.
    """
    uuid = payload[3]
    source = header[2]

    # Convert tuple to list for easier manipulation.
    placeholders = list(payload[5:])  # The payload data we are interested in starts from index 5.

    # Find all placeholders in the METRIC_SUBCODE_MAPPER string, including special cases like {UUID} with no numbers.
    placeholder_pattern = re.compile(r'{(\d+)(?::([^}]+))?}|{([a-zA-Z]+[0-9]*)}') # Regex has three capturing groups - NumberOnly, NumberAndFormat, SpecialFormat.
    num_matching_placeholders = placeholder_pattern.findall(subcode_member_string)

    # Iterate through each placeholder match and customise them as needed.
    for index, format, special_format in num_matching_placeholders:
        # Get the exact placeholder string (e.g. {0}, {0:CHAR4}, {UUID}) as it appears in the curly braces {}, so it can be replaced in the string or used in error messages.
        placeholder = f"{{{special_format}}}" if special_format else f"{{{index}:{format}}}" if format else f"{{{index}}}"
        try:
            if special_format:
                # Handle special formats that do not follow the standard {0:xyz}.
                if special_format == 'UUID':
                    uuid = UUID(uuid & 0xFFFFFF00).name
                    if UUID.doesNameExist(uuid):
                        styled_placeholder = f"{uuid}"
                    else:
                        styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Special Placeholder UUID Unknown UUID: {uuid}")

                elif special_format == 'UUID1':
                    uuid = UUID(uuid & 0xFFFFFF00).name
                    if UUID.doesNameExist(uuid):
                        styled_placeholder = f"{uuid}"
                    else:
                        styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Special Placeholder UUID1 Unknown UUID: {uuid}")
                else:
                    # Unknown special format.
                    styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Special Placeholder Unknown Format: {special_format}")
            else:
                data = placeholders[int(index)] # Get the data value for this placeholder index from the payload.

                if not format:
                    # No format identifier present, so just print the raw data value as a string.
                    styled_placeholder = str(data)
                else:
                    if format == 'BreakReasons':
                        if BreakReasons.doesValueExist(data):
                            styled_placeholder = f"{BreakReasons(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'CallSource':
                        if CallSource.doesValueExist(data):
                            styled_placeholder = f"{CallSource(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'CallType':
                        if CallType.doesValueExist(data):
                            styled_placeholder = f"{CallType(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'CHAR4':
                        # Convert the 4-byte integer to a string, removing any null terminators.
                        try:
                            styled_placeholder = data.to_bytes(4, byteorder='little').decode('utf-8').replace('\x00', '')
                        except UnicodeDecodeError:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'DemandStates':
                        if DemandStates.doesValueExist(data):
                            styled_placeholder = f"{DemandStates(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'DriveControlDir':
                        if DriveControlDir.doesValueExist(data):
                            styled_placeholder = f"{DriveControlDir(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'DriveSpeedProfiles':
                        if DriveSpeedProfiles.doesValueExist(data):
                            styled_placeholder = f"{DriveSpeedProfiles(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'DriveState':
                        if DriveState.doesValueExist(data):
                            styled_placeholder = f"{DriveState(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'DriveTest':
                        if DriveTest.doesValueExist(data):
                            styled_placeholder = f"{DriveTest(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'ECodes':
                        if ECodes.doesValueExist(data):
                            styled_placeholder = f"{ECodes(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'ErrorType':
                        if ErrorType.doesValueExist(data):
                            styled_placeholder = f"{ErrorType(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'GPIO_INPUTS':
                        if SrcDest(source) == SrcDest.SRC_DEST_X04 and InputsX04.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{InputsX04(data).name}")
                        elif SrcDest(source) == SrcDest.SRC_DEST_X01 and InputsX01.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{InputsX01(data).name}")
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'GPIO_OUTPUTS':
                        if SrcDest(source) == SrcDest.SRC_DEST_X04 and OutputsX04.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{OutputsX04(data).name}")
                        elif SrcDest(source) == SrcDest.SRC_DEST_X01 and OutputsX01.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{OutputsX01(data).name}")
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'LOGIC_STATE':
                        if LogicState.doesValueExist(data):
                            if data == LogicState.LOGIC_0.value:
                                styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.GPIO_LOW], 2, f"0")
                            else:
                                styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.GPIO_HIGH], 2, f"1")
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'MovingDriveState':
                        if MovingDriveState.doesValueExist(data):
                            styled_placeholder = f"{MovingDriveState(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'OperationalMode':
                        if OperationalMode.doesValueExist(data):
                            styled_placeholder = f"{CSS.START_STYLE}{PLACEHOLDER_STYLE[PlaceholderStyleCode.PASS]}{CSS.START_STYLE_END}{OperationalMode(data).name}{CSS.END_STYLE}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'PoweredOff':
                        ecu_time_off = int(data)

                        # Calculate days
                        days = ecu_time_off // (24 * 3600)
                        remaining_seconds_after_days = ecu_time_off % (24 * 3600)

                        # Calculate hours
                        hours = remaining_seconds_after_days // 3600
                        remaining_seconds_after_hours = remaining_seconds_after_days % 3600

                        # Calculate minutes
                        minutes = remaining_seconds_after_hours // 60

                        # Calculate seconds
                        seconds = remaining_seconds_after_hours % 60

                        styled_placeholder = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

                    elif format == 'RMM_ZONE':
                        if isinstance(data, int):
                            # Convert to signed integer first.
                            signed_data = int.from_bytes(data.to_bytes(4, byteorder='little', signed=False), byteorder='little', signed=True)

                            # Convert to zone length in mm.
                            data = (signed_data * 127) / 11.15126765

                            # Format the data to two decimal places.
                            styled_placeholder = f"{data:.2f}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'RMUStates':
                        if RMUStates.doesValueExist(data):
                            styled_placeholder = f"{RMUStates(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 's32':
                        # Convert data to signed integer if format is s32.
                        data = int.from_bytes(data.to_bytes(4, byteorder='little', signed=False), byteorder='little', signed=True)
                        styled_placeholder = str(data)

                    elif format == 'SUBCODE':
                        fidd = data
                        subcode = (fidd >> 16) & 0xFF
                        styled_placeholder = f"{subcode}"

                    elif format == 'SystemState':
                        if SystemState.doesValueExist(data):
                            if data == SystemState.NORMAL.value:
                                styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.PASS], 0, f"{SystemState(data).name}")
                            elif data == SystemState.FAULTED.value:
                                styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 0, f"{SystemState(data).name}")
                            else:
                                styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.WARNING], 0, f"{SystemState(data).name}")
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'UpDir':
                        if UpDirection.doesValueExist(data):
                            styled_placeholder = f"{UpDirection(data).name}"
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'Volts':
                        # Convert data from millivolts to volts with two decimal places.
                        styled_placeholder = f"{data / 1000:.2f}"

                    elif format == 'x8':
                        # Convert data to hexadecimal string with 8 digits.
                        styled_placeholder = f"{int(data):08X}"

                    else:
                        # Unknown format for this placeholder.
                        styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Unknown Format: {format}")

        except Exception as e:
            # Catch any unexpected errors for this placeholder.
            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {e}")

        # Replace the placeholder in the string with the newly styled value.
        subcode_member_string = subcode_member_string.replace(placeholder, styled_placeholder)

    return subcode_member_string # If there are no matches to the regex group, the original string is returned unchanged.