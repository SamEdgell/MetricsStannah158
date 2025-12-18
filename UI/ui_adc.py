# Third party imports.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_adc import ADCX04, ADCX01
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours
from Utilities.messages import unpackMessage


class UIADC:
    """
    Class for the ADC table. Handles initialisation, styling, population, and updates for the ADC table in the UI.
    """

    def __init__(self, main_window):
        """
        Initialises the ADC class.

        Args:
            main_window: Reference to the main window, used for accessing UI elements.
        """
        self.main_window = main_window
        self.main_window.ui.resetADCButton.clicked.connect(self.resetADCTable)
        self.main_window.ui.alterADCButton.clicked.connect(self.alterADCTable)

        self.adc_resolution_bits = 12
        self.adc_raw_saturated_percent = 85
        self.current_altered_channels = 0

        # Set up custom painter for all columns.
        delegate = Painter()
        self.main_window.ui.adcTable.setItemDelegate(delegate)

        self.setStyleSheetUIADC()
        self.populateADCTable()


    def setStyleSheetUIADC(self):
        """
        Sets the style sheet for the UIADC items.
        Only doing additional stuff to items here that would not work in QTCreator.
        """
        # Adjust the header and column widths.
        header = self.main_window.ui.adcTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Fixed)
        header.setSectionResizeMode(3, QHeaderView.Fixed)
        header.setSectionResizeMode(4, QHeaderView.Fixed)
        header.setFixedHeight(20)

        self.main_window.ui.adcTable.setColumnWidth(0, 45)
        self.main_window.ui.adcTable.setColumnWidth(2, 50)
        self.main_window.ui.adcTable.setColumnWidth(3, 40)
        self.main_window.ui.adcTable.setColumnWidth(4, 55)

        # Disable the built-in grid, will customise with the delegate painter.
        self.main_window.ui.adcTable.setShowGrid(False)


    def populateADCTable(self):
        """
        Populates the ADC table with the ADC enums.
        """
        self.main_window.ui.adcTable.setRowCount(len(ADCX04) + len(ADCX01))
        row = 0

        # Setup row for each channel.
        for adc_group, colour, prefix in ((ADCX04, Colours.GARNET, "X04"), (ADCX01, Colours.ROYAL_BLUE, "X01")):
            for adc_count, channel in enumerate(adc_group):
                self.main_window.ui.adcTable.setRowHeight(row, 14)
                pin_id = f"{prefix}-{adc_count}"

                # Column 0: Pin ID
                column_0 = QTableWidgetItem(pin_id)
                column_0.setFlags(Qt.ItemIsEnabled)
                column_0.setForeground(colour)
                column_0.setBackground(Colours.BEIGE)
                column_0.setTextAlignment(Qt.AlignLeft)
                self.main_window.ui.adcTable.setItem(row, 0, column_0)

                # Column 1: Channel Name
                column_1 = QTableWidgetItem(channel.name)
                column_1.setFlags(Qt.ItemIsEnabled)
                column_1.setForeground(Colours.BLACK)
                column_1.setBackground(Colours.BEIGE)
                column_1.setTextAlignment(Qt.AlignLeft)
                self.main_window.ui.adcTable.setItem(row, 1, column_1)

                # Column 2: Scaled Value
                column_2 = QTableWidgetItem("")
                column_2.setFlags(Qt.ItemIsEnabled)
                column_2.setForeground(Colours.BLACK)
                column_2.setBackground(Colours.BEIGE)
                column_2.setTextAlignment(Qt.AlignCenter)
                self.main_window.ui.adcTable.setItem(row, 2, column_2)

                # Column 3: Raw Value
                column_3 = QTableWidgetItem("")
                column_3.setFlags(Qt.ItemIsEnabled)
                column_3.setForeground(Colours.BLACK)
                column_3.setBackground(Colours.BEIGE)
                column_3.setTextAlignment(Qt.AlignCenter)
                self.main_window.ui.adcTable.setItem(row, 3, column_3)

                # Column 4: Alter Value
                column_4 = QTableWidgetItem("")
                column_4.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                column_4.setForeground(Colours.BLACK)
                column_4.setBackground(Colours.BEIGE)
                # Note: Alignment for editable column 4 is handled by the delegate or default behaviour.
                self.main_window.ui.adcTable.setItem(row, 4, column_4)

                row += 1

        # Resize the table to the content.
        self.resizeADCTableToContent()


    def resizeADCTableToContent(self):
        """
        Resizes the default table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons to positions based on the new table size.
        """
        # Table height.
        table_row_count = self.main_window.ui.adcTable.rowCount()
        table_row_height = self.main_window.ui.adcTable.rowHeight(0)
        table_header_height = self.main_window.ui.adcTable.horizontalHeader().height()
        table_frame_width = self.main_window.ui.adcTable.frameWidth()
        table_total_height = table_header_height + (table_row_count * table_row_height) + (2 * table_frame_width)
        self.main_window.ui.adcTable.setFixedHeight(table_total_height)

        # Define gaps.
        padding_gap = 16

        # Total group box height is the sum of the table height, padding gap.
        group_box_height = self.main_window.ui.adcTable.y() + table_total_height + padding_gap

        # Set new group box height.
        self.main_window.ui.adcTable.parent().setFixedHeight(group_box_height)


    def resetADCTable(self):
        """
        Resets the ADC table. The user has requested to reset the table from any altered state.
        """
        self.clearAlteredData()
        # Reset alter on both boards.
        msgID = MessageID.METRICS_RESET_ADC_ALTER # NOTE: This message has not been implemented on the ECU side.
        for dest in (SrcDest.SRC_DEST_X04, SrcDest.SRC_DEST_X01):
            self.main_window.ui_comms.sendMessage(msgID, "", [], dest, MsgMode.SET)


    def clearAlteredData(self):
        """
        Will clear any altered values under that column in the ADC table.
        """
        for row in range(self.main_window.ui.adcTable.rowCount()):
            # Reset alter column (column 4) to default.
            alter_column = self.main_window.ui.adcTable.item(row, 4)
            alter_column.setText("")
            alter_column.setTextAlignment(Qt.AlignCenter)
            alter_column.setForeground(Colours.BLACK) # Delegate will paint the cell text with this colour.
            alter_column.setBackground(Colours.BEIGE) # Delegate will paint the cell background with this colour.


    def alterADCTable(self):
        """
        Alters the ADC table. The user has requested to alter one or more values in the table.
        """
        self.alterADC(len(ADCX04), SrcDest.SRC_DEST_X04, 0)
        self.alterADC(len(ADCX01), SrcDest.SRC_DEST_X01, len(ADCX04))
        self.clearAlteredData() # This option may be disabled at times in future, but for now, once the button is clicked, clear the column.


    def alterADC(self, adc_count, dest, offset):
        """
        Alters the ADC channels for specified destination. Altering any channels affects the raw value only, not the scaled.

        Args:
            adc_count:  Total number of channels to enumerate.
            dest:       The destination of those channels to change.
            offset:     Row number offset to start capturing data from.
        """
        data = [0xFFFF] * adc_count # Default all values, this assumes they are not altered.
        alter_approved = False
        max_adc_value = (2 ** self.adc_resolution_bits)

        for i in range(adc_count):
            row_num = i + offset
            altered_row = self.main_window.ui.adcTable.item(row_num, 4).text()

            # Has this row been altered?
            if altered_row:
                alter_approved = True
                try:
                    # Convert string to int.
                    value = int(altered_row)

                    # Check value is within raw value range.
                    if 0 <= value < max_adc_value:
                        data[i] = value
                except ValueError:
                    # Alter failed.
                    pass

        if alter_approved:
            self.main_window.ui_comms.sendMessage(MessageID.METRIC_ADC_INPUTS_OVERRIDE, f"I{adc_count}H", [adc_count, *data], dest, MsgMode.SET)


    def updateADCTable(self, msg):
        """
        Updates the ADC table with its new values.

        Args:
            msg: ADC payload.
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                header, adcPayload = unpackMessage("I30H", msg)

                source = header[2]
                num_channels = adcPayload[0]
                data = adcPayload[1:-1] # Skip 1st index which is count.
                altered_channels = adcPayload[-1] # Last index is the altered channels bitmask.
                changed_altered_channels = 0

                # Check the channel count matches the expected number of channels per source.
                if num_channels != len(ADCX04) and SrcDest(source) == SrcDest.SRC_DEST_X04:
                    print(f"X04 ADC Count Mismatch. Enum Count = {len(ADCX04)}. Actual Count = {num_channels}")
                    return
                elif num_channels != len(ADCX01) and SrcDest(source) == SrcDest.SRC_DEST_X01:
                    print(f"X01 ADC Count Mismatch. Enum Count = {len(ADCX01)}. Actual Count = {num_channels}")
                    return

                # The X01 offset starts from the end of the X04 channels.
                offset = 0 if SrcDest(source) == SrcDest.SRC_DEST_X04 else len(ADCX04)

                # Check for any bits that have changed state from the previous reading for the altered channels. Doing this allows efficient GUI updates and prevents unnecessary redraws.
                changed_altered_channels = self.current_altered_channels ^ altered_channels
                self.current_altered_channels = altered_channels

                # Loop through each channel and update the table.
                for i in range(num_channels):
                    raw_value = data[i << 1] # Raw value is the first element of the pair.
                    scaled_value = data[(i << 1) + 1] # Scaled value is the second element of the pair.
                    bitmask = 1 << i
                    row_num = offset + i

                    # Populate raw data.
                    raw_column = self.main_window.ui.adcTable.item(row_num, 3)
                    raw_column.setText(str(raw_value))

                    # Populate scaled data.
                    scaled_column = self.main_window.ui.adcTable.item(row_num, 2)
                    scaled_column.setText(f"{scaled_value / 1000:.2f}")

                    # Check if the raw value is close to saturation and set the background colour accordingly.
                    bg_colour = Colours.LIGHT_PINK if (raw_value >= (((2 ** self.adc_resolution_bits) - 1) * (self.adc_raw_saturated_percent / 100))) else Colours.BEIGE
                    raw_column.setBackground(bg_colour)

                    # Check if this channel is currently altered.
                    if changed_altered_channels & bitmask:
                        cell_colour = Colours.APRICOT if self.current_altered_channels & bitmask else Colours.BEIGE
                        self.main_window.ui.adcTable.item(row_num, 1).setBackground(cell_colour)

        except Exception as e:
            print(f"E1: {__file__}: {e}")