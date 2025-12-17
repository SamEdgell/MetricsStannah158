# Local application imports.
from Enums.enum_msg import ASCII, MessageID


class COBSParser:
    """
    Class for parsing incoming serial data and encoding outgoing serial data using COBS byte stuffing.
    """

    def __init__(self, callback=None):
        """
        Initialises the COBSParser class.

        Args:
            callback: Callback method to be called when a new message is received. This is optional and not all objects will require a callback.
        """
        self.rx_buffer = bytearray()
        self.callbackMethod = callback
        self.MAX_BUFFER_SIZE = 1024
        self.MAX_BLOCK_SIZE = 0xFF


    def parseBytes(self, data):
        """
        Parses all incoming bytes and determines if a new message has been received.

        Args:
            data: Buffer of incoming bytes to be parsed.
        """
        for byte in data:
            self.rx_buffer.append(byte) # Append the byte to the buffer. The reason we do this before checking for ASCII.NULL is because if it is ASCII.NULL, it is required as part of the message to correctly decode.

            # Now check whether this is the end of the frame.
            if byte == ASCII.NULL.value:
                message = self.decodeMessage(self.rx_buffer) # Pass the message on for decoding and check to see if it is a valid message.

                self.rx_buffer.clear() # We no longer care about the data in this buffer, clear it.

                if message:
                    if self.callbackMethod:
                        if message[0] in (msg_id.value for msg_id in MessageID):
                            # When a complete message is received and approved, the callback method provided at instantiation will be called where it will add the new message to the queue.
                            self.callbackMethod(message)
            else:
                # Check to see if we have gotten out of sync, if so, dispose of current data in the buffer and start again.
                if len(self.rx_buffer) > self.MAX_BUFFER_SIZE:
                    self.rx_buffer.clear()


    def encodeMessage(self, msg):
        """
        Encodes the given message using COBS byte stuffing.

        Args:
            msg: List of incoming bytes to be encoded.

        Returns:
            Encoded message as a bytearray.
        """
        crc = self.calculateCRC(msg) # First, calulate the CRC.
        message_size = (len(msg) + 1)  # The total message size to encode is the message size +1 for the CRC byte.

        """
        We know the size of the complete message, we can work out the expected size after encoding.
        COBS will only store 254 bytes of data before needing to add an additional code byte should the size of the message exceed a blocks max length.
        """
        block_overhead_bytes = (message_size // 254) # If the buffer is greater than 254 bytes, calculate the total number of overhead bytes that signal new blocks.
        expected_len = (message_size + block_overhead_bytes + 2)  # +2 accounts for the first blocks overhead byte, and the ASCII.NULL byte to signal end of frame.

        encoded_msg = bytearray(expected_len) # Create the output message buffer.

        # Encode message.
        overhead_block_ptr = 0 # Pointer to the encoded_msg buffer which we will be writing the encoded message to. Pointing at encoded_msg[0] initially.
        write_ptr = 1 # Pointer to the encoded_msg buffer which which we will be writing the encoded message to. Pointing at encoded_msg[1] initially.
        overhead_count = 0x01 # A new block is about to start, at a minimum threre is always 1 byte in a block, hence its count is set to 1 here.

        for i in range(message_size):
            byte = msg[i] if i < len(msg) else crc # Iterate through the message bytes until we are at the end, then add the CRC for encoding to complete the encoded message.

            if byte != ASCII.NULL.value:
                encoded_msg[write_ptr] = byte # Byte is not ASCII.NULL, add it to the encoded message.
                write_ptr += 1 # Shift the write pointer to the next location.
                overhead_count += 1 # Increment because we have a valid byte.

            # If we have reached an ASCII.NULL byte, or filled the block (a block can only contain 254 bytes of data), terminate this block and restart with a new one.
            if byte == ASCII.NULL.value or overhead_count == self.MAX_BLOCK_SIZE:
                encoded_msg[overhead_block_ptr] = overhead_count # Update the overhead byte for this block.
                overhead_count = 0x01 # Reset the overhead count.
                overhead_block_ptr = write_ptr # Move the overhead block pointer to the current write pointer location.
                write_ptr += 1 # Move the write pointer to the next location for writing data.

        encoded_msg[overhead_block_ptr] = overhead_count # Update the overhead count for the final block.
        encoded_msg[write_ptr] = ASCII.NULL.value # Finally, append the ASCCII.NULL byte signalling end of frame.

        return encoded_msg


    def decodeMessage(self, msg):
        """
        Decodes the given message using COBS byte stuffing.

        Args:
            msg: List of incoming bytes to be decoded.

        Returns:
            Decoded message as a bytearray.
        """
        decoded_msg = bytearray() # Create the output buffer to store the decoded message.
        read_ptr = 0 # Pointer to the msg buffer. Pointing at msg[0] initially.
        overhead_count = self.MAX_BLOCK_SIZE # Initial value unused until the first iteration has finished.
        block_size = 0 # Size of the current block being processed. Initially start of with zero.

        while read_ptr < len(msg):
            if block_size > 0:
                decoded_msg.append(msg[read_ptr])
                read_ptr += 1
                block_size -= 1
            else:
                next_block_size = msg[read_ptr] # The first byte in a block is the overhead byte which indicates how many bytes are in this block.
                read_ptr += 1

                if next_block_size == ASCII.NULL.value:
                    break # Reached end of frame.

                if overhead_count != self.MAX_BLOCK_SIZE:
                    decoded_msg.append(ASCII.NULL.value)

                overhead_count = next_block_size

                block_size = overhead_count - 1 # Subtract 1 to account for the overhead byte itself.

        if not decoded_msg:
            return bytearray() # Empty message, return an empty bytearray, this is perceived as False by the caller.

        received_crc = decoded_msg[-1] # The last byte in the decoded message is the CRC.
        calculated_crc = self.calculateCRC(decoded_msg[:-1]) # Calculate the CRC of the decoded message excluding the received CRC byte.

        if received_crc == calculated_crc:
            return decoded_msg # Return the decoded message, this includes the CRC byte at the end.
        else:
            return bytearray() # CRC mismatch, return an empty bytearray, this is perceived as False by the caller.


    def calculateCRC(self, msg):
        """
        Calculates the CRC-8 of the given msg.

        Args:
            msg: Message buffer for which to calculate the CRC.

        Returns:
            Calculated CRC as an integer.
        """
        crc = 0

        for i in range(len(msg)):
            crc ^= msg[i]

        return crc


    @staticmethod
    def debugMessage(msg, is_encoded=True):
        """
        For debugging purposes only. Decodes either the encoded message or the built message and prints to CMD to see the contents.
        Static to allow calling without instantiating the class.

        Args:
            msg:            Message to debug.
            is_encoded:     If True, the message is encoded. If False, the message is built only.
        """
        print(f"\n------ Debug Message Start ------")

        if is_encoded:
            cobs_parser = COBSParser()
            decoded = cobs_parser.decodeMessage(msg) # Create a temp object to strip the ASCII.NULL byte and decode the message correctly.

            spaced_full_message = ' '.join(f'{byte:02x}' for byte in msg)           # Full message: Before decoding bytes.
            spaced_decoded_message = ' '.join(f'{byte:02x}' for byte in decoded)    # Full message: Decoded bytes.
            spaced_header = ' '.join(f'{byte:02x}' for byte in decoded[0:6])        # Header: index 0 to 5.
            spaced_payload = ' '.join(f'{byte:02x}' for byte in decoded[6:-1])      # Payload: index 6 to -1.
            spaced_CRC = ' '.join(f'{byte:02x}' for byte in decoded[-1:])           # CRC: Always the last byte.
            print(f"\nFull Message: {spaced_full_message}")
            print(f"\nDecoded Message: {spaced_decoded_message}")
            print(f"\nDecoded Header: {spaced_header}")
            print(f"\nDecoded Payload: {spaced_payload}")
            print(f"\nDecoded CRC: {spaced_CRC}")
        else:
            spaced_header = ' '.join(f'{byte:02x}' for byte in msg[0:6])     # Header: index 0 to 6.
            spaced_payload = ' '.join(f'{byte:02x}' for byte in msg[6:])     # Payload: index 6 onward.
            print(f"\nBuilt Header: {spaced_header}")
            print(f"\nBuilt Payload: {spaced_payload}")

        print(f"\n------ Debug Message End ------\n")