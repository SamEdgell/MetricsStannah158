# Standard library imports.
import os

# Third party imports.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_ate import ATERequests
from Enums.enum_config import StoredConfigID
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours
from Utilities.messages import unpackMessagePayload


class UIConfig:
    """
    Class for the configuration.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        self.main_window.ui.alterConfigButton.clicked.connect(self.alterConfig)
        self.main_window.ui.loadConfigButton.clicked.connect(self.loadConfig)
        self.main_window.ui.restoreConfigButton.clicked.connect(self.restoreConfig)
        self.main_window.ui.resetConfigButton.clicked.connect(self.clearAlterColumn)
        self.main_window.ui.eraseSDCardButton.clicked.connect(self.eraseSDCard)
        self.main_window.ui.injectConfigButton.clicked.connect(self.injectConfig)
        self.main_window.ui.saveConfigButton.clicked.connect(self.saveConfig)

        self.setStyleSheetUIConfig()
        self.populateConfigTable()

        # Set up custom painter for all columns.
        delegate = Painter()
        self.main_window.ui.configTable.setItemDelegate(delegate)

        self.ATEMode = False # When true, it will allow you to set/get stored config in release


    def setStyleSheetUIConfig(self):
        """
        Sets the style sheet for the UIConfig items.
        Only doing additional stuff to items here that would not work in QTCreator.
        """
        # Adjust the header and column widths.
        header = self.main_window.ui.configTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Fixed)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        header.setFixedHeight(20)

        self.main_window.ui.configTable.setColumnWidth(0, 50)
        self.main_window.ui.configTable.setColumnWidth(2, 100)
        self.main_window.ui.configTable.setColumnWidth(3, 100)

        # Disable the built-in grid, will customise with the delegate class.
        self.main_window.ui.configTable.setShowGrid(False)


    def populateConfigTable(self):
        """
        Populates the config table with the config enums.
        """
        self.main_window.ui.configTable.setRowCount(len(StoredConfigID))
        row = 0

        # Setup row for each record.
        for config_count, record in enumerate(StoredConfigID):
            # Column 0 is not editable.
            column0 = QTableWidgetItem(str(config_count))
            column0.setFlags(Qt.ItemIsEnabled)
            self.main_window.ui.configTable.setItem(row, 0, column0)

            # Column 1 is not editable.
            column1 = QTableWidgetItem(record.name)
            column1.setFlags(Qt.ItemIsEnabled)
            self.main_window.ui.configTable.setItem(row, 1, column1)

            # Column 2 is not editable.
            column2 = QTableWidgetItem("")
            column2.setFlags(Qt.ItemIsEnabled)
            self.main_window.ui.configTable.setItem(row, 2, column2)

            # Column 3 is editable.
            column3 = QTableWidgetItem("")
            self.main_window.ui.configTable.setItem(row, 3, column3)
            row += 1

        # Force additional settings to rows/columns after populated.
        for row in range(self.main_window.ui.configTable.rowCount()):
            self.main_window.ui.configTable.setRowHeight(row, 14)

            # Row colours.
            self.main_window.ui.configTable.item(row, 0).setBackground(Colours.BEIGE)
            self.main_window.ui.configTable.item(row, 1).setBackground(Colours.BEIGE)
            self.main_window.ui.configTable.item(row, 2).setBackground(Colours.BEIGE)
            self.main_window.ui.configTable.item(row, 3).setBackground(Colours.BEIGE)

            self.main_window.ui.configTable.item(row, 0).setForeground(Colours.GARNET)
            self.main_window.ui.configTable.item(row, 1).setForeground(Colours.BLACK)
            self.main_window.ui.configTable.item(row, 2).setForeground(Colours.BLACK)
            self.main_window.ui.configTable.item(row, 2).setForeground(Colours.BLACK)

            # Column alignment.
            for col in range(self.main_window.ui.configTable.columnCount()):
                alignment = Qt.AlignLeft if col in [1] else Qt.AlignCenter
                self.main_window.ui.configTable.item(row, col).setTextAlignment(alignment)

        # Resize the table to the content.
        self.resizeConfigTableToContent()


    def resizeConfigTableToContent(self):
        """
        Resizes the default table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons to positions based on the new table size.
        """
        # Table height.
        table_row_count = self.main_window.ui.configTable.rowCount()
        table_row_height = self.main_window.ui.configTable.rowHeight(0)
        table_frame_width = self.main_window.ui.configTable.frameWidth()
        table_header_height = self.main_window.ui.configTable.horizontalHeader().height()
        table_total_height = table_header_height + (table_row_count * table_row_height) + (2 * table_frame_width)
        self.main_window.ui.configTable.setFixedHeight(table_total_height)

        # Define gaps.
        pixel_gap = 12

        # Calculate positions for the buttons.
        button_top = self.main_window.ui.configTable.y() + table_total_height + pixel_gap
        button_bottom = button_top + self.main_window.ui.loadConfigButton.height()

        # Move buttons to their respective positions.
        self.main_window.ui.loadConfigButton.move(self.main_window.ui.loadConfigButton.x(), button_top)
        self.main_window.ui.alterConfigButton.move(self.main_window.ui.alterConfigButton.x(), button_top)
        self.main_window.ui.resetConfigButton.move(self.main_window.ui.resetConfigButton.x(), button_top)

        # Total group box height is the sum of the table height, button height, and button gap.
        group_box_height = button_bottom + pixel_gap

        # Set the new group box height.
        self.main_window.ui.configTable.parent().setFixedHeight(group_box_height)


    def loadConfig(self):
        """
        Request to load the config settings from the device.
        """
        setting_id = StoredConfigID.CONFIG_OBJECT_COUNT.value # To request all records, the setting ID must be >= StoredConfigID.CONFIG_OBJECT_COUNT
        if self.ATEMode:
            self.main_window.ui_comms.sendMessage(MessageID.ATE_REQUEST, "H4I", [ATERequests.ATE_STORED_CONFIGURATION_GET.value, setting_id, 0, 0, 0], SrcDest.SRC_DEST_X04, MsgMode.REQ)
        else:
            self.main_window.ui_comms.sendMessage(MessageID.STORED_CONFIGURATION, "HI", [setting_id, 0], SrcDest.SRC_DEST_X04, MsgMode.GET)


    def restoreConfig(self):
        """
        Request to restore the config settings from the device.
        """
        if self.main_window.ui.confirmRestoreButton.isChecked():
            self.main_window.ui_comms.sendMessage(MessageID.RESET_ALL_CONFIG, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ)


    def clearAlterColumn(self):
        """
        Clears the alter column.
        """
        for row in range(self.main_window.ui.configTable.rowCount()):
            item = self.main_window.ui.configTable.item(row, 3)
            item.setText("")


    def alterConfig(self):
        """
        Request to alter the config settings on the device.
        """
        for record in StoredConfigID:
            if record.value < StoredConfigID.CONFIG_OBJECT_COUNT.value:
                setting_id = record.value
                value = self.main_window.ui.configTable.item(setting_id, 3).text()
                if len(value) > 0:
                    value = int(value)
                    self.main_window.ui_console.logDebugConsole(f"{setting_id}, {value}")
                    if self.ATEMode:
                        # Lower case i is intentional instead of I, which is what is expected on the receiving end
                        self.main_window.ui_comms.sendMessage(MessageID.ATE_REQUEST, "H4i", [ATERequests.ATE_STORED_CONFIGURATION_SET.value, setting_id, value, 0, 0], SrcDest.SRC_DEST_X04, MsgMode.REQ)
                    else:
                        self.main_window.ui_comms.sendMessage(MessageID.STORED_CONFIGURATION, "Hi", [setting_id, value], SrcDest.SRC_DEST_X04, MsgMode.SET)
        self.clearAlterColumn()
        self.loadConfig() # Also request a new update of the config table after altering


    def updateConfig(self, msg):
        """
        Updates the config table with the record values.

        Args:
            msg: config payload.
        """
        # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
        if MsgMode(msg[5]) == MsgMode.GET_ACK:
            configPayload = unpackMessagePayload("Hi", msg)
            setting_id = configPayload[0]
            value = configPayload[1]
            if value == -559038737:  # 0xDEADBEEF
                item = self.main_window.ui.configTable.item(setting_id, 2)
                item.setText(f"-")
            else:
                item = self.main_window.ui.configTable.item(setting_id, 2)
                item.setText(f"{value}")


    def eraseSDCard(self):
        """
        Erases all files on the SD card.
        """
        if self.main_window.ui.confirmEraseButton.isChecked():
            self.main_window.ui_comms.sendMessage(MessageID.RESET_STORED_DATA, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ)


    def injectConfig(self):
        """
        Injects a config file into the table widget ready to be altered.
        """
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Inject Config", "ConfigFiles", "Config Files (*.cfg)")

        self.main_window.ui_console.logDebugConsole(f"Injecting {file_path}")

        if file_path:
            # Read file and apply config changes to each record
            with open(file_path, 'r') as f:
                for _, line in enumerate(f, 1):
                    line = line.strip()
                    # Skip empty lines
                    if not line:
                        continue

                    line = line.split(',', 1) # Split only the first comma

                    if len(line) == 2:
                        setting_id = int(line[0].strip())
                        value = int(line[1].strip())

                        self.main_window.ui_console.logDebugConsole(f"{setting_id}, {value}")

                        # Add line of data to config table
                        inject_row = self.main_window.ui.configTable.item(setting_id, 3)
                        if value != 0xDEADBEEF:
                            inject_row.setText(f"{value}")


    def saveConfig(self):
        """
        Saves current values in table widget into a config file.
        """
        config_dir = "ConfigFiles"
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        file_path, _ = QFileDialog.getSaveFileName(self.main_window, "Save Config", config_dir, "Config Files (*.cfg)")

        if file_path:
            self.main_window.ui_console.logDebugConsole(f"Saving config {file_path}")
            # Create buffer
            buffer = []
            for record in range(StoredConfigID.CONFIG_OBJECT_COUNT.value):
                try:
                    id = self.main_window.ui.configTable.item(record, 0).text()
                    value = self.main_window.ui.configTable.item(record, 2).text()
                    # Do not alter the records that reside in BBRAM
                    if (record in [StoredConfigID.CONFIG_UNRECOVERABLE_FAULT_PRESENT.value,
                                   StoredConfigID.CONFIG_MAIN_DRIVE_POSITION.value,
                                   StoredConfigID.CONFIG_MAIN_DRIVE_POSITION_VALID.value,
                                   StoredConfigID.CONFIG_CURRENT_TIME.value]
                                   or
                    # Do not alter inactive records
                        value == "-"):
                        value = 0xDEADBEEF
                    self.main_window.ui_console.logDebugConsole(f"{id},{value}")
                    buffer.append(f"{id},{value}")
                except Exception as e:
                    print(f"E1: {__file__}: {e}")

            # Write buffer to file
            try:
                with open(file_path, 'w') as f:
                    for line in buffer:
                        f.write(line + "\n")
            except Exception as e:
                print(f"E2: {__file__}: {e}")


    def updateSDCardErase(self, msg):
        """
        Updates text box that erasing of SD card was successful.

        Args:
            msg: SD card payload.
        """
        # Check for mode type. Note, this is the 5th element as it's not unpacked yet.
        if MsgMode(msg[5]) == MsgMode.REQ_ACK:
            self.main_window.ui.sdCardTextEdit.setText(f"SD Card Erased")
            self.main_window.ui.sdCardTextEdit.setStyleSheet(f"""
                                                            QLineEdit{{
                                                                background-color: {Colours.PALE_GREEN.name()};
                                                                border: 1px solid {Colours.BLACK.name()};
                                                                border-radius: 3px;
                                                            }}
                                                            """)
        else:
            self.main_window.ui.sdCardTextEdit.setText(f"SD Card Erase Failed")
            self.main_window.ui.sdCardTextEdit.setStyleSheet(f"""
                                                            QLineEdit{{
                                                                background-color: {Colours.LIGHT_PINK.name()};
                                                                border: 1px solid {Colours.BLACK.name()};
                                                                border-radius: 3px;
                                                            }}
                                                            """)


    def setATEMode(self, isATE):
        """
        Sets the state of ATE mode.

        Args:
            isATE: True if ATE mode, false otherwise
        """
        self.ATEMode = isATE


    def getATEMode(self):
        """
        Get the state of ATE mode.

        Returns:
            True if ATE mode, false otherwise
        """
        return self.ATEMode