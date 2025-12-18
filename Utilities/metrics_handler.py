# Standard library imports.
import re
from datetime import datetime
from enum import Enum, unique

# Local application imports.
from Enums.enum_gpio import InputsX04, InputsX01, LogicState, OutputsX04, OutputsX01
from Enums.enum_metrics import MetricSubcodes
from Enums.enum_msg import MsgMode, SrcDest
from UI.ui_styling import Colours, CSS
from Utilities.messages import unpackMessage


"""
Metrics handler expects to receive messages in the following format:

Message Header:
    Message ID (1 byte) | Size (2 bytes) | Source (1 byte) | Destination (1 byte) | Mode (1 byte) | SRID (2 bytes)
Metric Payload:
    Metric Subcode (2 bytes) | Timestamp (8 bytes) | Sequence Number (2 bytes) | UUID (4 bytes) | Mode (4 bytes) | Data1 (4 bytes) | Data2 (4 bytes) | Data3 (4 bytes) | Data4 (4 bytes)
"""
METRIC_PAYLOAD_FORMAT = "HQH6I"


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@unique
class MessageStyleCode(Enum):
    """
    Enum for style codes used to display metric messages on the UIConsole.
    Inherits from Python's Enum to provide a set of unique, type-safe constants that are used as keys for CSS styling and message formatting.
    """
    COMPONENT_FAULT         = 0x0000

    STYLE_1                 = 0x0001
    STYLE_2                 = 0x0002
    STYLE_3                 = 0x0003
    STYLE_4                 = 0x0004
    STYLE_5                 = 0x0005
    STYLE_6                 = 0x0006
    STYLE_7                 = 0x0007
    STYLE_8                 = 0x0008

    # Non Metric specific styles Below.
    TEST                    = 0xFFF8
    WARNING                 = 0xFFF9
    PASS                    = 0xFFFA
    DEFAULT                 = 0xFFFB
    ERROR                   = 0xFFFC
    SEQUENCE_NUMBER         = 0xFFFD
    TIME_STAMP_EVEN         = 0xFFFE
    TIME_STAMP_ODD          = 0xFFFF


# All possible style codes for the metric messages displayed on the UIConsole.
CSS_STYLE = {
    MessageStyleCode.COMPONENT_FAULT:           f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",

    MessageStyleCode.STYLE_1:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.PASTEL_PINK.name()};",
    MessageStyleCode.STYLE_2:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.LIME_GREEN.name()};",
    MessageStyleCode.STYLE_3:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.PERIWINKLE.name()};",
    MessageStyleCode.STYLE_4:                   f"color: {Colours.AMBER.name()}; background-color: {Colours.FOREST_GREEN.name()};",
    MessageStyleCode.STYLE_5:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.GOLDEN_YELLOW.name()};",
    MessageStyleCode.STYLE_6:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.BRIGHT_CYAN.name()};",
    MessageStyleCode.STYLE_7:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.ELECTRIC_LIME.name()};",
    MessageStyleCode.STYLE_8:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.LAVENDER.name()};",

    # Non Metric specific styles Below.
    MessageStyleCode.TEST:                      f"color: {Colours.BLACK.name()}; background-color: {Colours.YELLOW.name()};",
    MessageStyleCode.WARNING:                   f"color: {Colours.BLACK.name()}; background-color: {Colours.MARIGOLD.name()};",
    MessageStyleCode.PASS:                      f"color: {Colours.BLACK.name()}; background-color: {Colours.KELLY_GREEN.name()};",
    MessageStyleCode.DEFAULT:                   f"color: {Colours.BLACK.name()};",
    MessageStyleCode.ERROR:                     f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",
    MessageStyleCode.SEQUENCE_NUMBER:           f"color: {Colours.GARNET.name()}",
    MessageStyleCode.TIME_STAMP_EVEN:           f"color: {Colours.BLACK.name()}; background-color: {Colours.GOLD.name()};",
    MessageStyleCode.TIME_STAMP_ODD:            f"color: {Colours.BLACK.name()}; background-color: {Colours.BABY_BLUE.name()};",
}


# Maps a metric subcode to a CSS style code and the desired string to be displayed on the console for that subcode. Further CSS styling of placeholders is handled inside the customisePlaceholders function.
METRIC_SUBCODE_MAPPER = {
    # Subcode Member                                        CSS Style                                   String
    MetricSubcodes.METRIC_INVALID:                          [MessageStyleCode.ERROR,                    "METRIC_INVALID"],
}
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@unique
class PlaceholderStyleCode(Enum):
    """
    Enum for placeholder style codes used to display metric messages on the UIConsole.
    Inherits from Python's Enum to provide a set of unique, type-safe constants that are used as keys for the PLACEHOLDER_STYLE dictionary,
    determining the CSS styling for each placeholder type.
    """
    DEFAULT              = 0
    PASS                 = 1
    WARNING              = 2
    ERROR                = 3

    GPIO_LOW             = 10
    GPIO_HIGH            = 11

    BG_APRICOT           = 20


