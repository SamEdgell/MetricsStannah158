# Standard library imports.
from enum import Enum, unique

# Local application imports.
from Enums.enum_utils import EnumUtils


@unique
class ErrorType(EnumUtils, Enum):
    """
    Enum class containing all the error types.
    """
    NO_ERROR            = 0
    GENERIC             = 1
    ERROR               = 2
    NXP_ERROR           = 3 # Error occurred in NXP and we caught it
    NXP_HOOK            = 4 # Error occurred in NXP and we failed to catch it
    POINTER_NOT_NULL    = 5
    CORRECT_LENGTH      = 6
    CORRECT_VALUE       = 7
    CORRECT_STATE       = 8

    # Errors that weren't caused by an assert
    UNHANDLED_IRQ       = 9
    HARD_FAULT          = 10
    SIGNAL_SIGABRT      = 11 # Software error (e.g. array bounds)
    SIGNAL_UNHANDLED    = 12 # Software error (unhandled as yet)
    SIGNAL_CPP          = 13 # An unhandled CPP error occurred
    STACK_OVERFLOW      = 14