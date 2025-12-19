# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class SystemDrive(EnumUtils, Enum):
    """
    Enum class containing all the system drive types.
    """
    SYS_DRIVE_SWIVEL                    = 0
    SYS_DRIVE_CHAIR_FOLD                = 1
    SYS_DRIVE_FOOTREST                  = 2
    SYS_DRIVE_HINGE                     = 3
    SYS_DRIVE_MAIN_DRIVE                = 4