# Third party imports.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_calls_demands import ChairDemands, FootrestDemands, MainDemands, SwivelDemands
from Enums.enum_msg import MsgMode
from Enums.enum_drive_state_machine import ActiveBridge, DriveState, DriveStateData, MovingDriveState
from Enums.enum_system_drives import SystemDrive
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours
from Utilities.messages import unpackMessagePayload


class UIDriveStateMachine:
    """
    Class for handling all aspects of drive state machine data.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        delegateChair = Painter()
        self.main_window.ui.chairStateMachineTable.setItemDelegate(delegateChair)

        delegateFootrest = Painter()
        self.main_window.ui.footrestStateMachineTable.setItemDelegate(delegateFootrest)

        delegateMain = Painter()
        self.main_window.ui.mainStateMachineTable.setItemDelegate(delegateMain)

        delegateSwivel = Painter()
        self.main_window.ui.swivelStateMachineTable.setItemDelegate(delegateSwivel)

        self.setStyleSheetUIDriveState()
        self.populateStateTables()


    def setStyleSheetUIDriveState(self):
        """
        Sets the style sheet for the UIDriveStateMachine tables.
        Only doing additional stuff to items here that would not work in QTCreator.
        """
        tables = [
            self.main_window.ui.chairStateMachineTable,
            self.main_window.ui.footrestStateMachineTable,
            self.main_window.ui.mainStateMachineTable,
            self.main_window.ui.swivelStateMachineTable
        ]

        for table in tables:
            header = table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Fixed)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setFixedHeight(20)
            # Once header is set, remove visibility, this is intended for these tables.
            header.setVisible(False)

            table.setColumnWidth(0, 60)

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
                font-weight: normal;                /* Font weight of the header text */
            }}
            QHeaderView::section:last {{
                border-right: none;                 /* Remove the right border from the last header section. This is because of an overlap with the table widget border */
            }}
            """)


    def populateStateTables(self):
        """
        Populates the State Machine table with the variable ID's
        """
        tables = [
            self.main_window.ui.chairStateMachineTable,
            self.main_window.ui.footrestStateMachineTable,
            self.main_window.ui.mainStateMachineTable,
            self.main_window.ui.swivelStateMachineTable
        ]

        for table in tables:
            table.setRowCount(len(DriveStateData))
            row = 0

            # Setup each row.
            for _, var in enumerate(DriveStateData):
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
        self.resizeStateTableToContent()


    def resizeStateTableToContent(self):
        """
        Resizes the default table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons (if exists) to positions based on the new table size.
        """
        tables = [
            self.main_window.ui.chairStateMachineTable,
            self.main_window.ui.footrestStateMachineTable,
            self.main_window.ui.mainStateMachineTable,
            self.main_window.ui.swivelStateMachineTable
        ]

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


    def updateDriveStateTable(self, msg):
        """
        Handles new drive state data for a specific drive.

        Args:
            msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                state_data = unpackMessagePayload("4B", msg)

                if SystemDrive(state_data[0]) == SystemDrive.SYS_DRIVE_CHAIR_FOLD:
                    drive_name = "chair"
                elif SystemDrive(state_data[0]) == SystemDrive.SYS_DRIVE_FOOTREST:
                    drive_name = "footrest"
                elif SystemDrive(state_data[0]) == SystemDrive.SYS_DRIVE_MAIN_DRIVE:
                    drive_name = "main"
                elif SystemDrive(state_data[0]) == SystemDrive.SYS_DRIVE_SWIVEL:
                    drive_name = "swivel"
                else:
                    return

                # Get the table for the drive.
                state_table = getattr(self.main_window.ui, f"{drive_name}StateMachineTable", None)

                if state_table is not None:
                    # Start populating from row 1, row 0 is done in the demand function below.
                    item = state_table.item(1, 1)
                    item.setText(f"{ActiveBridge(state_data[3]).name}")

                    item = state_table.item(2, 1)
                    item.setText(f"{DriveState(state_data[2]).name}")

                    item = state_table.item(3, 1)
                    item.setText(f"{MovingDriveState(state_data[1]).name}")
                else:
                    print(f"E2: {__file__} - {drive_name}")

        except Exception as e:
            print(f"E1: {__file__}: {e}")


    def updateDriveStateDemand(self, msg):
        """
        Updates the last field in the drive state table. This is done here because it comes from another message.

        Args:
            msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                automation_payload = unpackMessagePayload("QH10BQ", msg)

                main_demand = automation_payload[2]
                swivel_demand = automation_payload[3]
                chair_demand = automation_payload[4]
                footrest_demand = automation_payload[5]

                # Update the first row for each table
                self.main_window.ui.mainStateMachineTable.item(0, 1).setText(f"{MainDemands(main_demand).name}")
                self.main_window.ui.swivelStateMachineTable.item(0, 1).setText(f"{SwivelDemands(swivel_demand).name}")
                self.main_window.ui.chairStateMachineTable.item(0, 1).setText(f"{ChairDemands(chair_demand).name}")
                self.main_window.ui.footrestStateMachineTable.item(0, 1).setText(f"{FootrestDemands(footrest_demand).name}")

        except Exception as e:
            print(f"E3: {__file__}: {e}")