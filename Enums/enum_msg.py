from enum import Enum, unique
from Enums.enum_utils import EnumUtils


@unique
class MessageID(EnumUtils, Enum):
    """
    Enum class containing all the message IDs expected over serial.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each message ID.
    """
    HANDSHAKE                           = 0x00
    AUTHENTICATE                        = 0x01
    ENCRYPTION_KEY_TRANSFER             = 0x02
    HEARTBEAT                           = 0x03

    ADC_STATUS                          = 0x10
    GPIO_INPUTS_STATUS                  = 0x11
    GPIO_OUTPUTS_STATUS                 = 0x12

    METRICS_EVENT                       = 0x20
    METRICS_ADC_ALTER                   = 0x21
    METRICS_RESET_ADC_ALTER             = 0x22
    METRICS_GPIO_INPUTS_ALTER           = 0x23
    METRICS_RESET_GPIO_INPUTS_ALTER     = 0x24
    METRICS_GPIO_OUTPUTS_ALTER          = 0x25
    METRICS_RESET_GPIO_OUTPUTS_ALTER    = 0x26


@unique
class SrcDest(EnumUtils, Enum):
    """
    Enum class containing all the source/destination IDs.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each source or destination.
    """
    SRC_DEST_NONE           = 0
    SRC_DEST_PC             = 1
    SRC_DEST_ECU1           = 2
    SRC_DEST_ECU2           = 3


@unique
class MsgMode(EnumUtils, Enum):
    """
    Enum class containing all the message modes.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each message mode.
    """
    OUT                     = 0
    GET                     = 1
    SET                     = 2
    REQ                     = 3

    NACK                    = 10
    GET_ACK                 = 11
    SET_ACK                 = 12
    REQ_ACK                 = 13