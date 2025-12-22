# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class UUID(EnumUtils, Enum):
    """
    Enum class containing all the UUID's.
    """
    INVALID_ID                              = 0
    TEST_COMPONENT                          = 1

    # Threads
    TASK_SUPERVISOR                         = 0x1010_0000
    TASK_COMMS                              = 0x1020_0000
    TASK_OTA                                = 0x1030_0000
    TASK_SLOW_GENERAL                       = 0x1040_0000
    TASK_FAST_GENERAL                       = 0x1050_0000
    TASK_FOOTREST                           = 0x1060_0000
    TASK_MAIN_DRIVE                         = 0x1070_0000
    TASK_SWIVEL                             = 0x1080_0000
    TASK_CHAIR_FOLD                         = 0x1090_0000
    TASK_AUDIO_STREAM                       = 0x10A0_0000
    TASK_SD_CARD_DRIVER                     = 0x10B0_0000
    TASK_FILE_MANAGER                       = 0x10C0_0000
    TASK_FLC_HOST                           = 0x10D0_0000
    TASK_UNASSIGNED_E                       = 0x10E0_0000
    TASK_UNASSIGNED_F                       = 0x10F0_0000

    # Layers
    HARDWARE_LAYER                          = 0x2010_0000
    SERVICE_LAYER                           = 0x2020_0000
    CONTROL_LAYER                           = 0x2030_0000

    # Components
    # TODO-Phase_6 (Mantis 2497) this is an initial list of component IDs. This includes main and shadow versions.
    # Take out any that aren't required (e.g. ones that don't have shadow versions) and add in any that have
    # been missed. Add multiple instances as well.

    # --- Control ---
    DEMAND_PROCESSOR                        = 0x3101_0000
    ECODE_HANDLER                           = 0x3102_0000
    FAULT_LOG_CONTROL                       = 0x3103_0000
    OPERATIONAL_MODE_CONTROL                = 0x3104_0000
    SOFTWARE_UPDATE_MANAGER                 = 0x3105_0000
    SYSTEM_EVENT_RECORDER                   = 0x3106_0000

    # drive state machine
    DRIVE_STATE_MACHINE_MAIN_DRIVE          = 0x3110_0000
    DRIVE_STATE_MACHINE_FOOTREST            = 0x3111_0000
    DRIVE_STATE_MACHINE_CHAIR_FOLD          = 0x3112_0000
    DRIVE_STATE_MACHINE_SWIVEL              = 0x3113_0000
    DRIVE_STATE_MACHINE_HINGE               = 0x3114_0000


    # --- Service ---
    AUDIBLE_ALERTS                          = 0x3201_0000
    BATTERY_MONITOR                         = 0x3202_0000
    BRAKE_CONTROL                           = 0x3203_0000
    CALL_DETECTION                          = 0x3204_0000
    DIAGNOSTICS_MODULE                      = 0x3205_0000
    CHARGE_MONITOR                          = 0x3206_0000
    DATA_SYNC                               = 0x3207_0000
    FILE_MANAGER                            = 0x3208_0000
    MESSAGE_EXCHANGE                        = 0x3209_0000
    RMU                                     = 0x320A_0000
    STORED_CONFIGURATION                    = 0x320B_0000
    SYSTEM_MONITOR                          = 0x320C_0000
    VISIBLE_INDICATIONS                     = 0x320D_0000
    RMM_MANAGER                             = 0x320E_0000
    RMM_CONFIG                              = 0x320F_0000
    DRIVE_RELAY_CONTROL                     = 0x3210_0000
    BISTABLE_MONITOR                        = 0x3211_0000
    #----------------------------------------------------------------------
    DRIVE_TESTS_MAIN_DRIVE                  = 0x3220_0000
    DRIVE_TESTS_FOOTREST                    = 0x3221_0000
    DRIVE_TESTS_CHAIR_FOLD                  = 0x3222_0000
    DRIVE_TESTS_SWIVEL                      = 0x3223_0000
    DRIVE_TESTS_HINGE                       = 0x3224_0000
    #----------------------------------------------------------------------
    DRIVE_POWER_MONITOR_MAIN_DRIVE          = 0x3230_0000
    DRIVE_POWER_MONITOR_FOOTREST            = 0x3231_0000
    DRIVE_POWER_MONITOR_CHAIR_FOLD          = 0x3232_0000
    DRIVE_POWER_MONITOR_SWIVEL              = 0x3233_0000
    DRIVE_POWER_MONITOR_HINGE               = 0x3234_0000
    #----------------------------------------------------------------------
    CALIBRATION_MAIN_DRIVE                  = 0x3240_0000
    CALIBRATION_FOOTREST                    = 0x3241_0000
    CALIBRATION_CHAIR_FOLD                  = 0x3242_0000
    CALIBRATION_SWIVEL                      = 0x3243_0000
    CALIBRATION_HINGE                       = 0x3244_0000
    #----------------------------------------------------------------------
    DRIVE_POSITION_MAIN_DRIVE               = 0x3250_0000
    DRIVE_POSITION_FOOTREST                 = 0x3251_0000
    DRIVE_POSITION_CHAIR_FOLD               = 0x3252_0000
    DRIVE_POSITION_SWIVEL                   = 0x3253_0000
    DRIVE_POSITION_HINGE                    = 0x3254_0000
    #----------------------------------------------------------------------
    DRIVE_CONTROL_MAIN_DRIVE                = 0x3260_0000
    DRIVE_CONTROL_FOOTREST                  = 0x3261_0000
    DRIVE_CONTROL_CHAIR_FOLD                = 0x3262_0000
    DRIVE_CONTROL_SWIVEL                    = 0x3263_0000
    DRIVE_CONTROL_HINGE                     = 0x3264_0000
    #----------------------------------------------------------------------

    # --- Hardware ---
    ADC_MONITOR                             = 0x3301_0000
    AUDIO_PLAYER                            = 0x3302_0000
    BATTERY_BACKED_RAM                      = 0x3303_0000
    BINARY_MESSAGE_PARSER                   = 0x3304_0000
    CAN_HANDLER                             = 0x3305_0000
    DIRECTIONAL_CONTROL_LIGHTING            = 0x3306_0000
    DUAL_HEX_DISPLAY                        = 0x3307_0000
    FLASH_MANAGER                           = 0x3308_0000
    HARDWARE_TEST                           = 0x3309_0000
    HWSOFTWARE_ERROR_HANDLER                = 0x3309_0100
    I2C                                     = 0x330A_0000
    I2C_1                                   = 0x330A_0100
    I2C_2                                   = 0x330A_0200
    I2C_3                                   = 0x330A_0300
    I2C_4                                   = 0x330A_0400
    I2S                                     = 0x330B_0000
    IMU                                     = 0x330C_0000
    IO_MONITOR                              = 0x330D_0000
    LINEAR_ENCODER                          = 0x330E_0000
    PUDDLE_LIGHTING                         = 0x330F_0000

    REAL_TIME_CLOCK                         = 0x3311_0000
    ROTARY_ENCODER                          = 0x3312_0000
    ROTARY_ENCODER_FOOTREST                 = 0x3312_0100
    ROTARY_ENCODER_SWIVEL                   = 0x3312_0200
    ROTARY_ENCODER_CHAIR_FOLD               = 0x3312_0300
    SD_CARD_DRIVER                          = 0x3313_0000
    SPI                                     = 0x3314_0000
    SPI_1                                   = 0x3314_0100
    SPI_2                                   = 0x3314_0200
    SPI_3                                   = 0x3314_0300
    SPI_4                                   = 0x3314_0400
    SYSTEM_TICK                             = 0x3315_0000
    USB_HANDLER                             = 0x3316_0000
    WATCHDOG                                = 0x3317_0000
    EMC_HANDLER                             = 0x3318_0000
    PWM_INDEPENDENT_LED_BLUE                = 0x3319_0000
    PWM_INDEPENDENT_LED_GREEN               = 0x3319_0100
    PWM_INDEPENDENT_LED_RED                 = 0x3319_0200
    PWM_INDEPENDENT_PUDDLE_CHAIR            = 0x3319_0300
    PWM_INDEPENDENT_PUDDLE_CARRIAGE         = 0x3319_0400
    PWM_COMPLEMENTARY_SWIVEL                = 0x3320_0000
    PWM_COMPLEMENTARY_CHAIR_FOLD            = 0x3320_0100
    PWM_COMPLEMENTARY_FOOTREST              = 0x3320_0200
    PWM_COMPLEMENTARY_MAIN_DRIVE            = 0x3320_0300

    # --- Utilities ---
    LOGGING                                 = 0x3402_0000
    TASK_MONITOR                            = 0x3405_0000