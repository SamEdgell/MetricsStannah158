# Third party imports.
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QComboBox, QHeaderView, QListView, QTableWidgetItem

# Local application imports.
from Enums.enum_ecodes import ECodes
from Enums.enum_errors import ErrorType
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from Enums.enum_system import AssertData, OperationalMode, SystemData, SystemState, UpDirection
from UI.ui_custom_widgets import NoFocus, Painter
from UI.ui_styling import Colours
from Utilities.messages import unpackMessage, unpackMessagePayload


class UIMisc:
    """
    Class for handling all aspects of miscellaneous data.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        self.main_window.ui.setOpModeButton.clicked.connect(self.setOpMode)
        self.main_window.ui.clearFaultButton.clicked.connect(lambda: self.main_window.ui_comms.sendMessage(MessageID.CLEAR_UNRECOVERABLE_FAULT, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ))
        self.main_window.ui.clearAssertButton.clicked.connect(self.clearAssertTable)
        delegateMisc = Painter()
        self.main_window.ui.miscTable.setItemDelegate(delegateMisc)

        delegateAssert = Painter()
        self.main_window.ui.assertTable.setItemDelegate(delegateAssert)

        self.miscTimer = QTimer()
        self.miscTimer.timeout.connect(self.requestMiscData)
        self.miscTimer.start(1000)

        self.setStyleSheetUIMisc()
        self.populateMiscTable()
        self.populateAssertTable()
        self.populateOpModeBox()


    def setStyleSheetUIMisc(self):
        """
        Sets the style sheet for the UISystem table.
        Only doing additional stuff to items here that would not work in QTCreator.
        """
        tables = [self.main_window.ui.miscTable, self.main_window.ui.assertTable]

        for table in tables:
            # Adjust the header and column widths.
            header = table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Fixed)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            # Once header is set, remove visibility, this is intended for this table.
            header.setVisible(False)

            if table == self.main_window.ui.miscTable:
                table.setColumnWidth(0, 90)
            else:
                table.setColumnWidth(0, 50)

            # Disable the built-in grid, will customise with the delegate class.
            table.setShowGrid(False)

            # Refine the style sheet.
            table.setStyleSheet(f"""
            QTableWidget {{
                border: 2px solid {Colours.BLACK.name()};
                background: {Colours.BEIGE.name()};
            }}
            """)

        # Set the op mode box style sheet.
        self.main_window.ui.opModeBox.setMaxVisibleItems(10)
        list_view = QListView(self.main_window.ui.opModeBox)
        list_view.setAttribute(Qt.WA_StyledBackground, True) # Force the background to be painted from the style sheet.

        font = QFont()
        font.setPointSize(8)
        list_view.setFont(font)

        list_view.setStyleSheet(f"""
                                QListView,
                                QAbstractItemView{{
                                    color: {Colours.BLACK.name()};             /* Text colour */
                                    background: {Colours.WHITE.name()};        /* Background colour */
                                    border: 1px solid {Colours.BLACK.name()};  /* Border colour */
                                }}
                                QListView::item{{
                                    padding: 4px 8px;           /* Item padding */
                                    min-height: 15px;           /* Minimum item height */
                                    font-size: 10px;            /* Font size */
                                }}
                                QListView::item:hover,
                                QListView::item:selected{{
                                    color: {Colours.BLACK.name()};             /* Text colour */
                                    background: {Colours.PALE_GREEN.name()};   /* Background colour */
                                }}
                                """)
        list_view.setItemDelegate(NoFocus(list_view)) # Prevent focus rectangle around items in the drop down boxes.
        self.main_window.ui.opModeBox.setView(list_view)


    def populateMiscTable(self):
        """
        Populates the misc table with the variable ID's.
        """
        self.main_window.ui.miscTable.setRowCount(len(SystemData))

        # Setup each row.
        for row, var in enumerate(SystemData):
            # Column 0 is not editable.
            column0 = QTableWidgetItem(var.name)
            column0.setFlags(Qt.ItemIsEnabled)
            column0.setBackground(Colours.BEIGE)
            column0.setForeground(Colours.BLACK)
            column0.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.main_window.ui.miscTable.setItem(row, 0, column0)

            # Column 1 is not editable.
            column1 = QTableWidgetItem("")
            column1.setFlags(Qt.ItemIsEnabled)
            column1.setBackground(Colours.BEIGE)
            column1.setForeground(Colours.BLACK)
            column1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.main_window.ui.miscTable.setItem(row, 1, column1)

            self.main_window.ui.miscTable.setRowHeight(row, 18)

        # Resize the table to the content.
        self.resizeTableToContent(self.main_window.ui.miscTable)


    def populateAssertTable(self):
        """
        Populates the assert table with the variable ID's.
        """
        self.main_window.ui.assertTable.setRowCount(len(AssertData))

        # Setup each row.
        for row, var in enumerate(AssertData):
            # Column 0 is not editable.
            column0 = QTableWidgetItem(var.name)
            column0.setFlags(Qt.ItemIsEnabled)
            column0.setBackground(Colours.BEIGE)
            column0.setForeground(Colours.BLACK)
            column0.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.main_window.ui.assertTable.setItem(row, 0, column0)

            # Column 1 is not editable.
            column1 = QTableWidgetItem("")
            column1.setFlags(Qt.ItemIsEnabled)
            column1.setBackground(Colours.BEIGE)
            column1.setForeground(Colours.BLACK)
            column1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.main_window.ui.assertTable.setItem(row, 1, column1)

            self.main_window.ui.assertTable.setRowHeight(row, 18)

        # Resize the table to the content.
        self.resizeTableToContent(self.main_window.ui.assertTable)


    def resizeTableToContent(self, table):
        """
        Resizes the default table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons (if exists) to positions based on the new table size.

        @param table: The table to resize.
        """
        table_row_count = table.rowCount()
        table_row_height = table.rowHeight(0)
        table_frame_width = table.frameWidth()
        table_total_height = (table_row_count * table_row_height) + (2 * table_frame_width)
        table.setFixedHeight(table_total_height)


    def populateOpModeBox(self):
        """
        Populates the operational mode combo box with the operational modes.
        """
        self.main_window.ui.opModeBox.clear()

        for i, var in enumerate(OperationalMode):
            self.main_window.ui.opModeBox.addItem(var.name)
            self.main_window.ui.opModeBox.setItemData(i, int(Qt.AlignCenter), Qt.TextAlignmentRole)

        self.main_window.ui.opModeBox.setCurrentIndex(0)


    def setOpMode(self):
        """
        Requests to change the operational mode.
        """
        # Get the selected index from the combo box.
        selected_index = self.main_window.ui.opModeBox.currentIndex()

        # Get the selected operational mode.
        if selected_index < 0:
            print("Error: No operational mode selected.")
            return

        selected_op_mode = OperationalMode(selected_index).value

        self.main_window.ui_config.setATEMode(selected_op_mode == OperationalMode.ATE.value)

        # Send the request to change the operational mode.
        self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_OP_MODE, "B", [selected_op_mode], SrcDest.SRC_DEST_X01, MsgMode.SET)
        self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_OP_MODE, "B", [selected_op_mode], SrcDest.SRC_DEST_X04, MsgMode.SET)


    def requestMiscData(self):
        """
        Request misc data every 1 second if we are authenticated.
        """
        if self.main_window.ui_authentication.isAuthenticated():
            self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_STATE, "", [], SrcDest.SRC_DEST_X01, MsgMode.GET)
            self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_STATE, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET)
            self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_CONFIGURATION, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET)
            self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_OP_MODE, "", [], SrcDest.SRC_DEST_X01, MsgMode.GET)
            self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_OP_MODE, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET)


    def updateSystemState(self, msg):
        """
        Handles new system state data.

        @param msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                header, system_state_payload = unpackMessage("B", msg)
                system_state = SystemState(system_state_payload[0]).name

                if SrcDest(header[2]) == SrcDest.SRC_DEST_X01:
                    self.main_window.ui.miscTable.item(0, 1).setText(str(system_state))
                elif SrcDest(header[2]) == SrcDest.SRC_DEST_X04:
                    self.main_window.ui.miscTable.item(1, 1).setText(str(system_state))

        except Exception as e:
            print(f"E1: {__file__}: {e}")


    def updateSystemConfiguration(self, msg):
        """
        Handles new system configuration data.

        @param msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                header, sys_config_payload = unpackMessage("2B", msg)
                handing = UpDirection(sys_config_payload[0]).name

                if SrcDest(header[2]) == SrcDest.SRC_DEST_X04:
                    self.main_window.ui.miscTable.item(4, 1).setText(handing)

        except Exception as e:
            print(f"E2: {__file__}: {e}")


    def updateSystemOpMode(self, msg):
        """
        Handles new system op mode data.

        @param msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                header, op_mode_payload = unpackMessage("B", msg)
                opMode = OperationalMode(op_mode_payload[0]).name

                if SrcDest(header[2]) == SrcDest.SRC_DEST_X01:
                    self.main_window.ui.miscTable.item(2, 1).setText(str(opMode))
                elif SrcDest(header[2]) == SrcDest.SRC_DEST_X04:
                    self.main_window.ui.miscTable.item(3, 1).setText(str(opMode))

        except Exception as e:
            print(f"E3: {__file__}: {e}")


    def updateECodeChanged(self, msg):
        """
        Handles new E-code changed data.

        @param msg: The message to unpack.
        """
        if 0:
            # This is purely for displaying values on the hex display.
            e_code = 0x1015
            digit0 = (e_code & 0xF000) >> 12
            digit1 = (e_code & 0x0F00) >> 8
            digit2 = (e_code & 0x00F0) >> 4
            digit3 = e_code & 0x000F

            self.main_window.ui.hexDigit0.display(digit0)
            self.main_window.ui.hexDigit1.display(digit1)
            self.main_window.ui.hexDigit2.display(digit2)
            self.main_window.ui.hexDigit3.display(digit3)
            return
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                payload = unpackMessagePayload("H", msg)

                # Convert e_code to an integer.
                e_code = int.from_bytes(payload[0].to_bytes(2, byteorder='big'), byteorder='big')

                # Convert e_code to a hexadecimal string for the hex display
                digit0 = (e_code & 0xF000) >> 12
                digit1 = (e_code & 0x0F00) >> 8
                digit2 = (e_code & 0x00F0) >> 4
                digit3 = e_code & 0x000F

                self.main_window.ui.hexDigit0.display(digit0)
                self.main_window.ui.hexDigit1.display(digit1)
                self.main_window.ui.hexDigit2.display(digit2)
                self.main_window.ui.hexDigit3.display(digit3)

                # Update the E-code line edit with the new value.
                e_code_str = ECodes(e_code).name
                self.main_window.ui.eCodeLineEdit.setText(e_code_str)
        except Exception as e:
            print(f"E4: {__file__}: {e}")


    def updateAssert(self, msg):
        """
        Handles the assert data.

        @param msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                header, payload = unpackMessage("HH120s", msg)

                try:
                    # Try to find the first null terminator.
                    nullIndex = payload[2].index(b'\0')

                    # Decode the filename from bytes into string, up to the null terminator.
                    filename = payload[2][:nullIndex].decode('utf-8', errors='ignore')
                except ValueError:
                    # If no null terminator is found, decode the entire payload.
                    filename = payload[2].decode('utf-8', errors='ignore')

                # Strip the path and get the filename only.
                lastSlash = filename.rfind('/')
                if lastSlash == -1:
                    lastSlash = filename.rfind('\\')

                if lastSlash >= 0:
                    filename = filename[lastSlash + 1:]

                self.main_window.ui.assertTable.item(0, 1).setText(filename)
                self.main_window.ui.assertTable.item(1, 1).setText(f"{ErrorType(payload[0]).name}")
                self.main_window.ui.assertTable.item(2, 1).setText(f"{payload[1]}")
                self.main_window.ui.assertTable.item(3, 1).setText(f"{SrcDest(header[2]).name}")
        except Exception as e:
            print(f"E5: {__file__}: {e}")


    def clearAssertTable(self):
        """
        Clears the assert table on request.
        """
        for i in range(self.main_window.ui.assertTable.rowCount()):
            self.main_window.ui.assertTable.item(i, 1).setText("")