# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class DiagRequests(EnumUtils, Enum):
    """
    Enum class containing all the diagnostic request codes.
    """
    INVALID                             = 0x0000
    ENABLE_DIAG                         = 0x0011
    DISABLE_DIAG                        = 0x0012

    DIAG_REQ_TEST_A                     = 0x00C0
    DIAG_REQ_TEST_B                     = 0x00C1
    DIAG_REQ_TEST_C                     = 0x00C2
    DIAG_REQ_TEST_D                     = 0x00C3

    DIAG_REQ_TEST_AUDIO                 = 0x00C4

    DIAG_REQ_TEST_E                     = 0x00C5
    DIAG_REQ_TEST_F                     = 0x00C6
    DIAG_REQ_TEST_G                     = 0x00C7
    DIAG_REQ_TEST_H                     = 0x00C8

    DIAG_REQ_MANUAL_DUTY                = 0x0090
    DIAG_REQ_RESET_POSITION             = 0x0091
    DIAG_REQ_DEMAND                     = 0x0092