# Further CSS style codes for the placeholders in the metric message.
PLACEHOLDER_STYLE = {
    PlaceholderStyleCode.DEFAULT:                       f"color: {Colours.BLACK.name()};",
    PlaceholderStyleCode.PASS:                          f"color: {Colours.BLACK.name()}; background-color: {Colours.KELLY_GREEN.name()};",
    PlaceholderStyleCode.WARNING:                       f"color: {Colours.BLACK.name()}; background-color: {Colours.MARIGOLD.name()};",
    PlaceholderStyleCode.ERROR:                         f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",

    PlaceholderStyleCode.GPIO_LOW:                      f"color: {Colours.BLACK.name()}; background-color: {Colours.CORAL_PINK.name()};",
    PlaceholderStyleCode.GPIO_HIGH:                     f"color: {Colours.BLACK.name()}; background-color: {Colours.KELLY_GREEN.name()};",

    PlaceholderStyleCode.BG_APRICOT:                    f"color: {Colours.BLACK.name()}; background-color: {Colours.APRICOT.name()};",
}
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def processMetrics(app_instance, msg):
    """
    Processes a Metric message received from the serial port.

    Args:
        app_instance:   App instance to emit the formatted metric message to the UIConsole.
        msg:            The metric message to handle.
    """
    # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
    if MsgMode(msg[5]) == MsgMode.OUT:
        header, metric_payload = unpackMessage(METRIC_PAYLOAD_FORMAT, msg)
        source = header[2]
        seq_num = metric_payload[2]

        # Style the timestamp.
        timestamp = formatTimestamp(seq_num)

        # Style the metric message.
        metric_message = formatMetricMessage(header, metric_payload)

        # Build string to emit to the UIConsole.
        console_string = timestamp + metric_message

        # Emit the string to the appropriate console.
        if SrcDest(source) == SrcDest.SRC_DEST_X04:
            # Emit to primary console.
            app_instance.signal_slot.primary_console_signal.emit(console_string)
        elif SrcDest(source) == SrcDest.SRC_DEST_X01:
            # Emit to secondary console.
            app_instance.signal_slot.secondary_console_signal.emit(console_string)


def styleString(style, whitespace_amount, string):
    """
    Styles a string with the given CSS style and surrounding whitespace.

    Args:
        style:              The CSS style.
        whitespace_amount:  The amount of whitespaces to add on each side.
        string:             The string to append.

    Returns:
        The formatted string with CSS styling and whitespace.
    """
    whitespace_str = CSS.WHITE_SPACE * whitespace_amount
    formatted_string = (
        f"{CSS.START_STYLE}{style}{CSS.START_STYLE_END}"
        f"{whitespace_str}{string}{whitespace_str}"
        f"{CSS.END_STYLE}"
    )
    return formatted_string


def formatTimestamp(seq_num):
    """
    Formats the string with a timestamp and sequence number using CSS styling.

    Args:
        seq_num: The sequence number of the message.

    Returns:
        The formatted timestamp string.
    """
    # Choose the timestamp style based on whether the sequence number is odd or even.
    if seq_num % 2:
        time_stamp_style = CSS_STYLE.get(MessageStyleCode.TIME_STAMP_ODD)
    else:
        time_stamp_style = CSS_STYLE.get(MessageStyleCode.TIME_STAMP_EVEN)

    # Format the current time with the chosen style.
    time_string = styleString(time_stamp_style, 0, f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}")

    # Format the sequence number with the chosen style.
    sequence_number_string = styleString(CSS_STYLE.get(MessageStyleCode.SEQUENCE_NUMBER), 0, f"{seq_num:0X}")

    # Combine the timestamp and sequence number, separated by white spaces.
    timestamp_string = time_string + CSS.WHITE_SPACE + sequence_number_string + CSS.WHITE_SPACE

    return timestamp_string


def formatMetricMessage(header, payload):
    """
    Formats the Metric message based on its subcode.

    Args:
        header:     The metric message header information.
        payload:    The metric message to format.

    Returns:
        The formatted metric message as a styled string.
    """
    subcode = payload[0]

    # Check if the metric subcode is recognised.
    if MetricSubcodes.doesValueExist(subcode):
        # Returns the member of the metric subcode based on its value.
        subcode_member = MetricSubcodes.getMember(subcode)

        # Map the style/string of the subcode member.
        subcode_member_style, subcode_member_string = METRIC_SUBCODE_MAPPER.get(subcode_member, (None, None))

        if subcode_member_style and subcode_member_string:
            # Get the CSS style for the metric subcode.
            message_CSS_style = CSS_STYLE.get(subcode_member_style)

            if message_CSS_style:
                try:
                    # Customise any placeholders within the message.
                    formatted_string = formatPlaceholders(subcode_member_string, header, payload)
                except Exception as e:
                    # Error occurred during formatting of a placeholder within the message.
                    formatted_string = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder Formatting Error: 0x{subcode:0X}, {e}")

                # Return the formatted message, either the customised placeholders or the error string.
                return styleString(message_CSS_style, 0, formatted_string)
            else:
                # Return error - CSS style not found for the message.
                return styleString(CSS_STYLE.get(MessageStyleCode.ERROR), 1, f"CSS_STYLE Error: 0x{subcode:0X}")
        else:
            # Return error - Subcode member style/string not found in the mapper.
            return styleString(CSS_STYLE.get(MessageStyleCode.ERROR), 1, f"METRIC_SUBCODE_MAPPER Error: 0x{subcode:0X}")
    else:
        # Return error - Metric subcode is not recognised.
        return styleString(CSS_STYLE.get(MessageStyleCode.ERROR), 1, f"Unknown Metric Subcode: 0x{subcode:0X}")


