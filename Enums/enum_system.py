# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class SystemState(EnumUtils, Enum):
    """
    Enum class containing all system states.
    """
    INVALID             = 0
    INITIALISATION      = 1
    NORMAL              = 2
    LOW_POWER           = 3
    FAULTED             = 4
    SOFTWARE_UPDATE     = 5
    STANDBY             = 6
    NUMBER_OF_STATES    = 7


@unique
class SystemData(EnumUtils, Enum):
    """
    Enum class containing various system data.
    """
    X01SystemState      = 0
    X04SystemState      = 1
    X01OpMode           = 2
    X04OpMode           = 3
    Handing             = 4


@unique
class OperationalMode(EnumUtils, Enum):
    """
    Enum class containing the operational modes.
    """
    END_USER            = 0
    ATE                 = 1
    SERVICE             = 2
    HW_TEST_MODE        = 3
    EMC                 = 4


@unique
class SystemVersion(EnumUtils, Enum):
    """
    Enum class containing system version data.
    """
    X01_Version             = 0
    X01_VersionSuffix       = 1
    X01_ProductID           = 2
    X01_SerialNumber        = 3
    X04_Version             = 4
    X04_VersionSuffix       = 5
    X04_ProductID           = 6
    X04_SerialNumber        = 7


@unique
class UpDirection(EnumUtils, Enum):
    """
    Enum class containing the handing states.
    """
    UP_IS_LEFT              = 0
    UP_IS_RIGHT             = 1
    UNKNOWN                 = 99


@unique
class RTC(EnumUtils, Enum):
    """
    Enum class containing the variables in the 'timeTable'.
    """
    SystemTime              = 0
    SystemTimeUnix          = 1
    ECUTime                 = 2
    ECUTimeUnix             = 3


@unique
class AssertData(EnumUtils, Enum):
    """
    Enum class containing the assert data.
    """
    File                    = 0
    Error                   = 1
    Line                    = 2
    Source                  = 3