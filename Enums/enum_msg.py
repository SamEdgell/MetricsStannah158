# Standard library imports.
from enum import Enum, unique

# Local application imports.
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

    SYSTEM_STATE                        = 0x10
    SYSTEM_VERSION                      = 0x11
    SYSTEM_CONFIGURATION                = 0x12

    RTC_TIME                            = 0x32
    RESET_ALL_CONFIG                    = 0x33

    RMM_REPORT                          = 0x40
    RMM_DELETE_ALL                      = 0x41
    RMM_MAP_MODE                        = 0x42
    RMM_UPDATE_POINT                    = 0x43
    RMM_NEW_POINT                       = 0x44
    RMM_DELETE_POINT                    = 0x45
    RMM_SAVE_MAP                        = 0x46
    RMM_NEW_POINT_AT_POS                = 0x47
    RMM_POSITION_REPORT                 = 0x48
    RMM_POSITION_QUERY                  = 0x49

    SYSTEM_OP_MODE                      = 0x50
    CALL_REQUEST                        = 0x51
    CALIBRATION_REQUEST                 = 0x52
    END_CALIBRATION                     = 0x53
    ATE_REQUEST                         = 0x58

    CLEAR_UNRECOVERABLE_FAULT           = 0x61
    E_CODE_CHANGED                      = 0x62

    GPIO_OUTPUT_STATUS                  = 0x70
    GPIO_INPUT_STATUS                   = 0x71
    ADC_STATUS                          = 0x72

    METRIC_EVENT                        = 0xA0
    METRIC_ADC_STATUS                   = 0xA4
    METRIC_GPIO_OUTPUT_STATUS           = 0xA5
    METRIC_GPIO_INPUT_STATUS            = 0xA6
    METRIC_GPIO_OUTPUTS_OVERRIDE        = 0xA7
    METRIC_GPIO_INPUTS_OVERRIDE         = 0xA8
    METRIC_ADC_INPUTS_OVERRIDE          = 0xA9

    METRIC_AUTOMATION_DATA              = 0xAC

    STORED_CONFIGURATION                = 0xDA

    GENERIC_DRIVE_TUNING_DATA           = 0xD5
    GENERIC_DRIVE_STATE_MACHINE_DATA    = 0xD6
    GENERIC_DRIVE_POSITION_HS_DATA      = 0xD7
    GENERIC_DRIVE_CONTROL_HS_DATA       = 0xD8

    HS_LOGGING_ENABLE                   = 0xE1

    DIAGNOSTIC_REQUEST                  = 0xF0
    SOFTWARE_CALL                       = 0xF1
    OVERRIDE_INPUT                      = 0xF2
    OVERRIDE_INPUT_RESET                = 0xF3
    OVERRIDE_OUTPUT                     = 0xF4
    OVERRIDE_OUTPUT_RESET               = 0xF5
    RESET_STORED_DATA                   = 0xF9


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
    SRC_DEST_X04            = 4
    SRC_DEST_X01            = 5
    SRC_DEST_INSTALLATION   = 6
    SRC_DEST_X06            = 7
    SRC_DEST_HW_TEST_TOOL   = 8


@unique
class MsgMode(EnumUtils, Enum):
    """
    Enum class containing all the message modes.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each message mode.
    """
    OUT                 = 0
    GET                 = 1
    SET                 = 2
    REQ                 = 3
    GET_ACK             = 21
    SET_ACK             = 22
    REQ_ACK             = 23
    NACK                = 30


@unique
class ASCII(EnumUtils, Enum):
    """
    Enum class containing all the ASCII values used.
    Inherits from EnumUtils and Python's Enum to provide utility methods and a set of unique, type-safe constants representing each ASCII value.
    """
    NULL                   = 0x00
    SOH                    = 0x01
    EOT                    = 0x04
    DLE                    = 0x10