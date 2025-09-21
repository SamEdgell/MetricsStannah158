# Standard library imports.
import threading
import time

# Third party imports.
import serial.tools.list_ports

# Local application imports.
from Serial.serial_handler import SerialHandler


LOOP_TIMEOUT        = 0.5     # Time to wait between port checks in seconds.
THREAD_JOIN_TIMEOUT = 2.0     # Timeout for joining the port handler thread in seconds.


class PortHandler:
    """
    Handles detection, connection, and management of COM port devices. Manages auto and manual connection modes, scans for recognised devices, and coordinates the serial handler for communication.
    """

    def __init__(self, ui_comms, event_loop):
        """
        Initialises the PortHandler class.

        Args:
            ui_comms:    UIComms instance, allowing PortHandler to send its required data to the UIComms class in a thread-safe way.
            event_loop:  Reference to the main thread's asyncio event loop. This is required to safely schedule function calls from this background thread back to the main async thread, for example, to add a received message to an asyncio.Queue.
        """
        print(f"Port Handler Started")
        self.ui_comms           = ui_comms
        self.event_loop         = event_loop
        self.discovered_ports   = set()
        self.recognised_ports   = set()
        self.port_connected     = False
        self.serial_handler     = None   # Initialise with None to avoid errors if the UI is closed without connecting to a port.
        self.auto_connect       = True   # Script auto connects by default. If changing, remember to uncheck the radio button in the UI.
        self.prepare_for_quit   = False  # If True, do not allow the port handler to open any more identified ports.
        self.lock               = threading.Lock() # Protects access to shared resources when switching connection mode.
        self.recognised_devices = [
                                    "0483:5740", # STM32F439ZI
                                    "1FC9:0094"  # NXP RT1021
                                    ]


    ########### Thread Management ##########


    def runPortHandler(self):
        """
        Continuously runs the port handler thread.
        """
        while self.port_event.is_set():
            try:
                # Check all available ports.
                current_ports = {p.device for p in serial.tools.list_ports.comports()}

                # Lock resources to prevent switching connection mode while this code is executing.
                with self.lock:
                    self.discovered_ports = current_ports
                    if self.auto_connect:
                        self.handleAutoConnect()
                    else:
                        self.handleManualConnect()

                connected_port = self.serial_handler.getConnectedPort() if self.serial_handler is not None else None # There is no connected port if the serial handler is None.
                self.ui_comms.signal_slot.com_port_signal.emit([list(self.discovered_ports), connected_port])

                time.sleep(LOOP_TIMEOUT)
            except Exception as e:
                print(f"E1: {__file__}: {e}")


    def start(self):
        """
        Starts the port handler thread.
        """
        self.port_thread = threading.Thread(target=self.runPortHandler)
        self.port_event = threading.Event()
        self.port_event.set()
        self.port_thread.start()


    def stop(self):
        """
        Stops the port handler thread.
        """
        self.prepare_for_quit = True
        with self.lock:
            self.close()
        self.port_event.clear()
        self.port_thread.join(timeout=THREAD_JOIN_TIMEOUT)
        print(f"Port Handler Stopped")


    ########### Port Management Methods ##########


    def close(self):
        """
        Attempts to close the connected port and serial handler.
        """
        # Cannot close a port if none is connected.
        if not self.connected():
            return

        if self.serial_handler:
            self.serial_handler.disconnect()
            self.serial_handler = None

        self.port_connected = False
        self.ui_comms.signal_slot.status_signal.emit(self.connected())


    def handleAutoConnect(self):
        """
        Handles automatic connection to a recognised port.
        """
        self.scanPorts()

        # If we have recognised ports, try to connect to the first one.
        if self.recognised_ports:
            # We should only connect to the port if we are not already connected and we are not in demo mode.
            if not self.connected() and not self.ui_comms.inDemoMode():
                port_to_connect = next(iter(self.recognised_ports))
                self.open(port_to_connect)
        # If we have no recognised ports, ensure we are disconnected.
        elif self.connected():
            self.close()


    def handleManualConnect(self):
        """
        Handles manual connection to a port.
        """
        # If we are connected, but the port has physically disappeared, and serial handler is active, close the connection.
        if self.connected() and self.serial_handler is not None:
            if self.serial_handler.getConnectedPort() not in self.discovered_ports:
                self.close()


    def open(self, port):
        """
        Attempts to open the requested port and connect the serial handler, only if there is not already a port connected.

        Args:
            port: The requested port to connect to.
        """
        # Do not attempt to open the port if a port is already connected or we are preparing to close the application.
        if self.connected() or self.prepare_for_quit:
            return

        try:
            # Pass the UIComms instance so that the SignalSlot can be set up.
            # A reference to the event loop is also required to read messages from the queue.
            self.serial_handler = SerialHandler(port,
                                                int(self.ui_comms.main_window.ui.baudRateBox.currentText()),
                                                self.ui_comms,
                                                self.event_loop)
            if self.serial_handler.connect():
                self.port_connected = True
                print(f"Connected to {port}")
            else:
                self.serial_handler = None  # Clean up failed connection.
        except Exception as e:
            print(f"E2: {__file__}: {e}")
            self.serial_handler = None

        self.ui_comms.signal_slot.status_signal.emit(self.connected())


    def setAutoConnect(self):
        """
        Sets the port handler to auto connection mode. Closes any existing connection before switching mode.
        """
        with self.lock:
            self.auto_connect = True
            self.close()


    def setManualConnect(self):
        """
        Sets the port handler to manual connection mode. Only disconnects if transitioning from auto to manual mode.
        """
        with self.lock:
            # Only disconnect if transitioning from auto to manual.
            if self.auto_connect:
                self.close()
            self.auto_connect = False


    ########### Status Methods ##########


    def connected(self):
        """
        Returns whether a port is currently connected.

        Returns:
            True if the port is connected, otherwise False.
        """
        return self.port_connected


    ########### Port Discovery Methods ##########


    def refreshPorts(self):
        """
        Refreshes the available COM ports and emits the updated list. This should be called when changing from auto to manual mode to prevent a stale list of COM ports.
        """
        # Scan for ports and emit the updated list to the UI.
        current_ports = {p.device for p in serial.tools.list_ports.comports()}
        with self.lock:
            self.discovered_ports = current_ports
            self.scanPorts()
        connected_port = self.serial_handler.getConnectedPort() if self.serial_handler is not None else None # There is no connected port if the serial handler is None.
        self.ui_comms.signal_slot.com_port_signal.emit([list(self.discovered_ports), connected_port])


    def scanPorts(self):
        """
        Scans the available COM ports and updates the set of recognised devices. Adds newly recognised devices and removes any recognised ports that have been disconnected.
        """
        # Clear recognised ports to ensure a fresh set each scan.
        self.recognised_ports.clear()

        # Find and add newly recognised devices.
        for port in serial.tools.list_ports.comports():
            if any(dev in port.hwid for dev in self.recognised_devices):
                self.recognised_ports.add(port.device)