# Third party imports.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_high_speed import HighSpeedSources
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from Enums.enum_position import ChairPositionData, ChairPositions, FootrestPositionData, FootrestPositions, MainPositionData, SwivelPositionData, SwivelPositions
from Enums.enum_system_drives import SystemDrive
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours
from Utilities.messages import unpackMessagePartial, unpackMessagePayload


class UIDrivePosition:
    """
    Class for handling all aspects of drive position data.
    """
    def __init__(self, main_windows):
        # Store reference to the main window to access UI elements.
        self.main_window = main_windows

        self.main_window.ui.requestChairPositionButton.clicked.connect(lambda:       self.requestHSPosition("Chair"))
        self.main_window.ui.requestFootrestPositionButton.clicked.connect(lambda:    self.requestHSPosition("Footrest"))
        self.main_window.ui.requestMainPositionButton.clicked.connect(lambda:        self.requestHSPosition("Main"))
        self.main_window.ui.requestSwivelPositionButton.clicked.connect(lambda:      self.requestHSPosition("Swivel"))


        delegateChair = Painter()
        self.main_window.ui.chairDrivePositionTable.setItemDelegate(delegateChair)

        delegateFootrest = Painter()
        self.main_window.ui.footrestDrivePositionTable.setItemDelegate(delegateFootrest)

        delegateMain = Painter()
        self.main_window.ui.mainDrivePositionTable.setItemDelegate(delegateMain)

        delegateSwivel = Painter()
        self.main_window.ui.swivelDrivePositionTable.setItemDelegate(delegateSwivel)

        self.setStyleSheetUIDrivePos()
        self.populatePositionTables()


    """
    Sets the style sheet for the UIDrivePosition tables.
    Only doing additional stuff to items here that would not work in QTCreator.
    """
    def setStyleSheetUIDrivePos(self):
        tables = [self.main_window.ui.chairDrivePositionTable, self.main_window.ui.footrestDrivePositionTable,
                  self.main_window.ui.mainDrivePositionTable, self.main_window.ui.swivelDrivePositionTable]

        for table in tables:
            header = table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Fixed)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setFixedHeight(20)
            # Once header is set, remove visibility, this is intended for these tables.
            header.setVisible(False)

            table.setColumnWidth(0, 90)

            # Disable the built-in grid, will customise with the delegate class.
            table.setShowGrid(False)

            # Refine the style sheet. Focusing really on the header.
            table.setStyleSheet(f"""
            QTableWidget {{
                border: 2px solid {Colours.BLACK.name()};           /* Border of the table */
                background: {Colours.BEIGE.name()};                 /* Background colour of table */
            }}
            QHeaderView::section {{
                background-color: {Colours.ICTERINE.name()};        /* Background colour of the header */
                border: none;                                       /* Border of the header */
                border-right: 1px solid {Colours.BLACK.name()};     /* Right border of the header. Splits columns visually */
                border-bottom: 2px solid {Colours.BLACK.name()};    /* Bottom border of the header */
                color: {Colours.BLACK.name()};                      /* Text colour of the header */
                font-weight: normal;                                /* Font weight of the header text */
            }}
            QHeaderView::section:last {{
                border-right: none;                 /* Remove the right border from the last header section. This is because of an overlap with the table widget border */
            }}
            """)


    """
    Populates the Position table with the variable ID's.
    """
    def populatePositionTables(self):
        tables = [self.main_window.ui.chairDrivePositionTable, self.main_window.ui.footrestDrivePositionTable,
                  self.main_window.ui.mainDrivePositionTable, self.main_window.ui.swivelDrivePositionTable]

        for table in tables:
            row = 0

            if table == self.main_window.ui.chairDrivePositionTable:
                table.setRowCount(len(ChairPositionData))
                enum = ChairPositionData
            elif table == self.main_window.ui.footrestDrivePositionTable:
                table.setRowCount(len(FootrestPositionData))
                enum = FootrestPositionData
            elif table == self.main_window.ui.mainDrivePositionTable:
                table.setRowCount(len(MainPositionData))
                enum = MainPositionData
            else:
                table.setRowCount(len(SwivelPositionData))
                enum = SwivelPositionData

            # Setup each row.
            for _, var in enumerate(enum):
                # Column 0 is not editable.
                column0 = QTableWidgetItem(var.name)
                column0.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, 0, column0)

                # Column 1 is not editable.
                column1 = QTableWidgetItem("")
                column1.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, 1, column1)

                row += 1

            # Force additional settings to rows/columns after populated.
            for row in range(table.rowCount()):
                table.setRowHeight(row, 18)

                # Row colours.
                table.item(row, 0).setBackground(Colours.BEIGE)
                table.item(row, 1).setBackground(Colours.BEIGE)

                table.item(row, 0).setForeground(Colours.BLACK)
                table.item(row, 1).setForeground(Colours.BLACK)

                # Column alignment.
                for col in range(table.columnCount()):
                    alignment = Qt.AlignLeft if col == 0 else Qt.AlignHCenter
                    alignment |= Qt.AlignVCenter
                    table.item(row, col).setTextAlignment(alignment)

        # Resize the table to the content.
        self.resizePositionTableToContent()


    """
    Resizes the default table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons to positions based on the new table size.
    """
    def resizePositionTableToContent(self):
        tables = [self.main_window.ui.chairDrivePositionTable, self.main_window.ui.footrestDrivePositionTable,
                  self.main_window.ui.mainDrivePositionTable, self.main_window.ui.swivelDrivePositionTable]

        for table in tables:
            # Table height
            table_row_count = table.rowCount()
            table_row_height = table.rowHeight(0)
            table_frame_width = table.frameWidth()
            table_total_height = (table_row_count * table_row_height) + (2 * table_frame_width)
            table.setFixedHeight(table_total_height)

            # Group box height
            pixel_gap = 18
            group_box_height = table.y() + table_total_height + pixel_gap
            table.parent().setFixedHeight(group_box_height)


    """
    Sends the request to enable/disable high speed position data for the selected drive.

    @param drive: The drive to enable/disable position data for.
    """
    def requestHSPosition(self, drive):
        if drive == "Chair":
            high_speed_source = HighSpeedSources.CHAIR_FOLD_POS.value
            src_dest = SrcDest.SRC_DEST_X01
        elif drive == "Footrest":
            high_speed_source = HighSpeedSources.FOOTREST_POS.value
            src_dest = SrcDest.SRC_DEST_X04
        elif drive == "Main":
            high_speed_source = HighSpeedSources.MAIN_DRIVE_ENCODER.value
            src_dest = SrcDest.SRC_DEST_X04
        elif drive == "Swivel":
            high_speed_source = HighSpeedSources.SWIVEL_POS.value
            src_dest = SrcDest.SRC_DEST_X01
        else:
            print(f"E1: {__file__} - {drive}")
            return

        self.main_window.ui_comms.sendMessage(MessageID.HS_LOGGING_ENABLE, "BB", [high_speed_source, True], src_dest, MsgMode.SET)


    """
    Handles new drive position data for a specific drive.

    @param msg: The message to unpack.
    """
    def updateDrivePositionTable(self, msg):
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                # Only interested in the drive ID first to see how much we need to unpack the full payload to.
                _, drive_id = unpackMessagePartial("B", msg)

                if SystemDrive(drive_id[0]) == SystemDrive.SYS_DRIVE_CHAIR_FOLD:
                    position_data = unpackMessagePayload("B5iI", msg)
                    drive_name = "chair"
                elif SystemDrive(drive_id[0]) == SystemDrive.SYS_DRIVE_FOOTREST:
                    position_data = unpackMessagePayload("B4iI", msg)
                    drive_name = "footrest"
                elif SystemDrive(drive_id[0]) == SystemDrive.SYS_DRIVE_MAIN_DRIVE:
                    position_data = unpackMessagePayload("B2iB", msg)
                    drive_name = "main"
                    position_data = position_data[:-1] # Do not want the last element from this message.
                elif SystemDrive(drive_id[0]) == SystemDrive.SYS_DRIVE_SWIVEL:
                    position_data = unpackMessagePayload("B5iI", msg)
                    drive_name = "swivel"
                else:
                    return

                # Get the table for the drive.
                position_table = getattr(self.main_window.ui, f"{drive_name}DrivePositionTable", None)

                # The drive ID is still in this data, we do not care about it here.
                position_data = position_data[1:]

                if position_table is not None:
                    for index, val in enumerate(position_data):
                        item = position_table.item(index, 1)
                        item.setText(f"{val}")
                else:
                    print(f"E3: {__file__} - {drive_name}")

        except Exception as e:
            print(f"E2: {__file__}: {e}")


    """
    Updates the last field in the drive position table. This is done here because it comes from another message.

    @param msg: The message to unpack.
    """
    def updateDrivePositionCalcPosition(self, msg):
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                automation_payload = unpackMessagePayload("QH10BQ", msg)

                chair_pos = automation_payload[7]
                swivel_pos = automation_payload[8]
                footrest_pos = automation_payload[9]

                # Update the last row for each table
                chair_last_row = self.main_window.ui.chairDrivePositionTable.rowCount() - 1
                footrest_last_row = self.main_window.ui.footrestDrivePositionTable.rowCount() - 1
                swivel_last_row = self.main_window.ui.swivelDrivePositionTable.rowCount() - 1

                self.main_window.ui.chairDrivePositionTable.item(chair_last_row, 1).setText(f"{ChairPositions(chair_pos).name}")
                self.main_window.ui.footrestDrivePositionTable.item(footrest_last_row, 1).setText(f"{FootrestPositions(footrest_pos).name}")
                self.main_window.ui.swivelDrivePositionTable.item(swivel_last_row, 1).setText(f"{SwivelPositions(swivel_pos).name}")

                self.main_window.ui.chairDrivePositionTable.item(chair_last_row, 1).setForeground(Colours.GARNET)
                self.main_window.ui.footrestDrivePositionTable.item(footrest_last_row, 1).setForeground(Colours.GARNET)
                self.main_window.ui.swivelDrivePositionTable.item(swivel_last_row, 1).setForeground(Colours.GARNET)
        except Exception as e:
            print(f"E4: {__file__}: {e}")