# Standard library imports.
from struct import calcsize, pack, unpack

# Local application imports.
from Enums.enum_msg import SrcDest


message_endianess = "<"            # Little endian.
message_CRC_format = "B"           # Format for the CRC byte.
message_header_format = "BHBBBH"   # Little endian. ID, size, source, dest, mode, SRID.
message_header_num_bytes = 8       # Number of bytes in the header.
message_header_num_items = 6       # Number of items in the header once unpacked.


def unpackMessage(payload_format, msg):
    """
    Unpacks full message. Returns the header and payload as separate entities.

    Args:
        payload_format: Payload format to unpack the message with.
        msg:            Message to unpack.

    Returns:
        Unpacked message [header, payload].
    """
    format = f"{message_endianess}{message_header_format}{payload_format}{message_CRC_format}"
    try:
        unpacked_message = unpack(format, msg)
        # The payload also contains the checksum, this is stripped before returning.
        return unpacked_message[:message_header_num_items], unpacked_message[message_header_num_items:-1]
    except Exception as e:
        msg_ID = msg[0]
        expected_size = calcsize(format)
        actual_size = len(msg)
        print(f"E1: {__file__}: {e}")
        print(f'Unable to unpack message ID: 0x{msg_ID:0X}. Expected {expected_size} bytes. Received {actual_size} bytes.')
        return None, None


def unpackMessageHeader(msg):
    """
    Unpacks message header.

    Args:
        msg: Message to unpack.

    Returns:
        Unpacked header.
    """
    format = f"{message_endianess}{message_header_format}"
    header_section = msg[:message_header_num_bytes]
    try:
        header = unpack(format, header_section)
        return header
    except Exception as e:
        msg_ID = msg[0]
        expected_size = calcsize(format)
        actual_size = len(header_section)
        print(f"E2: {__file__}: {e}")
        print(f'Unable to unpack message ID: 0x{msg_ID:0X}. Expected {expected_size} bytes. Received {actual_size} bytes.')
        return None


def unpackMessagePartial(partial_payload_format, msg):
    """
    Unpacks a partial amount of the message payload.

    Args:
        partial_payload_format: Payload partial format to unpack the message with.
        msg:                    Message to unpack.

    Returns:
        Unpacked message partial [header, partialPayload].
    """
    format = f"{message_endianess}{message_header_format}{partial_payload_format}"
    expected_size = calcsize(format)
    try:
        # Unpacks the full header and up to the specified size of bytes in the payload.
        unpacked_message = unpack(format, msg[:expected_size])
        return unpacked_message[:message_header_num_items], unpacked_message[message_header_num_items:]
    except Exception as e:
        msg_ID = msg[0]
        actual_size = len(msg[:expected_size])
        print(f"E3: {__file__}: {e}")
        print(f'Unable to unpack message ID: 0x{msg_ID:0X}. Expected {expected_size} bytes. Received {actual_size} bytes.')
        return None, None


def unpackMessagePayload(payload_format, msg):
    """
    Unpacks message payload.

    Args:
        payload_format: Payload format to unpack the message with.
        msg:            Message to unpack.

    Returns:
        Unpacked payload.
    """
    format = f"{message_endianess}{payload_format}{message_CRC_format}"
    try:
        payload = unpack(format, msg[message_header_num_bytes:])
        return payload[:-1] # The payload also contains the checksum, this is stripped before returning.
    except Exception as e:
        msg_ID = msg[0]
        expected_size = calcsize(format)
        actual_size = len(msg[message_header_num_bytes:])
        print(f"E4: {__file__}: {e}")
        print(f'Unable to unpack message ID: 0x{msg_ID:0X}. Expected {expected_size} bytes. Received {actual_size} bytes.')
        return None


def buildMessage(msg_ID, payload_format, payload, dest, mode, source=SrcDest.SRC_DEST_PC):
    """
    Creates the message to be sent over the serial port.

    Args:
        msg_ID:     Message ID.
        format:     Format of the payload.
        payload:    Payload data.
        dest:       Destination.
        mode:       Mode.
        source:     Source, by default PC, but can be changed for internal message routing and testing.

    Returns:
        Packed message. Still requires encoding.
    """
    try:
        # First pack the payload, because we don't know the true size of payload yet until packed.
        packed_payload = b"" if not payload else pack(f"{message_endianess}{payload_format}", *payload)

        # Then pack the header.
        size = len(packed_payload)
        packed_header = pack(f"{message_endianess}{message_header_format}", msg_ID.value, size, source.value, dest.value, mode.value, 0) # SRID is 0 for now.

        return packed_header + packed_payload
    except Exception as e:
        print(f"E5: {__file__}: {e}")
        print(f'Unable to build message ID: 0x{msg_ID.value:0x}')
        return None