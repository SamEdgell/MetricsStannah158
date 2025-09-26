# Third party imports.
from PySide6.QtCore import QObject, Signal


class SignalSlot(QObject):
    """
    Class for setting up a signal-slot mechanism to send data to the GUI in a thread-safe manner.
    Inherits from QObject to enable the use of Qt's signal and slot system, allowing safe communication between threads and the GUI.
    This enables thread-safe updates to the user interface from worker threads.
    Defines custom signals for passing port information, console messages, byte counts, and status updates.
    """
    com_port_signal           = Signal(list) # Called by PortHandler to pass port information.
    primary_console_signal    = Signal(str)  # Called by Metrics to pass string to primary console.
    rx_bytes_signal           = Signal(int)  # Called by SerialHandler to pass RX byte count.
    secondary_console_signal  = Signal(str)  # Called by Metrics to pass string to secondary console.
    status_signal             = Signal(bool) # Called by PortHandler to pass port status.
    tx_bytes_signal           = Signal(int)  # Called by SerialHandler to pass TX byte count.
