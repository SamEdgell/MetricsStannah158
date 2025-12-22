# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class RMUStates(EnumUtils, Enum):
    """
    Enum class containing all the RMU states.
    """
    STATE_INITIALISING          = 0x00
    STATE_SAVING                = 0x01
    STATE_PROCESSING            = 0x02
    STATE_OPERATING             = 0x03
    STATE_WAITING_FOR_SHUTDOWN  = 0x04
    STATE_SHUTDOWN              = 0x05
