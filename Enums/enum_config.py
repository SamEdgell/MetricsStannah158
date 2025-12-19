# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class StoredConfigID(EnumUtils, Enum):
    """
    Enum class containing all the stored config records.
    """
    CONFIG_SEATBELT_FITTED                                  = 0
    CONFIG_UP_DIRECTION                                     = 1
    CONFIG_OPTIONS_PRESENT                                  = 2
    CONFIG_ECUS_IN_SYSTEM                                   = 3
    CONFIG_UNRECOVERABLE_FAULT_PRESENT                      = 4 # BBRAM
    CONFIG_SYNC_FOLD                                        = 5
    CONFIG_DISPLAY_BRIGHTNESS                               = 6
    CONFIG_DISPLAY_MODE                                     = 7
    CONFIG_AUDIO_VOLUME                                     = 8
    CONFIG_ALARMS                                           = 9
    CONFIG_RMU_SHUTDOWN_DISABLE                             = 10
    CONFIG_CREEP_TO_CHARGE_ENABLE                           = 11

    CONFIG_DECEL_STEP_SIZE                                  = 12
    CONFIG_DRIVE_TARGET_VELOCITY                            = 13
    CONFIG_DRIVE_ACCEL_TIME                                 = 14

    CONFIG_DRIVE_PRESENCE_SWIVEL                            = 15
    CONFIG_DRIVE_PRESENCE_FOOTREST                          = 16
    CONFIG_DRIVE_PRESENCE_CHAIR_FOLD                        = 17
    CONFIG_DRIVE_PRESENCE_HINGE                             = 18

    CONFIG_FOOTREST_POS_RAW_OFFSET                          = 19
    CONFIG_FOOTREST_POS_UNFOLD                              = 20
    CONFIG_FOOTREST_POS_FOLD                                = 21

    CONFIG_CHAIR_FOLD_POS_RAW_OFFSET                        = 22
    CONFIG_CHAIR_FOLD_POS_UNFOLD                            = 23
    CONFIG_CHAIR_FOLD_POS_FOLD                              = 24
    CONFIG_CHAIR_FOLD_POS_PARTIAL_FOLD                      = 25

    CONFIG_SWIVEL_POS_POS_RAW_OFFSET                        = 26
    CONFIG_SWIVEL_POS_CENTRE_POSITION                       = 27
    CONFIG_SWIVEL_POS_LEFT_LIMIT                            = 28
    CONFIG_SWIVEL_POS_RIGHT_LIMIT                           = 29
    CONFIG_SWIVEL_POS_LEFT_BOARDING_LIMIT                   = 30
    CONFIG_SWIVEL_POS_RIGHT_BOARDING_LIMIT                  = 31

    CONFIG_HINGE_POS_OFFSET                                 = 32
    CONFIG_HINGE_POS_FOLD                                   = 33
    CONFIG_MAIN_DRIVE_POSITION                              = 34 # BBRAM
    CONFIG_MAIN_DRIVE_POSITION_VALID                        = 35 # BBRAM

    CONFIG_EMC_MODE_ACTIVATED                               = 36
    CONFIG_CURRENT_TIME                                     = 37 # BBRAM

    CONFIG_BOOL_SPARE_2                                     = 38
    CONFIG_BOOL_SPARE_3                                     = 39

    CONFIG_INT32_SPARE_1                                    = 40
    CONFIG_INT32_SPARE_2                                    = 41
    CONFIG_INT32_SPARE_3                                    = 42

    CONFIG_UINT32_SPARE_1                                   = 43
    CONFIG_UINT32_SPARE_2                                   = 44
    CONFIG_UINT32_SPARE_3                                   = 45

    CONFIG_OBJECT_COUNT                                     = 46

    CONFIG_INVALID                                          = 47