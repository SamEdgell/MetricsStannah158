# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class HighSpeedSources(EnumUtils, Enum):
    """
    Enum class containing all the high speed data sources.
    """
    MAIN_MOTOR_DATA                     = 0
    FOOTREST_CTRL_DATA                  = 1
    CHAIR_FOLD_CTRL_DATA                = 2
    SWIVEL_CTRL_DATA                    = 3
    HINGE_CTRL_DATA                     = 4
    MAIN_DRIVE_ENCODER                  = 5
    FOOTREST_POS                        = 6
    SWIVEL_POS                          = 7
    CHAIR_FOLD_POS                      = 8
    HINGE_POS                           = 9
    IMU_DATA                            = 10