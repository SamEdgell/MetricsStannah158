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
    METRICS_INPUTS_ALTER                = 0x23
    METRICS_RESET_INPUTS_ALTER          = 0x24
    METRICS_OUTPUTS_ALTER               = 0x25
    METRICS_RESET_OUTPUTS_ALTER         = 0x26


@unique
class SrcDest(EnumUtils, Enum):
    """
    Enum class containing all the source/destination IDs.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each source or destination.
    """
    SRC_DEST_NONE           = 0
    SRC_DEST_PC             = 1
    SRC_DEST_ATE            = 2
    SRC_DEST_DEV_BOX        = 3
    SRC_DEST_ECU1           = 4
    SRC_DEST_ECU2           = 5
    SRC_DEST_INSTALLATION   = 6
    SRC_DEST_X06            = 7
    SRC_DEST_HW_TEST_TOOL   = 8


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

    GET_ACK                 = 21
    SET_ACK                 = 22
    REQ_ACK                 = 23
    NACK                    = 24