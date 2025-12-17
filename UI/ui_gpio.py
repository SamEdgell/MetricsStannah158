# Third party imports.
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_gpio import InputsECU1, InputsECU2, OutputsECU1, OutputsECU2
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours
from Utilities.messages import unpackMessage


class UIGPIO:
    """
    Class for the GPIO tables. Handles initialisation, styling, population, and updates for the GPIO tables in the UI.
    """

    def __init__(self, main_window):
        """
        Initialises the UIGPIO class.

        Args:
            main_window: Reference to the main window, used for accessing UI elements.
        """
        self.main_window = main_window
        self.main_window.ui.resetInputsButton.clicked.connect(lambda: self.resetGPIOTable(self.main_window.ui.inputsTable))
        self.main_window.ui.alterInputsButton.clicked.connect(lambda: self.alterGPIOTable(self.main_window.ui.inputsTable))
        self.main_window.ui.resetOutputsButton.clicked.connect(lambda: self.resetGPIOTable(self.main_window.ui.outputsTable))
        self.main_window.ui.alterOutputsButton.clicked.connect(lambda: self.alterGPIOTable(self.main_window.ui.outputsTable))
        self.main_window.ui.inputsTable.cellClicked.connect(lambda row, column: self.handleCellClick(self.main_window.ui.inputsTable, row, column))
        self.main_window.ui.outputsTable.cellClicked.connect(lambda row, column: self.handleCellClick(self.main_window.ui.outputsTable, row, column))

        # For below. First 4 words are ECU1, last 4 words are ECU2.
        self.current_input_states = [0] * 8
        self.current_output_states = [0] * 8
        self.current_altered_input_states = [0] * 8
        self.current_altered_output_states = [0] * 8

        # Set up custom painter for all columns.
        delegate = Painter()
        self.main_window.ui.inputsTable.setItemDelegate(delegate)
        self.main_window.ui.outputsTable.setItemDelegate(delegate)

        self.setStyleSheetUIGPIO()
        self.populateGPIOTable(self.main_window.ui.inputsTable)
        self.populateGPIOTable(self.main_window.ui.outputsTable)


    def setStyleSheetUIGPIO(self):
        """
        Sets the style sheet for the UIGPIO items.
        Only applies additional styling here that would not work in QtCreator.
        """
        tables = [self.main_window.ui.inputsTable, self.main_window.ui.outputsTable]

        for table in tables:
            # Adjust the header and column widths.
            header = table.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Fixed)
            header.setSectionResizeMode(1, QHeaderView.Stretch)
            header.setSectionResizeMode(2, QHeaderView.Fixed)
            header.setSectionResizeMode(3, QHeaderView.Fixed)
            header.setFixedHeight(20)

            table.setColumnWidth(0, 45)
            table.setColumnWidth(2, 40)
            table.setColumnWidth(3, 40)

            # Disable the built-in grid, will customise with the delegate class.
            table.setShowGrid(False)


    def populateGPIOTable(self, table):
        """
        Populates the tables with their respective enums.

        Args:
            table: The table widget to populate.
        """
        if table == self.main_window.ui.inputsTable:
            self.main_window.ui.inputsTable.setRowCount(len(InputsECU1) + len(InputsECU2))
            ecu1_table = InputsECU1
            ecu2_table = InputsECU2
        else:
            self.main_window.ui.outputsTable.setRowCount(len(OutputsECU1) + len(OutputsECU2))
            ecu1_table = OutputsECU1
            ecu2_table = OutputsECU2

        row = 0

        # Set up row for each input or output.
        for table_group, colour, prefix in ((ecu1_table, Colours.GARNET, "ECU1"), (ecu2_table, Colours.ROYAL_BLUE, "ECU2")):
            for count, channel in enumerate(table_group):
                table.setRowHeight(row, 14)
                pin_id = f"{prefix}-{count}"

                # Column 0: Pin ID
                column_0 = QTableWidgetItem(pin_id)
                column_0.setForeground(colour)
                column_0.setBackground(Colours.BEIGE)
                column_0.setTextAlignment(Qt.AlignLeft)
                table.setItem(row, 0, column_0)

                # Column 1: Channel Name
                column_1 = QTableWidgetItem(channel.name)
                column_1.setForeground(Colours.BLACK)
                column_1.setBackground(Colours.BEIGE)
                column_1.setTextAlignment(Qt.AlignLeft)
                table.setItem(row, 1, column_1)

                # Column 2: Value
                column_2 = QTableWidgetItem("0")
                column_2.setForeground(Colours.BLACK)
                column_2.setBackground(Colours.LIGHT_PINK)
                column_2.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, 2, column_2)

                # Column 3: Alter Value
                column_3 = QTableWidgetItem("")
                column_3.setForeground(Colours.BLACK)
                column_3.setBackground(Colours.BEIGE)
                column_3.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, 3, column_3)

                row += 1

        # Resize the table to the content.
        self.resizeGPIOTableToContent(table)


    def resizeGPIOTableToContent(self, table):
        """
        Resizes the default table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons to positions based on the new table size.

        Args:
            table: Table to resize.
        """
        # Table height.
        table_row_count = table.rowCount()
        table_row_height = table.rowHeight(0)
        table_header_height = table.horizontalHeader().height()
        table_frame_width = table.frameWidth()
        table_total_height = table_header_height + (table_row_count * table_row_height) + (2 * table_frame_width)
        table.setFixedHeight(table_total_height)

        # Define gaps.
        padding_gap = 16

        # Total group box height is the sum of the table height, padding gap.
        group_box_height = table.y() + table_total_height + padding_gap

        # Set new group box height.
        table.parent().setFixedHeight(group_box_height)


    def resetGPIOTable(self, table):
        """
        Resets the table. The user has requested to reset the table from any altered state.

        Args:
            table: Table to reset.
        """
        self.clearAlteredData(table)
        # Reset alter on both boards.
        msgID = MessageID.METRICS_RESET_INPUTS_ALTER if table == self.main_window.ui.inputsTable else MessageID.METRICS_RESET_OUTPUTS_ALTER
        for dest in (SrcDest.SRC_DEST_ECU1, SrcDest.SRC_DEST_ECU2):
            self.main_window.ui_comms.sendMessage(msgID, "", [], dest, MsgMode.SET)


    def clearAlteredData(self, table):
        """
        Will clear any altered values under that column in the GPIO table.

        Args:
            table: Table to clear altered data from.
        """
        for row in range(table.rowCount()):
            # Reset alter column (column 3) to default.
            alter_column = table.item(row, 3)
            alter_column.setText("")
            alter_column.setTextAlignment(Qt.AlignCenter)
            alter_column.setForeground(Colours.BLACK) # Delegate will paint the cell text with this colour.
            alter_column.setBackground(Colours.BEIGE) # Delegate will paint the cell background with this colour.


    def alterGPIOTable(self, table):
        """
        Alters the table. The user has requested to alter one or more values in the table.

        Args:
            table: Table to alter.
        """
        if table == self.main_window.ui.inputsTable:
            self.alterInputs(0, len(InputsECU1), SrcDest.SRC_DEST_ECU1)
            self.alterInputs(len(InputsECU1), len(InputsECU2), SrcDest.SRC_DEST_ECU2)
        else:
            self.alterOutputs(0, len(OutputsECU1), SrcDest.SRC_DEST_ECU1)
            self.alterOutputs(len(OutputsECU1), len(OutputsECU2), SrcDest.SRC_DEST_ECU2)
        self.clearAlteredData(table) # This option may be disabled at times in future, but for now, once the button is clicked, clear the column.


    def alterInputs(self, offset, gpio_count, dest):
        """
        Alters the GPIO inputs for specified destination.

        Args:
            offset:     Row number offset to start capturing data from.
            gpio_count: Total number of inputs to enumerate.
            dest:       The destination of those inputs to change.
        """
        alter_approved = False

        # Retain all current states. This allows multiple alterations to be made without losing previous ones (unless reset).
        if SrcDest(dest) == SrcDest.SRC_DEST_ECU1:
            input_states = self.current_input_states[:4]                    # First 4 words are ECU1 inputs.
            altered_input_states = self.current_altered_input_states[:4]    # First 4 words are ECU1 altered inputs.
        else:
            input_states = self.current_input_states[4:]                    # Last 4 words are ECU2 inputs.
            altered_input_states = self.current_altered_input_states[4:]    # Last 4 words are ECU2 altered inputs.

        for i in range(gpio_count):
            word = i // 32          # Calculates which word contains the i-th input.
            bit = i & 31            # Locate bit position of input.
            bitmask = 1 << bit      # Creates mask with a 1 in the position of the input.
            row_num = i + offset    # For ECU1 inputs, the row number is not shifted down the table.

            altered_row = self.main_window.ui.inputsTable.item(row_num, 3).text()

            # Check to see whether this pin has an altered value set.
            if altered_row:
                alter_approved = True

                # Check to see whether this pin should be altered to logic 1 or 0.
                if altered_row == "1":
                    input_states[word] = input_states[word] | bitmask
                else:
                    input_states[word] = input_states[word] & ~bitmask

                # Update that this pin has been altered.
                altered_input_states[word] = altered_input_states[word] | bitmask

        # Has at least one pin been altered?
        if alter_approved:
            self.main_window.ui_comms.sendMessage(MessageID.METRICS_INPUTS_ALTER, "9I", [gpio_count, *input_states, *altered_input_states], dest, MsgMode.SET)


    def alterOutputs(self, offset, gpio_count, dest):
        """
        Alters the GPIO outputs for specified destination.

        Args:
            offset:     Row number offset to start capturing data from.
            gpio_count: Total number of outputs to enumerate.
            dest:       The destination of those outputs to change.
        """
        alter_approved = False

        # Retain all current states. This allows multiple alterations to be made without losing previous ones (unless reset).
        if SrcDest(dest) == SrcDest.SRC_DEST_ECU1:
            output_states = self.current_output_states[:4]                     # First 4 words are ECU1 outputs.
            altered_output_states = self.current_altered_output_states[:4]     # First 4 words are ECU1 altered outputs.
        else:
            output_states = self.current_output_states[4:]                     # Last 4 words are ECU2 outputs.
            altered_output_states = self.current_altered_output_states[4:]     # Last 4 words are ECU2 altered outputs.

        for i in range(gpio_count):
            word = i // 32          # Calculates which word contains the i-th output.
            bit = i & 31            # Locate bit position of output.
            bitmask = 1 << bit      # Creates mask with a 1 in the position of the output.
            row_num = i + offset    # For ECU1 outputs, the row number is not shifted down the table.

            altered_row = self.main_window.ui.outputsTable.item(row_num, 3).text()

            # Check to see whether this pin has an altered value set.
            if altered_row:
                alter_approved = True

                # Check to see whether this pin should be altered to logic 1 or 0.
                if altered_row == "1":
                    output_states[word] = output_states[word] | bitmask
                else:
                    output_states[word] = output_states[word] & ~bitmask

                # Update that this pin has been altered.
                altered_output_states[word] = altered_output_states[word] | bitmask

        # Has at least one pin been altered?
        if alter_approved:
            self.main_window.ui_comms.sendMessage(MessageID.METRICS_OUTPUTS_ALTER, "9I", [gpio_count, *output_states, *altered_output_states], dest, MsgMode.SET)


    def handleCellClick(self, table, row, column):
        """
        Handles the cell click event. The user has clicked on a cell in the table, requesting that row value to be altered.

        Args:
            table:  The table widget where the cell was clicked.
            row:    The row number of the clicked cell.
            column: The column number of the clicked cell.
        """
        # Allow altering of row if clicked inside the ID column or the alter column.
        if column in (1, 3):
            item = table.item(row, 3)
            cell_value = item.text()

            if cell_value == "":
                new_value = "1"
                cell_colour = Colours.PALE_GREEN
            elif cell_value == "1":
                new_value = "0"
                cell_colour = Colours.LIGHT_PINK
            else:
                new_value = ""
                cell_colour = Colours.BEIGE

            item.setText(new_value)
            item.setBackground(cell_colour)


    def updateInputTable(self, msg):
        """
        Updates the inputs table with their respective values.

        Args:
            msg: Input payload.
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                header, input_payload = unpackMessage("9I", msg)

                source = header[2]
                num_inputs = input_payload[0]           # The total number of inputs to loop through and retrieve data from in this message.
                inputs = input_payload[1:5]             # Where the input data is located, there is a buffer of 4 words containing up to 32 inputs each.
                altered_inputs = input_payload[5:9]     # Where the altered input data is located, buffer of 4 words containing up to 32 inputs each.
                changed_inputs = [0] * 4                # 4 words capable of holding up to 32 inputs each.
                changed_altered_inputs = [0] * 4        # 4 words capable of holding up to 32 altered inputs each.

                if SrcDest(source) == SrcDest.SRC_DEST_ECU1:
                    # Check the number of inputs matches the expected number.
                    if num_inputs != len(InputsECU1):
                        print(f"ECU1 Inputs Count Mismatch. Enum Count = {len(InputsECU1)}. Actual Count = {num_inputs}")
                        return
                    prev_table_offset = 0 # First 4 words are ECU1 inputs.
                    ecu_offset = 0 # For ECU1 inputs, the row number is not shifted down the table.
                elif SrcDest(source) == SrcDest.SRC_DEST_ECU2:
                    # Check the number of inputs matches the expected number.
                    if num_inputs != len(InputsECU2):
                        print(f"ECU2 Inputs Count Mismatch. Enum Count = {len(InputsECU2)}. Actual Count = {num_inputs}")
                        return
                    prev_table_offset = 4 # Last 4 words are ECU2 inputs.
                    ecu_offset = len(InputsECU1) # The ECU2 offset starts from at the end of the ECU1.
                else:
                    print(f"UIGPIO - Unknown Source Update Inputs - {source}")
                    return

                # Check for any bits that have changed state from the previous reading for both inputs and altered inputs. Doing this allows efficient GUI updates and prevents unnecessary redraws.
                for i in range(4):
                    changed_inputs[i] = self.current_input_states[i + prev_table_offset] ^ inputs[i] # This is a 'change mask', bits that have changed are set to 1, else 0.
                    self.current_input_states[i + prev_table_offset] = inputs[i] # Update current states.
                    changed_altered_inputs[i] = self.current_altered_input_states[i + prev_table_offset] ^ altered_inputs[i] # This is a 'change mask', bits that have changed are set to 1, else 0.
                    self.current_altered_input_states[i + prev_table_offset] = altered_inputs[i] # Update current altered states.

                # Loop through each input and update state (if changed).
                for i in range(num_inputs):
                    word = i // 32              # Calculates which word contains this i-th input.
                    bit = i & 31                # Locate bit position of this input.
                    bitmask = 1 << bit          # Creates mask with a 1 at the current position of this input.
                    row_num = i + ecu_offset

                    # Check if this input has changed state.
                    if changed_inputs[word] & bitmask:
                        cell_value = "1" if inputs[word] & bitmask else "0" # Get the new value of the input that has changed.
                        cell_colour = Colours.PALE_GREEN if cell_value == "1" else Colours.LIGHT_PINK
                        self.main_window.ui.inputsTable.setItem(row_num, 2, QTableWidgetItem(cell_value))
                        self.main_window.ui.inputsTable.item(row_num, 2).setTextAlignment(Qt.AlignCenter)
                        self.main_window.ui.inputsTable.item(row_num, 2).setBackground(cell_colour)
                        self.main_window.ui.inputsTable.item(row_num, 2).setForeground(Colours.BLACK)

                    # Check if this input has changed altered state.
                    if changed_altered_inputs[word] & bitmask:
                        cell_colour = Colours.APRICOT if altered_inputs[word] & bitmask else Colours.BEIGE
                        self.main_window.ui.inputsTable.item(row_num, 1).setBackground(cell_colour)

        except Exception as e:
            print(f"E1: {__file__}: {e}")


    def updateOutputTable(self, msg):
        """
        Updates the outputs table with their respective values.

        Args:
            msg: Output payload.
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                header, output_payload = unpackMessage("9I", msg)

                source = header[2]
                num_outputs = output_payload[0]          # The total number of outputs to loop through and retrieve data from in this message.
                outputs = output_payload[1:5]            # Where the output data is located, there is a buffer of 4 words containing up to 32 outputs each.
                altered_outputs = output_payload[5:9]    # Where the altered output data is located, buffer of 4 words containing up to 32 outputs each.
                changed_outputs = [0] * 4                # 4 words capable of holding up to 32 outputs each.
                changed_altered_outputs = [0] * 4        # 4 words capable of holding up to 32 altered outputs each.

                if SrcDest(source) == SrcDest.SRC_DEST_ECU1:
                    # Check the number of outputs matches the expected number.
                    if num_outputs != len(OutputsECU1):
                        print(f"ECU1 Outputs Count Mismatch. Enum Count = {len(OutputsECU1)}. Actual Count = {num_outputs}")
                        return
                    prev_table_offset = 0 # First 4 words are ECU1 outputs.
                    ecu_offset = 0 # For ECU1 outputs, the row number is not shifted down the table.
                elif SrcDest(source) == SrcDest.SRC_DEST_ECU2:
                    # Check the number of outputs matches the expected number.
                    if num_outputs != len(OutputsECU2):
                        print(f"ECU2 Outputs Count Mismatch. Enum Count = {len(OutputsECU2)}. Actual Count = {num_outputs}")
                        return
                    prev_table_offset = 4 # Last 4 words are ECU2 outputs.
                    ecu_offset = len(OutputsECU1) # The ECU2 offset starts from at the end of the ECU1.
                else:
                    print(f"UIGPIO - Unknown Source Update Outputs")
                    return

                # Check for any bits that have changed state from the previous reading for both outputs and altered outputs. Doing this allows efficient GUI updates and prevents unnecessary redraws.
                for i in range(4):
                    changed_outputs[i] = self.current_output_states[i + prev_table_offset] ^ outputs[i] # This is a 'change mask', bits that have changed are set to 1, else 0.
                    self.current_output_states[i + prev_table_offset] = outputs[i] # Update current states.
                    changed_altered_outputs[i] = self.current_altered_output_states[i + prev_table_offset] ^ altered_outputs[i] # This is a 'change mask', bits that have changed are set to 1, else 0.
                    self.current_altered_output_states[i + prev_table_offset] = altered_outputs[i] # Update current altered states.

                # Loop through each output and update state (if changed).
                for i in range(num_outputs):
                    word = i // 32              # Calculates which word contains this i-th output.
                    bit = i & 31                # Locate bit position of this output.
                    bitmask = 1 << bit          # Creates mask with a 1 at the current position of this output.
                    row_num = i + ecu_offset

                    # Check if this output has changed state.
                    if changed_outputs[word] & bitmask:
                        cell_value = "1" if outputs[word] & bitmask else "0" # Get the new value of the output that has changed.
                        cell_colour = Colours.PALE_GREEN if cell_value == "1" else Colours.LIGHT_PINK
                        self.main_window.ui.outputsTable.setItem(row_num, 2, QTableWidgetItem(cell_value))
                        self.main_window.ui.outputsTable.item(row_num, 2).setTextAlignment(Qt.AlignCenter)
                        self.main_window.ui.outputsTable.item(row_num, 2).setBackground(cell_colour)
                        self.main_window.ui.outputsTable.item(row_num, 2).setForeground(Colours.BLACK)

                    # Check if this output has changed altered state.
                    if changed_altered_outputs[word] & bitmask:
                        cell_colour = Colours.APRICOT if altered_outputs[word] & bitmask else Colours.BEIGE
                        self.main_window.ui.outputsTable.item(row_num, 1).setBackground(cell_colour)

        except Exception as e:
            print(f"E2: {__file__}: {e}")