def formatPlaceholders(subcode_member_string, header, payload):
    """
    Scans the METRIC_SUBCODE_MAPPER string for placeholders and customises them accordingly, if no customisation is provided for the placeholder, the raw value will be used.
    If there are no placeholders, the raw string will be returned.

    Args:
        subcode_member_string:  The METRIC_SUBCODE_MAPPER string to scan for placeholders and format.
        header:                 The metric message header information.
        payload:                The metric message payload to alter for the string.

    Returns:
        The customised placeholder string.
    """
    uuid = payload[3]
    source = header[2]

    # Convert tuple to list for easier manipulation.
    placeholders = list(payload[5:])  # The payload data we are interested in starts from index 5.

    # Find all placeholders in the METRIC_SUBCODE_MAPPER string, including special cases like {UUID} with no numbers.
    placeholder_pattern = re.compile(r'{(\d+)(?::([^}]+))?}|{([a-zA-Z]+[0-9]*)}') # Regex has three capturing groups - NumberOnly, NumberAndFormat, SpecialFormat.
    num_matching_placeholders = placeholder_pattern.findall(subcode_member_string)

    # Iterate through each placeholder match and customise them as needed.
    for index, format, special_format in num_matching_placeholders:
        # Get the exact placeholder string (e.g. {0}, {0:CHAR4}, {UUID}) as it appears in the curly braces {}, so it can be replaced in the string or used in error messages.
        placeholder = f"{{{special_format}}}" if special_format else f"{{{index}:{format}}}" if format else f"{{{index}}}"
        try:
            if special_format:
                # Handle special formats that do not follow the standard {0:xyz}.
                if special_format == 'UUID':
                    styled_placeholder = f"{uuid & 0xFFFFFFFF}"  # Ensure UUID is treated as a 4-byte value.
                else:
                    # Unknown special format.
                    styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Special Placeholder Unknown Format: {special_format}")
            else:
                data = placeholders[int(index)] # Get the data value for this placeholder index from the payload.

                if not format:
                    # No format identifier present, so just print the raw data value as a string.
                    styled_placeholder = str(data)
                else:
                    if format == 'CHAR4':
                        # Convert the 4-byte integer to a string, removing any null terminators.
                        try:
                            styled_placeholder = data.to_bytes(4, byteorder='little').decode('utf-8').replace('\x00', '')
                        except UnicodeDecodeError:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'GPIO_INPUTS':
                        if SrcDest(source) == SrcDest.SRC_DEST_X04 and InputsX04.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{InputsX04(data).name}")
                        elif SrcDest(source) == SrcDest.SRC_DEST_X01 and InputsX01.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{InputsX01(data).name}")
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'GPIO_OUTPUTS':
                        if SrcDest(source) == SrcDest.SRC_DEST_X04 and OutputsX04.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{OutputsX04(data).name}")
                        elif SrcDest(source) == SrcDest.SRC_DEST_X01 and OutputsX01.doesValueExist(data):
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.BG_APRICOT], 0, f"{OutputsX01(data).name}")
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 'LOGIC_STATE':
                        if LogicState.doesValueExist(data):
                            if data == LogicState.LOGIC_0.value:
                                styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.GPIO_LOW], 2, f"0")
                            else:
                                styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.GPIO_HIGH], 2, f"1")
                        else:
                            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {data}")

                    elif format == 's32':
                        # Convert data to signed integer if format is s32.
                        data = int.from_bytes(data.to_bytes(4, byteorder='little', signed=False), byteorder='little', signed=True)
                        styled_placeholder = str(data)

                    elif format == 'Volts':
                        # Convert data from millivolts to volts with two decimal places.
                        styled_placeholder = f"{data / 1000:.2f}"

                    else:
                        # Unknown format for this placeholder.
                        styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Unknown Format: {format}")

        except Exception as e:
            # Catch any unexpected errors for this placeholder.
            styled_placeholder = styleString(PLACEHOLDER_STYLE[PlaceholderStyleCode.ERROR], 1, f"Placeholder {placeholder} Error: {e}")

        # Replace the placeholder in the string with the newly styled value.
        subcode_member_string = subcode_member_string.replace(placeholder, styled_placeholder)

    return subcode_member_string # If there are no matches to the regex group, the original string is returned unchanged.