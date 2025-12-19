# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class ECodes(EnumUtils, Enum):
    """
    Enum class containing all the E-codes.
    """
    NO_ERROR                                    = 0x0000

    NO_CHARGE_DETECTED                          = 0x0505

    # Battery issues
    BATTERY_LOW                                 = 0x1005
    BATTERY_LOW_CALL_REJECTED                   = 0x1010
    BATTERY_ULTRA_LOW                           = 0x1015
    BATTERY_DIFFERENTIAL_TOO_GREAT              = 0x1020
    BATTERY_VOLTAGE_TOO_HIGH                    = 0x1025
    COIN_CELL_DEPLETED                          = 0x1030

    # Carriage ECU Detected Issues
    DUAL_CALL_CHAIR_ARM                         = 0x2005
    DUAL_CALL_REMOTE_CONTROL                    = 0x2010
    FOOTREST_MOTOR_MISSING                      = 0x2015
    STUCK_CALL                                  = 0x2020
    CALL_REJECTED                               = 0x2025
    USB_COMMS_FAULT                             = 0x2030
    MAIN_FUSE_BLOWN                             = 0x2035
    MAIN_DRIVE_MOTOR_MISSING                    = 0x2040
    BRAKE_OPEN_CIRCUIT                          = 0x2045
    BRAKE_FAILED_TO_ENGAGE                      = 0x2050
    BRAKE_FAILED_TO_DISENGAGE                   = 0x2055
    FOOTREST_INSTANTANEOUS_STALL                = 0x2060
    FOOTREST_INSTANTANEOUS_STALL_REPEATEDLY     = 0x2065
    FOOTREST_SUSTAINED_STALL                    = 0x2070
    FOOTREST_SUSTAINED_STALL_REPEATEDLY         = 0x2075
    FOOTREST_ENCODER_FAULT                      = 0x2080
    FOOTREST_OPERATED_DIRECTION_WRONG           = 0x2085
    FOOTREST_UNDERSPEED                         = 0x2090
    RMU_FAULT                                   = 0x2095
    RMU_SHUTDOWN                                = 0x2100
    UNEXPECTED_CHARGE                           = 0x2105
    CAN_COMMS_FAULT                             = 0x2110
    MAIN_DRIVE_INSTANTANEOUS_STALL              = 0x2115
    MAIN_DRIVE_INSTANTANEOUS_STALL_REPEATEDLY   = 0x2120
    MAIN_DRIVE_SUSTAINED_STALL                  = 0x2125
    MAIN_DRIVE_SUSTAINED_STALL_REPEATEDLY       = 0x2130
    MAIN_DRIVE_CURRENT_LOW_TRAVELLING_UP        = 0x2135
    MAIN_DRIVE_OPERATED_DIRECTION_WRONG         = 0x2140
    MAIN_DRIVE_OVERSPEED                        = 0x2145
    MAIN_DRIVE_UNDERSPEED                       = 0x2150
    MAIN_DRIVE_ENCODER_FAULT                    = 0x2155
    MAIN_DRIVE_RELAY_ACTIVE_FAULT               = 0x2160
    OPTION_DRIVE_RELAY_ACTIVE_FAULT             = 0x2165
    AUDIO_PLAYBACK_ERROR                        = 0x2170
    SD_CARD_MISSING                             = 0x2175
    SD_CARD_FILE_MISSING                        = 0x2180
    SD_CARD_NOT_MOUNTED                         = 0x2185
    SD_CARD_FILE_FAILURE                        = 0x2190
    IMU_LOSS_OF_COMMS                           = 0x2195
    IMU_IMPLAUSIBLE_DATA                        = 0x2200
    CONFIGURATION_FAULT                         = 0x2205
    HANDING_NOT_SET                             = 0x2210
    HEAVY_LOAD                                  = 0x2215
    MAIN_DRIVE_NOT_MOVING                       = 0x2220
    MAIN_DRIVE_NOT_FOLLOWING_PROFILE            = 0x2225
    MAIN_DRIVE_TIMEOUT                          = 0x2230
    FOOTREST_DRIVE_NOT_MOVING                   = 0x2235
    FOOTREST_NOT_FOLLOWING_PROFILE              = 0x2240
    FOOTREST_DRIVE_TIMEOUT                      = 0x2245
    REDUCED_SPEED                               = 0x2250

    # Carriage ECU Failures
    MAIN_POWER_RELAY_FAULT                      = 0x2505
    OPTION_RELAY_FAULT                          = 0x2510
    MAIN_DRIVE_ECU_FAULT                        = 0x2515
    FOOTREST_DRIVE_ECU_FAULT                    = 0x2520
    CARRIAGE_SOFTWARE_RESET_DETECTED            = 0x2525
    CARRIAGE_ADC_FAILURE                        = 0x2530
    SUPPLY_VOLTAGE_IMPLAUSIBLE_FAULT            = 0x2535
    DIRECTIONAL_CHAIN_ENERGISATION_FAULT        = 0x2540

    # Chair ECU Failures
    SEAT_RAISED_AND_LOADED                      = 0x3005
    OPTION_RELAY_FUSE_FAULT                     = 0x3010
    SWIVEL_MOTOR_MISSING                        = 0x3015
    CHAIR_FOLD_MOTOR_MISSING                    = 0x3020
    SWIVEL_ENCODER_FAULT                        = 0x3025
    SWIVEL_OPERATED_DIRECTION_WRONG             = 0x3030
    CHAIR_FOLD_ENCODER_FAULT                    = 0x3035
    CHAIR_FOLD_OPERATED_DIRECTION_WRONG         = 0x3040
    CHAIR_FOLD_INSTANTANEOUS_STALL              = 0x3045
    CHAIR_FOLD_INSTANTANEOUS_STALL_REPEATEDLY   = 0x3050
    CHAIR_FOLD_SUSTAINED_STALL                  = 0x3055
    CHAIR_FOLD_SUSTAINED_STALL_REPEATEDLY       = 0x3060
    CHAIR_FOLD_UNDERSPEED                       = 0x3065
    SWIVEL_INSTANTANEOUS_STALL                  = 0x3070
    SWIVEL_INSTANTANEOUS_STALL_REPEATEDLY       = 0x3075
    SWIVEL_SUSTAINED_STALL                      = 0x3080
    SWIVEL_SUSTAINED_STALL_REPEATEDLY           = 0x3085
    SWIVEL_UNDERSPEED                           = 0x3090
    SWIVEL_DRIVE_NOT_MOVING                     = 0x3095
    SWIVEL_NOT_FOLLOWING_PROFILE                = 0x3100
    SWIVEL_DRIVE_TIMEOUT                        = 0x3105
    CHAIR_FOLD_DRIVE_NOT_MOVING                 = 0x3110
    CHAIR_FOLD_NOT_FOLLOWING_PROFILE            = 0x3115
    CHAIR_FOLD_DRIVE_TIMEOUT                    = 0x3120

    # Chair ECU Failures
    SWIVEL_DRIVE_ECU_FAULT                      = 0x3505
    CHAIR_FOLD_ECU_FAULT                        = 0x3510
    CHAIR_SOFTWARE_RESET_DETECTED               = 0x3515
    CHAIR_ADC_FAILURE                           = 0x3520

    # ECU Generic
    ECU_FAILURE                                 = 0x4005
    SOFTWARE_VERSION_FAULT                      = 0x4010
    SYNC_LOSS                                   = 0x4015
    SYNC_PUSH_MESSAGE_FAULT                     = 0x4020
    FLASH_FAILURE                               = 0x4025
    INCONSISTENT_DRIVE_STATE                    = 0x4030
    ECU_IO_FAILURE                              = 0x4040
    COMMUNICATION_FAULT                         = 0x4045
    CHAIR_TYPE_FAULT                            = 0x4050
    SAFETY_CHAIN_VOLTAGE_FAULT                  = 0x4055
    WATCHDOG_X01_FAULT                          = 0x4060
    WATCHDOG_X04_FAULT                          = 0x4065
    UNIDENTIFIED_FAULT                          = 0x4070

    # Safety Devices
    FINAL_LIMIT_SAFETY                          = 0x9005
    BISTABLE_SAFETY                             = 0x9010
    SWIVEL_CENTRE_SAFETY                        = 0x9015
    MAIN_DRIVE_SAFETY                           = 0x9020
    RIGHT_SKATE_SAFETY                          = 0x9025
    RIGHT_CLUSTER_SAFETY                        = 0x9030
    RIGHT_CARRIAGE_SAFETY                       = 0x9035
    RIGHT_FOOTREST_SAFETY                       = 0x9040
    LEFT_SKATE_SAFETY                           = 0x9045
    LEFT_CLUSTER_SAFETY                         = 0x9050
    LEFT_CARRIAGE_SAFETY                        = 0x9055
    LEFT_FOOTREST_SAFETY                        = 0x9060
    BOTTOM_FOOTREST_SAFETY                      = 0x9065
    ULTIMATE_NOT_CONTIGUOUS                     = 0x9070
    BOTH_CHAINS_ON                              = 0x9075
    BISTABLE_FAILED_TEST                        = 0x9080
    BISTABLE_REQUEST_SYNC_FAIL                  = 0x9085

    # Hazard Mitigation Device
    KEY_SWITCH                                  = 0x9105
    HANDING_BLOCK                               = 0x9110
    SEATBELT                                    = 0x9120
    EMERGENCY_OVERRIDE                          = 0x9125
    SEAT_LOAD_SENSOR                            = 0x9130
    DOWNSIDE_ARM                                = 0x9135
    DRIVE_NOT_CALIBRATED                        = 0x9140
    SEATBELT_BLOCKS_CHAIR_FOLD                  = 0x9145