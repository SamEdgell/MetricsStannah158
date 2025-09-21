# Local application imports.
from Enums.enum_msg import MessageID


SOM = 0x01
EOM = 0x04
DLE = 0x10

MAX_BUFFER_SIZE = 2048


class ProtocolParser:
    """
    Class for parsing incoming serial data and encoding outgoing serial data.
    """

    def __init__(self, callback=None):
        """
        Initialises the ProtocolParser class.

        Args:
            callback: Callback method to be called when a new message is received. This is optional and not all objects will require a callback.
        """
        self.rx_buffer = bytearray()
        self.callbackMethod = callback
        self.reset()


    def reset(self):
        """
        Resets the parser to a known state.
        """
        self.escaped = False
        self.started = False
        self.msg_size = 0
        self.crc = 0
        self.rx_buffer.clear()


    def parseMessage(self, data):
        """
        Parses all incoming bytes and determines if a new message has been received.

        Args:
            data: Buffer of incoming bytes to be parsed.
        """
        for byte in data:
            insert = False
            msg_received = False

            if not self.escaped:
                if byte == DLE:
                    self.escaped = True
                else:
                    insert = True
            else:
                if byte == SOM:
                    self.rx_buffer.clear()
                    self.started = True
                    self.msg_size = 0
                    self.crc = 0
                elif byte == EOM:
                    if self.started:
                        self.started = False
                        if self.crc == 0:
                            msg_received = True
                        else:
                            print(f"CRC Error! Msg ID: {self.rx_buffer[0]:0X}")
                            self.reset()
                else:
                    insert = True
                self.escaped = False

            if self.started and insert:
                if self.msg_size < MAX_BUFFER_SIZE:
                    self.rx_buffer.append(byte)
                    self.msg_size += 1
                    self.crc ^= byte
                else:
                    print(f"Message Length Too Long: {self.msg_size}")
                    self.reset()

            if msg_received:
                if self.callbackMethod:
                    if self.rx_buffer[0] in [msg_id.value for msg_id in MessageID]:
                        # Create a copy of the message to avoid reference issues.
                        message = bytes(self.rx_buffer[:self.msg_size])
                        # When a complete message is received and approved, the callback method provided at instantiation will be called where it will add the new message to the queue.
                        self.callbackMethod(message)
                self.reset()  # Reset after successful message.


    @staticmethod
    def encodeMessage(msg):
        """
        Encodes a message to the required serial format. This static method allows encoding without instantiating the class.

        Args:
            msg: Message to encode (as a bytes-like object).

        Returns:
            Encoded message as a bytearray.
        """
        out_msg = bytearray([DLE, SOM])
        crc = 0

        for byte in msg:
            if byte == DLE:
                out_msg.append(DLE)
            out_msg.append(byte)
            crc ^= byte

        out_msg.extend([crc, DLE, EOM])

        return out_msg


    @staticmethod
    def decodeMessage(msg, is_encoded=True):
        """
        For debugging purposes only. Decodes either the encoded message or the built message. This static method allows decoding without instantiating the class.

        Args:
            msg:        Message to decode.
            is_encoded: If True, the message is encoded. If False, the message is built only.
        """
        print(f"\n------ Decode Message ------")

        if is_encoded:
            spaced_full_message = ' '.join(f'{byte:02x}' for byte in msg)   # Full message: all bytes.
            spaced_header = ' '.join(f'{byte:02x}' for byte in msg[2:10])   # Header: index 2 to 10.
            spaced_payload = ' '.join(f'{byte:02x}' for byte in msg[10:-3]) # Payload: index 10 to -3.
            spaced_CRC = ' '.join(f'{byte:02x}' for byte in msg[-3:-2])     # CRC: Third last byte.
            print(f"\nDecoded Message: {spaced_full_message}")
            print(f"\nDecoded Header: {spaced_header}")
            print(f"\nDecoded Payload: {spaced_payload}")
            print(f"\nDecoded CRC: {spaced_CRC}")
        else:
            spaced_header = ' '.join(f'{byte:02x}' for byte in msg[0:8])    # Header: index 0 to 8.
            spaced_payload = ' '.join(f'{byte:02x}' for byte in msg[8:])    # Payload: index 8 onward.
            print(f"\nBuilt Header: {spaced_header}")
            print(f"\nBuilt Payload: {spaced_payload}")

        print(f"\n------ Decode Message End ------\n")