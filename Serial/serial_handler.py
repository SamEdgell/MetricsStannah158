import queue
import serial
import threading
import time

from datetime import datetime, timedelta
from queue import Queue
from Serial.protocol_parser import ProtocolParser


LOOP_PERIOD             = 0.002     # Loop period for the serial handler thread in seconds.
READ_TIMEOUT            = 1         # Timeout for reading from the serial port in seconds.
THREAD_JOIN_TIMEOUT     = 2         # Timeout for joining the serial handler thread in seconds.
COMMUNICATION_TIMEOUT   = 5         # Time delta for communication timeout in seconds.
WRITE_TIMEOUT           = 0.005     # Timeout for writing to the serial port in seconds.


class SerialHandler:
    """
    Handles serial port communication, including connection management, message transmission, reception, and thread safety.
    """

    def __init__(self, port, baud, ui_comms, event_loop):
        """
        Initialises the SerialHandler class.

        Args:
            port:       COM port to connect to.
            baud:       Baud rate for communication.
            ui_comms:   UIComms instance, allowing SerialHandler to send its information to UIComms in a thread-safe way.
            event_loop: Reference to the main thread's asyncio event loop. Required to safely schedule function calls from this background thread to the main async thread, for example, to add a received message to an asyncio.Queue.
        """
        self.port       = port
        self.baud       = baud
        self.ui_comms   = ui_comms
        self.tx_queue   = Queue()
        self.event_loop = event_loop
        self.stopped_communicating = True # Class not communicating at startup.


    ########### Connection Methods ##########


    def connect(self):
        """
        Opens the serial port and starts the handler thread for receiving and parsing data.

        Returns:
            True if connection is successful, False otherwise.
        """
        try:
            self.serial_port = serial.Serial(port                = self.port,
                                             baudrate            = self.baud,
                                             bytesize            = serial.EIGHTBITS,
                                             parity              = serial.PARITY_NONE,
                                             stopbits            = serial.STOPBITS_ONE,
                                             timeout             = READ_TIMEOUT,
                                             xonxoff             = False,
                                             rtscts              = False,
                                             write_timeout       = WRITE_TIMEOUT,
                                             dsrdtr              = False,
                                             inter_byte_timeout  = None,
                                             exclusive           = None)
            self.serial_port.reset_input_buffer()
            self.serial_port.reset_output_buffer()
            # The following below must be set up first before starting the thread.
            self.protocol_parser = ProtocolParser(self.appendMessage)
            self.last_received_data = datetime.now()
            self.stopped_communicating = False
            # Set up the serial handler thread.
            self.serial_thread = threading.Thread(target=self.runSerial)
            self.serial_event = threading.Event()
            self.serial_event.set()
            self.serial_thread.start()
            print("Serial Handler Started")
            return True
        except Exception as e:
            if isinstance(e, serial.SerialException):
                print(f"Unable to open {self.port}: {e}")
            else:
                print(f"E1: {__file__}: {e}")

            # Clean up on failure.
            if hasattr(self, 'serial_port') and self.serial_port and self.serial_port.is_open:
                self.serial_port.close()

            self.serial_port = None
            return False


    def disconnect(self):
        """
        Disconnects the serial handler, stopping the thread and closing the port. Cleans up resources and clears queues to prevent memory leaks.
        """
        try:
            # Stop the thread first, then close the port.
            if hasattr(self, 'serial_event') and self.serial_event:
                self.serial_event.clear()

            if hasattr(self, 'serial_thread') and self.serial_thread and self.serial_thread.is_alive():
                self.serial_thread.join(timeout=THREAD_JOIN_TIMEOUT)
                if self.serial_thread.is_alive():
                    print(f"Warning: The serial thread did not stop gracefully")

            # Close serial port.
            if hasattr(self, 'serial_port') and self.serial_port is not None and self.serial_port.is_open:
                self.serial_port.close()
                print(f"Disconnected from {self.port}")
            else:
                print("No serial port to close.")

            # Clear all resources.
            self.port = None
            self.baud = None
            self.serial_port = None
            self.protocol_parser = None
            self.serial_thread = None
            self.last_received_data = None
            self.stopped_communicating = True

            # Clear the queue to prevent memory leaks.
            while not self.tx_queue.empty():
                try:
                    self.tx_queue.get_nowait()
                except queue.Empty:
                    break
        except Exception as e:
            print(f"E2: {__file__}: {e}")


    ########### Thread Management ##########


    def runSerial(self):
        """
        Main loop for the serial handler thread. Handles receiving data, parsing messages, transmitting queued messages, and monitoring communication status.
        """
        try:
            while self.serial_event.is_set():
                if not self.serial_port or not self.serial_port.is_open:
                    break

                # Read all available data from the serial port.
                if self.serial_port.in_waiting > 0:
                    data = self.serial_port.read(self.serial_port.in_waiting)
                    if data:
                        self.ui_comms.signal_slot.rx_bytes_signal.emit(len(data))
                        self.protocol_parser.parseMessage(data)
                        self.last_received_data = datetime.now()
                        if self.stopped_communicating:
                            self.stopped_communicating = False
                            print(f"Regained communication with {self.port}")

                # Process the write queue if communication is active and data is available to transmit.
                if not self.stopped_communicating and not self.tx_queue.empty():
                    try:
                        msg = self.tx_queue.get_nowait()
                        bytes_written = self.serial_port.write(msg)
                        self.ui_comms.signal_slot.tx_bytes_signal.emit(bytes_written)
                        if bytes_written < len(msg): # Check if all bytes were written.
                            self.stopped_communicating = True
                            print(f"Write failed to {self.port} - only {bytes_written}/{len(msg)} bytes written.")
                    except (serial.SerialException, OSError) as e:
                        # Handle serial/OS errors when port is disconnected.
                        if self.ui_comms.authenticated and not self.stopped_communicating:
                            self.stopped_communicating = True
                            print(f"Serial write error on {self.port}: {e}")
                    except Exception as e:
                        print(f"E3: {__file__}: {e}")

                # Check for communication timeout, this occurs if we have stopped receiving data after 5 seconds.
                if (datetime.now() - self.last_received_data > timedelta(seconds=COMMUNICATION_TIMEOUT)) and not self.stopped_communicating:
                    self.stopped_communicating = True
                    print(f"Stopped communicating with {self.port}")

                time.sleep(LOOP_PERIOD)

        except (serial.SerialException, OSError):
            # Expected if the port is disconnected; let the thread exit gracefully.
            pass

        finally:
            print(f"Serial Handler Stopped")


    ########### Messaging Methods ##########


    def appendMessage(self, msg):
        """
        Thread-safe callback. When the protocol parser receives a valid message, this method appends it to the UI message queue.

        Args:
            msg: The message to append.
        """
        self.event_loop.call_soon_threadsafe(self.ui_comms.message_queue.put_nowait, msg)


    def writeMessage(self, msg):
        """
        Transmits a message over the serial port using a thread-safe queue.

        Args:
            msg: The message to be transmitted.

        Returns:
            True if the message was queued for transmission, otherwise False.
        """
        # Do not transmit if the port is closed or communication has stopped.
        if self.serial_port and self.serial_port.is_open and not self.stopped_communicating:
            self.tx_queue.put(msg)
            return True
        else:
            print("Failed to write message: Port closed or communication stopped.")
            return False


    ########### Status Methods ##########


    def getConnectedPort(self):
        """
        Gets the currently connected port.

        Returns:
            Current connected port, else None.
        """
        return self.port


    def isCommunicating(self):
        """
        Returns whether serial is still communicating or not.

        Returns:
            True if communicating, false otherwise.
        """
        return not self.stopped_communicating