# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class PID(EnumUtils, Enum):
    """
    Enum class containing all the PID data ID.
    """
    driveId             = 0
    tickMs              = 1
    currentPosition     = 2
    targetPosition      = 3
    currentSpeed        = 4
    targetSpeed         = 5
    error               = 6
    integral            = 7
    derivative          = 8
    speedError          = 9
    speedIntegral       = 10
    speedDerivative     = 11
    kpTerm              = 12
    kiTerm              = 13
    kdTerm              = 14
    kffTerm             = 15
    kPSpeedTerm         = 16
    kISpeedTerm         = 17
    kDSpeedTerm         = 18
    output              = 19
    current             = 20