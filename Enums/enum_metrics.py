# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class MetricSubcodes(EnumUtils, Enum):
    """
    Enum class to define the metric subcodes.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants.
    The enum values are used as indices for the METRIC_SUBCODE_MAPPER dictionary.
    """
    METRIC_INVALID                          = 0x0000

    METRIC_POWER_UP                         = 0x0010
    METRIC_EXCEPTION                        = 0x0015
    METRIC_GENERIC_OUTPUT                   = 0x0016
    METRIC_SEPARATOR                        = 0x0017
    METRIC_TASK_OVERRUN_DUE_FS              = 0x0019
    METRIC_RESTART_FILENAME                 = 0x001B
    METRIC_TIME_POWERED_OFF                 = 0x001C

    METRIC_INPUT_STATE_CHANGE               = 0x0020
    METRIC_OUTPUT_STATE_CHANGE              = 0x0021
    METRIC_INPUT_DEB_FAULT                  = 0x0022
    METRIC_OUTPUT_DEB_FAULT                 = 0x0023

    METRIC_SYS_OPERATIONAL_STATE            = 0x0030
    METRIC_HARDWARE_LAYER_INIT              = 0x0033
    METRIC_SERVICE_LAYER_INIT               = 0x0034
    METRIC_CONTROL_LAYER_INIT               = 0x0035
    METRIC_TASK_SETUP_COMPLETE              = 0x0036
    METRIC_COMPONENT_FAULT                  = 0x0037
    METRIC_OPERATIONAL_MODE                 = 0x0038

    METRIC_SD_CARD_PRESENT                  = 0x003A
    METRIC_SD_CARD_NOT_PRESENT              = 0x003B
    METRIC_SD_CARD_MOUNT_OK                 = 0x003C
    METRIC_SD_CARD_MOUNT_FAILED             = 0x003D

    METRIC_DRIVE_STATE                      = 0x0040
    METRIC_DRIVE_PROFILER_SPEED_CHG         = 0x0042
    METRIC_DRIVE_MAIN_RECOVERED_POS         = 0x0043
    METRIC_DRIVE_MAIN_START_POS             = 0x0044
    METRIC_DRIVE_MAIN_TARGET_POS            = 0x0045
    METRIC_DRIVE_MAIN_MAX_SPEED             = 0x0046
    METRIC_DRIVE_MAIN_HB_BRIDGE_USED        = 0x0047
    METRIC_DRIVE_MAIN_NO_TARGET_POS         = 0x0048
    METRIC_DRIVE_MAIN_DEMAND_REMOVED        = 0x0049
    METRIC_DRIVE_MAIN_SAFETY_STOP           = 0x004A

    METRIC_CALL_PLACED                      = 0x0050
    METRIC_CALL_REMOVED                     = 0x0051
    METRIC_DEMAND_STATE_CHANGE              = 0x0052
    METRIC_DEMAND_BREAK_REASON              = 0x0053

    METRIC_FILE_LOAD_ERROR                  = 0x0060

    # ---------- Drive Tests ----------
    METRIC_DT_STARTED_PRE                   = 0x0100
    METRIC_DT_STARTED_POST                  = 0x0101
    METRIC_DT_STOPPED                       = 0x0102
    METRIC_DT_ABORTED                       = 0x0103
    METRIC_DT_PASSED                        = 0x0104
    METRIC_DT_FAILED                        = 0x0105
    METRIC_DT_STARTED                       = 0x0107
    METRIC_DT_TIMEOUT                       = 0x0108

    METRIC_DT_F_01_SUPL_NO_VOLTS            = 0x0110
    METRIC_DT_F_01_SUPL_TOO_LOW             = 0x0111
    METRIC_DT_F_01_SUPL_TOO_HIGH            = 0x0112
    METRIC_DT_P_01_SUPL_IN_RANGE            = 0x0113

    METRIC_DT_P_02_L_DRV_V_LOW              = 0x0120
    METRIC_DT_F_02_L_DRV_V_MID              = 0x0121
    METRIC_DT_F_02_L_DRV_V_HIGH             = 0x0122

    METRIC_DT_P_02_R_DRV_V_LOW              = 0x0123
    METRIC_DT_F_02_R_DRV_V_MID              = 0x0124
    METRIC_DT_F_02_R_DRV_V_HIGH             = 0x0125

    METRIC_DT_P_03_L_DRV_V_MID_S1           = 0x0130
    METRIC_DT_F_03_L_BOT_FET_SHORT_S1       = 0x0131
    METRIC_DT_F_03_L_DRV_V_HIGH_S1          = 0x0132

    METRIC_DT_P_03_R_DRV_V_MID_S2           = 0x0133
    METRIC_DT_F_03_R_BOT_FET_SHORT_S2       = 0x0134
    METRIC_DT_F_03_R_DRV_V_HIGH_S2          = 0x0135

    METRIC_DT_P_03_L_DRV_V_LOW_S4           = 0x0136
    METRIC_DT_F_03_L_BOT_FET_OPEN_S4        = 0x0137
    METRIC_DT_F_03_L_DRV_V_HIGH_S4          = 0x0138

    METRIC_DT_P_03_R_DRV_V_LOW_S5           = 0x0139
    METRIC_DT_F_03_R_BOT_FET_OPEN_S5        = 0x013A
    METRIC_DT_F_03_R_DRV_V_HIGH_S5          = 0x013B

    METRIC_DT_P_03_MOTOR_DETECTED           = 0x013C
    METRIC_DT_F_03_MOTOR_NOT_DET            = 0x013D

    METRIC_DT_P_04_SKIP_LEFT_CHECK          = 0x0140
    METRIC_DT_P_04_SKIP_RIGHT_CHECK         = 0x0141

    METRIC_DT_P_04_L_DRV_V_HIGH             = 0x0142
    METRIC_DT_F_04_L_DRV_V_LOW              = 0x0143
    METRIC_DT_F_04_L_DRV_V_MID_RAIL         = 0x0144

    METRIC_DT_P_04_R_DRV_V_HIGH             = 0x0145
    METRIC_DT_F_04_R_DRV_V_LOW              = 0x0146
    METRIC_DT_F_04_R_DRV_V_MID_RAIL         = 0x0147

    METRIC_DT_P_11_SUPL_NO_VOLTS            = 0x01A0
    METRIC_DT_F_11_SUPL_V_MID_RAIL          = 0x01A1
    METRIC_DT_F_11_SUPL_V_HIGH              = 0x01A2
    METRIC_DT_F_11_SKIPPED                  = 0x01A3
    # ---------- Drive Tests End ----------

    METRIC_RMM_MAP_LOADED                   = 0x0200
    METRIC_RMM_MAP_LOAD_FAILED              = 0x0201
    METRIC_RMM_MAP_SAVED                    = 0x0202
    METRIC_RMM_MAP_SAVE_FAILED              = 0x0203
    METRIC_RMM_MAP_SORTED                   = 0x0204
    METRIC_RMM_MAP_DELETE_ENTRY             = 0x0205
    METRIC_RMM_MAP_FIND_STOPS               = 0x0207
    METRIC_RMM_MAP_LOAD_FAILED_FRM_CHK      = 0x0209

    METRIC_CFG_FILE_SAVED                   = 0x0222
    METRIC_CFG_FILE_SAVE_FAILED             = 0x0223

    METRIC_BRK_RELEASED                     = 0x0240
    METRIC_BRK_ENGAGED                      = 0x0241
    METRIC_BRK_SHUTDOWN_VBUS_LOW            = 0x0242
    METRIC_BRK_SHUTDOWN_WRONG_STATE         = 0x0244
    METRIC_BRK_PENDING                      = 0x0245

    # ---------- Calibration ----------
    METRIC_CAL_MAIN_DRIVE_PREP              = 0x0301
    METRIC_CAL_MAIN_HANDING                 = 0x0302
    METRIC_CAL_MAIN_HANDING_RESULT          = 0x0303
    METRIC_CAL_MAIN_MOVING                  = 0x0304
    METRIC_CAL_MAIN_DOWN_POS                = 0x0305
    METRIC_CAL_MAIN_UP_POS                  = 0x0308
    METRIC_CAL_MAIN_FINALISING              = 0x0309
    METRIC_CAL_MAIN_NEW_SLOWING_ZONE        = 0x030D
    METRIC_CAL_MAIN_NEW_CHARGE_POINT        = 0x030E
    METRIC_CAL_MAIN_NEW_HALF_FOLD_ZONE      = 0x030F
    METRIC_CAL_MAIN_COMPLETED               = 0x0316
    METRIC_CAL_CHARGE_ZONE_CROSSING         = 0x0317
    METRIC_CAL_CHARGE_ZONE_END              = 0x0318
    METRIC_CAL_CHARGE_ZONE_REJECTED         = 0x0319
    METRIC_CAL_SAFETY_EDGE                  = 0x031A
    METRIC_CAL_MOVE_STARTED                 = 0x031B
    METRIC_CAL_MOVE_ENDED                   = 0x031C
    METRIC_CAL_HANDING_ERROR                = 0x031D
    METRIC_CAL_SLOW_ZONE_START              = 0x0321
    METRIC_CAL_SLOW_ZONE_END                = 0x0322
    METRIC_CAL_SLOW_ZONE_TOO_SHORT          = 0x0323
    METRIC_CAL_SLOW_ZONE_WIDTH              = 0x0326
    METRIC_CAL_PART_UNFOLD_ZONE_START       = 0x0330
    METRIC_CAL_PART_UNFOLD_ZONE_END         = 0x0331
    METRIC_CAL_PART_UNFOLD_ZONE_SHORT       = 0x0332
    METRIC_CAL_PART_UNFOLD_ZONE_WIDTH       = 0x0335

    METRIC_CAL_SWIVEL_DRIVE_PREP            = 0x0350
    METRIC_CAL_SWIVEL_DRIVE_LEFT            = 0x0351
    METRIC_CAL_SWIVEL_DRIVE_RIGHT           = 0x0352
    METRIC_CAL_SWIVEL_DRIVE_FINALISE        = 0x0353
    METRIC_CAL_SWIVEL_STALL_LEFT_POS        = 0x0354
    METRIC_CAL_SWIVEL_STALL_RIGHT_POS       = 0x0355
    METRIC_CAL_SWIVEL_CENTRE_POS            = 0x0356
    METRIC_CAL_SWIVEL_CAL_INPUT_POS         = 0x0357
    METRIC_CAL_SWIVEL_DRIVE_CENTRE          = 0x0358
    METRIC_CAL_SWIVEL_COMPLETED             = 0x0359
    METRIC_CAL_SWIVEL_LEFT_POS_FINAL        = 0x035A
    METRIC_CAL_SWIVEL_RIGHT_POS_FINAL       = 0x035B
    METRIC_CAL_SWIVEL_CENTRE_POS_FINAL      = 0x035C
    METRIC_CAL_SWIVEL_RAW_OFFSET_FINAL      = 0x035D

    METRIC_CAL_FR_DRIVE_PREP                = 0x0370
    METRIC_CAL_FR_DRIVE_UNFOLD              = 0x0371
    METRIC_CAL_FR_DRIVE_FOLD                = 0x0372
    METRIC_CAL_FR_DRIVE_FINALISE            = 0x0373
    METRIC_CAL_FR_STALL_UNFOLD_POS          = 0x0374
    METRIC_CAL_FR_STALL_FOLD_POS            = 0x0375
    METRIC_CAL_FR_COMPLETED                 = 0x0376
    METRIC_CAL_FR_UNFOLD_POS_FINAL          = 0x0377
    METRIC_CAL_FR_FOLD_POS_FINAL            = 0x0378
    METRIC_CAL_FR_RAW_OFFSET_FINAL          = 0x0379

    METRIC_CAL_CF_DRIVE_PREP                = 0x0390
    METRIC_CAL_CF_DRIVE_UNFOLD              = 0x0391
    METRIC_CAL_CF_DRIVE_FOLD                = 0x0392
    METRIC_CAL_CF_DRIVE_FINALISE            = 0x0393
    METRIC_CAL_CF_STALL_UNFOLD_POS          = 0x0394
    METRIC_CAL_CF_STALL_FOLD_POS            = 0x0395
    METRIC_CAL_CF_COMPLETED                 = 0x0396
    METRIC_CAL_CF_UNFOLD_POS_FINAL          = 0x0397
    METRIC_CAL_CF_FOLD_POS_FINAL            = 0x0398
    METRIC_CAL_CF_RAW_OFFSET_FINAL          = 0x0399

    METRIC_ROT_ENC_AS5600_MAGNET_LOW        = 0x0411
    METRIC_ROT_ENC_AS5600_MAGNET_HIGH       = 0x0412