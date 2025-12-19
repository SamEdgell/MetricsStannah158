# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class DriveSpeedProfiles(EnumUtils, Enum):
    """
    Enum class containing all the drive speed profiles.
    """
    NORMAL              = 0
    SLOW                = 1
    CREEP               = 2
    CALIBRATION         = 3
    STOPPED             = 4


@unique
class DriveControlDir(EnumUtils, Enum):
    """
    Enum class containing the drive direction of the H-bridge.
    """
    LEFT                = 0
    RIGHT               = 1
    HOLD                = 2