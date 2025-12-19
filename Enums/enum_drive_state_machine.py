# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class DriveState(EnumUtils, Enum):
    """
    Enum class containing all the base drive states.
    """
    IDLE            = 0
    PRE_RUN         = 1
    MOVING          = 2
    POST_RUN        = 3
    FINALISE        = 4
    INVALID         = 5


@unique
class MovingDriveState(EnumUtils, Enum):
    """
    Enum class containing all the moving drive states.
    """
    IDLE            = 0
    INITIALISE      = 1
    PRE_MOVING      = 2
    MOVING          = 3
    POST_MOVING     = 4


@unique
class ActiveBridge(EnumUtils, Enum):
    """
    Enum class containing the active H-bridge side.
    """
    NONE            = 0
    LEFT            = 1
    RIGHT           = 2
    HOLD            = 3


@unique
class DriveStateData(EnumUtils, Enum):
    """
    Enum class containing the data for the drive state machine tables.
    """
    demand          = 0
    request         = 1
    baseState       = 2
    childState      = 3