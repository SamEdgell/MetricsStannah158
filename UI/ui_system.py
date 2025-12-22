# Standard library imports.
from datetime import datetime

# Third party imports.
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from Enums.enum_system import RTC, SystemVersion
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours
from Utilities.messages import unpackMessage


class UISystem:
    """
    Class for handling all aspects of various system data.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        self.main_window.ui.requestSystemVersionButton.clicked.connect(self.requestSystemVersion)
        self.main_window.ui.setRTCButton.clicked.connect(self.setRTC)

        delegateVer = Painter()
        self.main_window.ui.sysVerTable.setItemDelegate(delegateVer)
        delegateTime = Painter()
        self.main_window.ui.timeTable.setItemDelegate(delegateTime)

        self.sysTimeTimer = QTimer()
        self.sysTimeTimer.timeout.connect(self.updateSysTime)
        self.sysTimeTimer.start(1000)

        self.setStyleSheetUISystem()
        self.populateSystemVersionTable()
        self.populateTimeTable()


    def setStyleSheetUISystem(self):
        """
        Sets the style sheet for the UISystem table.
        Only doing additional stuff to items here that would not work in QTCreator.
        """
        tables = [self.main_window.ui.sysVerTable, self.main_window.ui.timeTable]

        for table in tables:
            # Adjust the header and column widths.
            header = table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Fixed)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            # Once header is set, remove visibility, this is intended for these table.
            header.setVisible(False)

            table.setColumnWidth(0, 100)

            # Disable the built-in grid, will customise with the delegate class.
            table.setShowGrid(False)

            # Refine the style sheet.
            table.setStyleSheet(f"""
            QTableWidget {{
                border: 2px solid {Colours.BLACK.name()};
                background: {Colours.BEIGE.name()};
            }}
            """)


    def populateSystemVersionTable(self):
        """
        Populates the System version table with the variable ID's.
        """
        self.main_window.ui.sysVerTable.setRowCount(len(SystemVersion))
        row = 0

        # Setup each row.
        for _, var in enumerate(SystemVersion):
            # Column 0 is not editable.
            column0 = QTableWidgetItem(var.name)
            column0.setFlags(Qt.ItemIsEnabled)
            self.main_window.ui.sysVerTable.setItem(row, 0, column0)

            # Column 1 is not editable.
            column1 = QTableWidgetItem("")
            column1.setFlags(Qt.ItemIsEnabled)
            self.main_window.ui.sysVerTable.setItem(row, 1, column1)

            row += 1

        # Force additional settings to rows/columns after populated.
        for row in range(self.main_window.ui.sysVerTable.rowCount()):
            self.main_window.ui.sysVerTable.setRowHeight(row, 18)

            # Row colours.
            self.main_window.ui.sysVerTable.item(row, 0).setBackground(Colours.BEIGE)
            self.main_window.ui.sysVerTable.item(row, 1).setBackground(Colours.BEIGE)

            self.main_window.ui.sysVerTable.item(row, 0).setForeground(Colours.BLACK)
            self.main_window.ui.sysVerTable.item(row, 1).setForeground(Colours.BLACK)

            # Column alignment.
            for col in range(self.main_window.ui.sysVerTable.columnCount() - 1):
                alignment = Qt.AlignLeft if col == 0 else Qt.AlignHCenter
                alignment |= Qt.AlignVCenter
                self.main_window.ui.sysVerTable.item(row, col).setTextAlignment(alignment)

        # Resize the table to the content.
        self.resizeSystemTableToContent()


    def resizeSystemTableToContent(self):
        """
        Resizes the system table size to the total number of rows.
        Moves the bottom frame and the buttons (if exists) to positions based on the new table size.
        This does not adjust the position of the table, just the size.
        """
        # Table height
        table_row_count = self.main_window.ui.sysVerTable.rowCount()
        table_row_height = self.main_window.ui.sysVerTable.rowHeight(0)
        table_frame_width = self.main_window.ui.sysVerTable.frameWidth()
        table_total_height = (table_row_count * table_row_height) + (2 * table_frame_width)
        self.main_window.ui.sysVerTable.setFixedHeight(table_total_height)

        # Group box height
        pixel_gap = 18
        group_box_height = self.main_window.ui.sysVerTable.y() + table_total_height + pixel_gap
        self.main_window.ui.sysVerTable.parent().setFixedHeight(group_box_height)


    def populateTimeTable(self):
        """
        Populates the System time table with the variable ID's.
        """
        self.main_window.ui.timeTable.setRowCount(len(RTC))
        row = 0

        # Setup each row.
        for _, var in enumerate(RTC):
            # Column 0 is not editable.
            column0 = QTableWidgetItem(var.name)
            column0.setFlags(Qt.ItemIsEnabled)
            self.main_window.ui.timeTable.setItem(row, 0, column0)

            # Column 1 is not editable.
            column1 = QTableWidgetItem("")
            column1.setFlags(Qt.ItemIsEnabled)
            self.main_window.ui.timeTable.setItem(row, 1, column1)

            row += 1

        # Force additional settings to rows/columns after populated.
        for row in range(self.main_window.ui.timeTable.rowCount()):
            self.main_window.ui.timeTable.setRowHeight(row, 18)

            # Row colours.
            self.main_window.ui.timeTable.item(row, 0).setBackground(Colours.BEIGE)
            self.main_window.ui.timeTable.item(row, 1).setBackground(Colours.BEIGE)

            self.main_window.ui.timeTable.item(row, 0).setForeground(Colours.BLACK)
            self.main_window.ui.timeTable.item(row, 1).setForeground(Colours.BLACK)

            # Column alignment.
            for col in range(self.main_window.ui.timeTable.columnCount() - 1):
                alignment = Qt.AlignLeft if col == 0 else Qt.AlignHCenter
                alignment |= Qt.AlignVCenter
                self.main_window.ui.timeTable.item(row, col).setTextAlignment(alignment)

        # Resize the table to the content.
        self.resizeTimeTableToContent()


    def resizeTimeTableToContent(self):
        """
        Resizes the time table size to the total number of rows.
        Moves the bottom frame and the buttons (if exists) to positions based on the new table size.
        This does not adjust the position of the table, just the size.
        """
        # Table height.
        table_row_count = self.main_window.ui.timeTable.rowCount()
        table_row_height = self.main_window.ui.timeTable.rowHeight(0)
        table_frame_width = self.main_window.ui.timeTable.frameWidth()
        table_total_height = (table_row_count * table_row_height) + (2 * table_frame_width)
        self.main_window.ui.timeTable.setFixedHeight(table_total_height)

        # Define gaps.
        pixel_gap = 18

        # Calculate positions for the buttons.
        set_rtc_button_top = self.main_window.ui.timeTable.y() + table_total_height + pixel_gap
        set_rtc_button_bottom = set_rtc_button_top + self.main_window.ui.setRTCButton.height()

        # Total group box height is the sum of the table height, button height, and button gap.
        group_box_height = set_rtc_button_bottom + pixel_gap

        # Move buttons to their respective positions.
        self.main_window.ui.setRTCButton.move(self.main_window.ui.setRTCButton.x(), set_rtc_button_top)

        # Set the new group box height.
        self.main_window.ui.timeTable.parent().setFixedHeight(group_box_height)


    def requestSystemVersion(self):
        """
        Requests the system version from the system.
        """
        self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_VERSION, "", [], SrcDest.SRC_DEST_X01, MsgMode.GET)
        self.main_window.ui_comms.sendMessage(MessageID.SYSTEM_VERSION, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET)


    def updateSystemVersion(self, msg):
        """
        Handles new system version data.

        Args:
            msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                header, version_payload = unpackMessage("2BHB3B10B16", msg)

                version_string = f"{version_payload[0]}.{version_payload[1]}.{version_payload[2]}"
                version_suffix = "".join(map(chr, version_payload[3:6])).strip()
                product_id = "".join(chr(b) for b in version_payload[6:16] if b != 0).strip()
                serial_num = "".join(chr(b) for b in version_payload[16:32] if b != 0).strip()

                if SrcDest(header[2]) == SrcDest.SRC_DEST_X01:
                    self.main_window.ui.sysVerTable.item(0, 1).setText(version_string)
                    self.main_window.ui.sysVerTable.item(1, 1).setText(version_suffix)
                    self.main_window.ui.sysVerTable.item(2, 1).setText(product_id)
                    self.main_window.ui.sysVerTable.item(3, 1).setText(serial_num)
                elif SrcDest(header[2]) == SrcDest.SRC_DEST_X04:
                    self.main_window.ui.sysVerTable.item(4, 1).setText(version_string)
                    self.main_window.ui.sysVerTable.item(5, 1).setText(version_suffix)
                    self.main_window.ui.sysVerTable.item(6, 1).setText(product_id)
                    self.main_window.ui.sysVerTable.item(7, 1).setText(serial_num)

        except Exception as e:
            print(f"E1: {__file__}: {e}")


    def setRTC(self):
        """
        Sends a message to sync the RTC with PC. Value should be in UTC format.
        """
        now_unix = int(datetime.now().timestamp())
        self.main_window.ui_comms.sendMessage(MessageID.RTC_TIME, "I", [now_unix], SrcDest.SRC_DEST_X04, MsgMode.SET)


    def updateSysTime(self):
        """
        Updates the system time every second. Also requests for the ECU time.
        """
        self.main_window.ui_comms.sendMessage(MessageID.RTC_TIME, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET) # Request the ECU time
        system_datetime = datetime.now()
        system_unix = int(system_datetime.timestamp())
        system_datetime = system_datetime.strftime("%Y-%m-%d %H:%M:%S")
        self.main_window.ui.timeTable.item(0, 1).setText(f"{system_datetime}")
        self.main_window.ui.timeTable.item(1, 1).setText(f"{system_unix}")


    def updateECUTime(self, msg):
        """
        Updates the ECU time when requested.
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                _, rtc_payload = unpackMessage("I", msg)

                ecu_unix = rtc_payload[0]
                ecu_datetime = datetime.fromtimestamp(ecu_unix)
                ecu_datetime = ecu_datetime.strftime("%Y-%m-%d %H:%M:%S")
                self.main_window.ui.timeTable.item(2, 1).setText(f"{ecu_datetime}")
                self.main_window.ui.timeTable.item(3, 1).setText(f"{ecu_unix}")

        except Exception as e:
            print(f"E2: {__file__}: {e}")