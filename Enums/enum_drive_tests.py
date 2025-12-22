# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class DriveTest(EnumUtils, Enum):
    """
    Emum class containing all the drive test ID's.
    """
    DRIVE_TEST_RELAY_ON         = 0
    DRIVE_TEST_MOTOR_VOLTS      = 1
    DRIVE_TEST_BOTTOM_FETS      = 2
    DRIVE_TEST_TOP_FETS         = 3
    DRIVE_TEST_RELAY_OFF        = 4