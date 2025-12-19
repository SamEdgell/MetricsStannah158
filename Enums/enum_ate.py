# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class ATERequests(EnumUtils, Enum):
    """
    Enum class containing all the ATE request codes.
    """
    ATE_REQ_NOT_SET                     = 0x0000

    ATE_ENERGISE_UP_SAFETY_CHAIN        = 0x0020
    ATE_ENERGISE_DOWN_SAFETY_CHAIN      = 0x0021
    ATE_DEENERGISE_SAFETY_CHAIN         = 0x0022

    ATE_MAIN_DRIVE_SET_POSITION         = 0x0030

    ATE_TRIGGER_FAULT                   = 0x0032

    ATE_STORED_CONFIGURATION_GET        = 0x0040
    ATE_STORED_CONFIGURATION_SET        = 0x0041
