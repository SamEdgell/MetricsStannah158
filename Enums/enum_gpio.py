# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class InputsX04(EnumUtils, Enum):
    """
    Enum class containing all the inputs for X04.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each input for ECU1.
    """
    INPUT_MON_UP_CALL                     = 0
    INPUT_MON_DOWN_CALL                   = 1
    INPUT_MON_SW_UP_CALL                  = 2
    INPUT_MON_SW_DOWN_CALL                = 3
    INPUT_CHARGER_PRESENT                 = 4
    INPUT_RMU_SENSE                       = 5
    INPUT_KEY_SENSE                       = 6
    INPUT_SD_CARD_PRESENT                 = 7
    INPUT_MON_ULTIMATE_RETURN             = 8
    INPUT_MON_OSG_FEED                    = 9
    INPUT_MON_OSG_RETURN                  = 10
    INPUT_MON_HANDING_PLUG_2              = 11
    INPUT_MON_HANDING_PLUG_4              = 12
    INPUT_RIGHT_STOP_LIMIT                = 13
    INPUT_MON_RIGHT_SKATE                 = 14
    INPUT_MON_RIGHT_SAFETY                = 15
    INPUT_LEFT_STOP_LIMIT                 = 16
    INPUT_MON_LEFT_SKATE                  = 17
    INPUT_MON_LEFT_SAFETY                 = 18
    INPUT_MON_BOTTOM_FOOTREST             = 19
    INPUT_MON_RELAY_COIL                  = 20
    INPUT_MON_BRAKE_STATE                 = 21


@unique
class InputsX01(EnumUtils, Enum):
    """
    Enum class containing all the inputs for X01.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each input for ECU2.
    """
    INPUT_MON_BISTABLE_FEED               = 0
    INPUT_MON_BISTABLE_RTN                = 1
    INPUT_MON_OVERRIDE                    = 2
    INPUT_MON_JOY_FEED                    = 3
    INPUT_MON_JOY_LEFT                    = 4
    INPUT_MON_JOY_RIGHT                   = 5
    INPUT_MON_SEATBELT                    = 6
    INPUT_LOCAL_CALL_LEFT                 = 7
    INPUT_LOCAL_CALL_RIGHT                = 8
    INPUT_VC_SENSE                        = 9
    INPUT_MON_BISTABLE_SW                 = 10


@unique
class OutputsX04(EnumUtils, Enum):
    """
    Enum class containing all the outputs for X04.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each output for ECU1.
    """
    OUTPUT_N_MAIN_POWER_DISABLE           = 0
    OUTPUT_OPT_DCHRG_CTRL                 = 1
    OUTPUT_SW_CALL_UP                     = 2
    OUTPUT_SW_CALL_DOWN                   = 3
    OUTPUT_CARRIAGE_RELAY_CTRL            = 4
    OUTPUT_CARRIAGE_DISCHG_CTRL           = 5
    OUTPUT_CARRIAGE_SHUTDOWN_EN           = 6
    OUTPUT_BRAKE_CTRL                     = 7
    OUTPUT_OPTIONS_RELAY_CTRL             = 8
    OUTPUT_FOOTREST_SHUTDOWN_EN           = 9
    OUTPUT_AUDIO_GAIN                     = 10


@unique
class OutputsX01(EnumUtils, Enum):
    """
    Enum class containing all the outputs for X01.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each output for ECU2.
    """
    OUTPUT_SWIVEL_SHUTDOWN_EN             = 0
    OUTPUT_CHAIR_FOLD_SHUTDOWN_EN         = 1
    OUTPUT_BISTABLE_TEST_1                = 2
    OUTPUT_BISTABLE_TEST_2                = 3


@unique
class LogicState(EnumUtils, Enum):
    """
    Enum class containing logic state details.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing logic states.
    """
    LOGIC_0                = 0
    LOGIC_1                = 1