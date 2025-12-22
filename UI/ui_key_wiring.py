# Local application imports.
from Enums.enum_adc import ADCX04
from Enums.enum_gpio import InputsX01, InputsX04, OutputsX04
from Enums.enum_msg import MsgMode, SrcDest
from Utilities.messages import unpackMessage


class UIKeyWiring:
    """
    Class for the key wiring diagram
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        self.key_inputs_prev_state = [0] * 8
        self.key_outputs_prev_state = [0] * 8


    def updateKeyWiringInputLEDs(self, msg):
        """
        Updates the key wiring diagram LEDs that are input monitoring points

        @param msg: The message to unpack
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                header, gpio_payload = unpackMessage("9I", msg)

                source = header[2]
                num_inputs = gpio_payload[0]    # The total number of inputs to loop through and retrive data from in this message.
                inputs = gpio_payload[1:5]      # Where the input data is located, there is a buffer of 4 words containing up to 32 inputs each.
                word_inputs = [0] * 4           # 4 words capable of holding up to 32 inputs each.

                input_led_map_X01 = {
                    InputsX01.INPUT_MON_BISTABLE_FEED:         self.main_window.ui.bistableFeedLED,
                    InputsX01.INPUT_MON_BISTABLE_RTN:          self.main_window.ui.bistableReturnLED,
                    InputsX01.INPUT_MON_OVERRIDE:              self.main_window.ui.swivelOverrideLED,
                }

                input_led_map_X04 = {
                    InputsX04.INPUT_MON_ULTIMATE_RETURN:       self.main_window.ui.ultimateLED,
                    InputsX04.INPUT_MON_OSG_RETURN:            self.main_window.ui.osgReturnLED,
                    InputsX04.INPUT_MON_BOTTOM_FOOTREST:       self.main_window.ui.bottomFootrestLED,
                    InputsX04.INPUT_MON_HANDING_PLUG_2:        self.main_window.ui.handing2LED,
                    InputsX04.INPUT_MON_HANDING_PLUG_4:        self.main_window.ui.handing4LED,
                    InputsX04.INPUT_RIGHT_STOP_LIMIT:          self.main_window.ui.rightStopLED,
                    InputsX04.INPUT_MON_RIGHT_SKATE:           self.main_window.ui.rightSkateLED,
                    InputsX04.INPUT_MON_RIGHT_SAFETY:          self.main_window.ui.rightSafetyLED,
                    InputsX04.INPUT_LEFT_STOP_LIMIT:           self.main_window.ui.leftStopLED,
                    InputsX04.INPUT_MON_LEFT_SKATE:            self.main_window.ui.leftSkateLED,
                    InputsX04.INPUT_MON_LEFT_SAFETY:           self.main_window.ui.leftSafetyLED,
                    InputsX04.INPUT_MON_RELAY_COIL:            self.main_window.ui.relayCoilMonitorLED,
                }

                if SrcDest(source) == SrcDest.SRC_DEST_X04:
                    prev_table_offset = 0 # First 4 words are X04 inputs.
                    input_led_map = input_led_map_X04
                    enum_type = InputsX04
                else:
                    prev_table_offset = 4 # Last 4 words are X01 inputs.
                    input_led_map = input_led_map_X01
                    enum_type = InputsX01

                # Check for any bits that have changed state from the previous reading.
                for i in range(4):
                    word_inputs[i] = self.key_inputs_prev_state[i + prev_table_offset] ^ inputs[i] # This is a 'change mask', bits that have changed are set to 1, else 0.
                    self.key_inputs_prev_state[i + prev_table_offset] = inputs[i] # Update previous with current data.

                # Loop through each input and update state (if changed).
                for i in range(num_inputs):
                    word = i // 32          # Calculates which word contains the i-th input
                    bit = i & 31            # Locate bit position of input.
                    bitmask = 1 << bit      # Creates mask with a 1 in the position of the input.

                    # Check if input has changed state.
                    if word_inputs[word] & bitmask:
                        input_id = word * 32 + bit  # Calculate the input ID.
                        enum_input_id = enum_type(input_id)
                        if enum_input_id in input_led_map:
                            check = True if inputs[word] & bitmask else False  # Get the new value of the input that has changed.
                            input_led_map[enum_input_id].setChecked(check)  # Update the corresponding radio button.

        except Exception as e:
            print(f"E1: {__file__}: {e}")


    def updateKeyWiringOutputLEDs(self, msg):
        """
        Updates the key wiring diagram LEDs that are outputs

        @param msg: The message to unpack
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                header, gpio_payload = unpackMessage("9I", msg)

                source = header[2]
                num_outputs = gpio_payload[0]   # The total number of outputs to loop through and retrive data from in this message.
                outputs = gpio_payload[1:5]     # Where the output data is located, there is a buffer of 4 words containing up to 32 outputs each.
                word_outputs = [0] * 4          # 4 words capable of holding up to 32 outputs each.

                output_led_map_X04 = {
                    OutputsX04.OUTPUT_SW_CALL_UP:               self.main_window.ui.callUpLED,
                    OutputsX04.OUTPUT_SW_CALL_DOWN:             self.main_window.ui.callDownLED,
                }

                if SrcDest(source) == SrcDest.SRC_DEST_X04:
                    prev_table_offset = 0 # First 4 words are X04 outputs.
                    output_led_map = output_led_map_X04
                    enum_type = OutputsX04
                else:
                    return

                # Check for any bits that have changed state from the previous reading.
                for i in range(4):
                    word_outputs[i] = self.key_outputs_prev_state[i + prev_table_offset] ^ outputs[i] # This is a 'change mask', bits that have changed are set to 1, else 0.
                    self.key_outputs_prev_state[i + prev_table_offset] = outputs[i] # Update previous with current data.

                # Loop through each output and update state (if changed).
                for i in range(num_outputs):
                    word = i // 32          # Calculates which word contains the i-th output
                    bit = i & 31            # Locate bit position of output.
                    bitmask = 1 << bit      # Creates mask with a 1 in the position of the output.

                    # Check if output has changed state.
                    if word_outputs[word] & bitmask:
                        output_id = word * 32 + bit  # Calculate the output ID.
                        enum_output_id = enum_type(output_id)
                        if enum_output_id in output_led_map:
                            check = True if outputs[word] & bitmask else False  # Get the new value of the output that has changed.
                            output_led_map[enum_output_id].setChecked(check)  # Update the corresponding radio button.

        except Exception as e:
            print(f"E2: {__file__}: {e}")


    def updateKeyWiringOutputADC(self, msg):
        """
        Updates the key wiring diagram LEDs that are ADC

        @param msg: The message to unpack
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                header, adc_payload = unpackMessage("I30H", msg)

                source = header[2]
                num_channels = adc_payload[0]
                data = adc_payload[1:] # Skip 1st index which is count

                adc_led_map_X04 = {
                    ADCX04.ADC_ANA_LFR_MON:             self.main_window.ui.leftFootrestLED,
                    ADCX04.ADC_ANA_RFR_MON:             self.main_window.ui.rightFootrestLED,
                }

                if SrcDest(source) == SrcDest.SRC_DEST_X04:
                    adc_map = adc_led_map_X04
                    enum_type = ADCX04
                else:
                    return

                for i in range(num_channels):
                    adc_id = enum_type(i)
                    if adc_id in adc_map:
                        #raw_index = data[i * 2]
                        scaled_value = data[(i * 2) + 1]
                        check = True if scaled_value > 23000 else False
                        adc_map[adc_id].setChecked(check)

        except Exception as e:
            print(f"E3: {__file__}: {e}")