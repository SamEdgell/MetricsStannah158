# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class ChairPositionData(EnumUtils, Enum):
    """
    Enum class containing all the drive position data ID's for chair fold.
    """
    currentPosition     = 0
    foldLimit           = 1
    partFoldLimit       = 2
    unfoldLimit         = 3
    rawPosition         = 4
    cycles              = 5
    position            = 6


@unique
class ChairPositions(EnumUtils, Enum):
    """
    Enum class containing the chair fold positions.
    """
    FULLY_FOLDED        = 0
    FULLY_UNFOLDED      = 1
    PARTIAL_FOLD        = 2
    FOLDED              = 3
    UNFOLDED            = 4
    UNKNOWN             = 5


@unique
class FootrestPositionData(EnumUtils, Enum):
    """
    Enum class containing all the drive position data ID's for footrest.
    """
    currentPosition     = 0
    foldLimit           = 1
    unfoldLimit         = 2
    rawPosition         = 3
    cycles              = 4
    position            = 5


@unique
class FootrestPositions(EnumUtils, Enum):
    """
    Enum class containing the footrest positions.
    """
    FOLDED              = 0
    UNFOLDED            = 1
    IN_TRANSITION       = 2
    UNKNOWN             = 3


@unique
class MainPositionData(EnumUtils, Enum):
    """
    Enum class containing all the drive position data ID's for main drive.
    """
    encoderValue        = 0
    encoderPosition     = 1


@unique
class SwivelPositionData(EnumUtils, Enum):
    """
    Enum class containing all the drive position data ID's for swivel.
    """
    currentPosition     = 0
    leftLimit           = 1
    centre              = 2
    rightLimit          = 3
    rawPosition         = 4
    cycles              = 5
    position            = 6


@unique
class SwivelPositions(EnumUtils, Enum):
    """
    Enum class containing the swivel positions.
    """
    FULLY_LEFT          = 0
    LEFT                = 1
    CENTRE              = 2
    RIGHT               = 3
    FULLY_RIGHT         = 4
    UNKNOWN             = 5