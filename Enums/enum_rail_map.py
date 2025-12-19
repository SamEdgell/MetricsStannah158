# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class MapOperationalMode(EnumUtils, Enum):
    """
    Enum class containing all the rail map operating mode.
    """
    DISABLED            = 0     # Acts as there is no rail map.
    EDITING             = 1     # The mode used to edit rail map. The movement is not restricted by the map points.
    POSITION_FINDING    = 2     # This mode is used when the position needs to be re-established.
    RESTRICTED          = 3     # In this mode the movement is fully restricted to the rail map profile.


@unique
class RailMap(EnumUtils, Enum):
    """
    Enum class containing all the rail map variables for the table.
    """
    operationalMode     = 0
    numStops            = 1
    leftStopIndex       = 2
    rightStopIndex      = 3
    gyroX               = 4
    gyroY               = 5
    gyroZ               = 6
    currentPosition     = 7


@unique
class RailMapModes(EnumUtils, Enum):
    """
    Enum class containing all the rail map modes.
    """
    ENABLED                     = (1<<0)
    BOARDING                    = (1<<1)
    PARKING                     = (1<<2)
    UNPACK_ON_ARRIVAL           = (1<<3)

    SWIVEL_LEFT_ENABLED         = (1<<4)
    SWIVEL_RIGHT_ENABLED        = (1<<5)
    PARTIAL_UNFOLD_ZONE         = (1<<6)
    HALF_SPEED_ZONE             = (1<<7)

    NARROW_ZONE                 = (1<<8)
    WIDE_ZONE                   = (1<<9)
    SWIVEL_ANGLE_80DEG          = (1<<10)
    REMOTE_CONTROL_POINT_A      = (1<<11)

    REMOTE_CONTROL_POINT_B      = (1<<12)
    REMOTE_CONTROL_POINT_C      = (1<<13)
    REMOTE_CONTROL_POINT_D      = (1<<14)
    UNUSED                      = (1<<15)