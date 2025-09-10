from PySide6 import QtCore


class SignalSlot(QtCore.QObject):
    """
    Class for setting up a signal-slot mechanism to send data to the GUI in a thread-safe manner.
    Inherits from QtCore.QObject to enable the use of Qt's signal and slot system, allowing safe communication between threads and the GUI.
    This enables thread-safe updates to the user interface from worker threads.
    Defines custom signals for passing port information, console messages, byte counts, and status updates.
    """
    com_port_signal           = QtCore.Signal(list) # Called by PortHandler to pass port information.
    primary_console_signal    = QtCore.Signal(str)  # Called by Metrics to pass string to primary console.
    rx_bytes_signal           = QtCore.Signal(int)  # Called by SerialHandler to pass RX byte count.
    secondary_console_signal  = QtCore.Signal(str)  # Called by Metrics to pass string to secondary console.
    status_signal             = QtCore.Signal(bool) # Called by PortHandler to pass port status.
    tx_bytes_signal           = QtCore.Signal(int)  # Called by SerialHandler to pass TX byte count.
