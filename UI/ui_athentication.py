# Standard library imports.
from datetime import datetime

# Local application imports.
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from UI.ui_styling import Colours, CSS
from Utilities.messages import unpackMessage


class UIAuthentication:
    """
    Handles the authentication logic.
    """
    def __init__(self, main_window):
        """
        Initialises the UIComms class.

        Args:
            main_window:    Reference to the main window, used for accessing UI elements.
        """
        self.main_window = main_window

        # Connect UI elements to their handlers.
        self.main_window.ui.authenticateButton.toggled.connect(self.handleAuthenticateButton)

        # Set the desired initial authentication state.
        self.auth_required = False
        self.authenticated = False

        # Update the authentication button state but do not call the handler.
        self.main_window.ui.authenticateButton.blockSignals(True)
        self.main_window.ui.authenticateButton.setChecked(self.auth_required)
        self.main_window.ui.authenticateButton.blockSignals(False)

        self.updateAuthenticationStatus(self.authenticated)


    def authRequired(self):
        """
        Returns whether authentication is required.

        Returns:
            True if authentication is required, False otherwise.
        """
        return self.auth_required


    def calcAuth(self, auth_val):
        """
        Calculates the authentication key.

        Args:
            auth_val: The authorisation value.

        Returns:
            The calculated authentication key as an integer.
        """
        auth_val_calc = (auth_val ^ 0x5355505244415645) % 0x200052C8 # PC
        return auth_val_calc


    def handleAuthenticateButton(self):
        """
        Enables or disables the need for authentication based on the button click.
        """
        self.auth_required = self.main_window.ui.authenticateButton.isChecked()

        if self.auth_required and self.main_window.ui_comms.serial_port_handler.connected():
            self.sendHandshake()

        self.updateAuthenticationStatus(self.authenticated)


    def isAuthenticated(self):
        """
        Returns whether the device is authenticated.

        Returns:
            True if authenticated, False otherwise.
        """
        return self.authenticated


    def processAuthentication(self, msg):
        """
        Called when an authentication message is received.

        Args:
            msg: The authentication message.
        """
        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: {Colours.GARNET.name()};{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Received authentication{CSS.END_STYLE}")

        status_msg = ""

        match MsgMode(msg[5]): # Note, mode is the 5th element as it's not unpacked yet.
            case MsgMode.NACK:
                status_msg = "Authentication NACK received"
            case MsgMode.REQ_ACK:
                status_msg = "Authentication REQ_ACK received"
            case MsgMode.SET_ACK:
                status_msg = "Authentication SET_ACK received"
                self.setAuthentication(True)
            case _:
                status_msg = "Authentication Unknown"

        if status_msg:
            self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: {Colours.GARNET.name()};{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - {status_msg}{CSS.END_STYLE}")

        # If we are authenticated, a heartbeat is immediately sent to the processor.
        if self.authenticated:
            self.main_window.ui_panel.heartbeatReceived() # Needs to be updated again once authenticated. If not, the original time at initialisation is taken and a timeout occurs.
            self.main_window.ui_panel.sendHeartbeat()
            self.main_window.ui_panel.startLEDHeartbeatTimer() # The LED heartbeat timer can now be started.


    def processHandshake(self, msg):
        """
        Called when a handshake message is received.

        Args:
            msg: The handshake message.
        """
        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: {Colours.GARNET.name()};{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Received handshake{CSS.END_STYLE}")

        match MsgMode(msg[5]): # Note, mode is the 5th element as it's not unpacked yet.
            case MsgMode.NACK:
                status_msg = "Handshake NACK received"
            case MsgMode.REQ_ACK:
                status_msg = "Handshake REQ_ACK received"
            case MsgMode.SET_ACK:
                status_msg = "Handshake SET_ACK received"
            case _:
                _, payload = unpackMessage("Q", msg)
                auth_val = payload[0]
                self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: {Colours.GARNET.name()};{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Auth Value: {auth_val}{CSS.END_STYLE}")
                auth_calc = self.calcAuth(auth_val)
                self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: {Colours.GARNET.name()};{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - Auth Calc: {auth_calc}{CSS.END_STYLE}")
                if self.main_window.ui_comms.sendMessage(MessageID.AUTHENTICATE, "Q", [auth_calc], SrcDest.SRC_DEST_ECU1, MsgMode.SET):
                    status_msg = "Sending authentication"

        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: {Colours.GARNET.name()};{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - {status_msg}{CSS.END_STYLE}")


    def sendHandshake(self):
        """
        Sends a handshake in an attempt to authenticate with the device.
        """
        if self.main_window.ui_comms.sendMessage(MessageID.HANDSHAKE, "BBB", [SrcDest.SRC_DEST_PC.value, 1, 0], SrcDest.SRC_DEST_ECU1, MsgMode.SET):
            status_msg = "Sending handshake"
        else:
            status_msg = "Unable to send handshake"

        self.main_window.ui_console.logPrimaryConsole(f"{CSS.START_STYLE}color: {Colours.GARNET.name()};{CSS.START_STYLE_END}{datetime.now().strftime('%H:%M:%S.%f')[:-3]} - {status_msg}{CSS.END_STYLE}")


    def setAuthentication(self, authenticated):
        """
        Sets the authentication status.

        Args:
            authenticated: True if authenticated, False otherwise.
        """
        self.authenticated = authenticated
        self.updateAuthenticationStatus(self.authenticated)


    def updateAuthenticationStatus(self, authenticated):
        """
        Updates the authentication status text box.

        Args:
            authenticated: True if authenticated, False otherwise.
        """
        if not self.auth_required:
            self.main_window.ui.authenticateLineEdit.setStyleSheet(f"""
                                                                    color: {Colours.BLACK.name()};                       /* Text colour */
                                                                    background-color: {Colours.CANARY_YELLOW.name()};    /* Background colour */
                                                                    border: 1px solid {Colours.BLACK.name()};            /* Thin black solid border */
                                                                    border-radius: 5px;                                  /* Optional: rounded corners */
                                                                    padding: 5px;                                        /* Adds space around the text */
                                                                    padding-top: 3px;                                    /* Adjusts the padding at the top */
                                                                    padding-bottom: 3px;                                 /* Adjusts the padding at the bottom */
                                                                    line-height: 20px;                                   /* Ensures proper vertical alignment of text */
                                                                """)
            self.main_window.ui.authenticateLineEdit.setText("Not Required")
        else:
            if authenticated:
                self.main_window.ui.authenticateLineEdit.setStyleSheet(f"""
                                                                        color: {Colours.BLACK.name()};                  /* Text colour */
                                                                        background-color: {Colours.PALE_GREEN.name()};  /* Background colour */
                                                                        border: 1px solid {Colours.BLACK.name()};       /* Thin black solid border */
                                                                        border-radius: 5px;                             /* Optional: rounded corners */
                                                                        padding: 5px;                                   /* Adds space around the text */
                                                                        padding-top: 3px;                               /* Adjusts the padding at the top */
                                                                        padding-bottom: 3px;                            /* Adjusts the padding at the bottom */
                                                                        line-height: 20px;                              /* Ensures proper vertical alignment of text */
                                                                    """)
                self.main_window.ui.authenticateLineEdit.setText("Authenticated")
            else:
                self.main_window.ui.authenticateLineEdit.setStyleSheet(f"""
                                                                        color: {Colours.BLACK.name()};                  /* Text colour */
                                                                        background-color: {Colours.LIGHT_PINK.name()};  /* Background colour */
                                                                        border: 1px solid {Colours.BLACK.name()};       /* Thin black solid border */
                                                                        border-radius: 5px;                             /* Optional: rounded corners */
                                                                        padding: 5px;                                   /* Adds space around the text */
                                                                        padding-top: 3px;                               /* Adjusts the padding at the top */
                                                                        padding-bottom: 3px;                            /* Adjusts the padding at the bottom */
                                                                        line-height: 20px;                              /* Ensures proper vertical alignment of text */
                                                                    """)
                self.main_window.ui.authenticateLineEdit.setText("Not Authenticated")