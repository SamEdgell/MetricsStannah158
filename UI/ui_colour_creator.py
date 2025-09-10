from datetime import datetime
from metrics_handler import CSS_STYLE, MessageStyleCode
from UI.ui_styling import CSS


class UIColourCreator:
    """
    Class for the colour creator.
    """

    def __init__(self, main_Window):
        """
        Initialises the ColourCreator class.

        Args:
            main_Window: Reference to the main window, used for accessing UI elements.
        """
        self.main_window = main_Window
        self.main_window.ui.clearPaletteConsoleButton.clicked.connect(self.clearConsole)
        self.main_window.ui.appendButton.clicked.connect(self.appendText)
        self.main_window.ui.fgWhiteButton.clicked.connect(lambda: self.setSliders("W", True))
        self.main_window.ui.fgBlackButton.clicked.connect(lambda: self.setSliders("B", True))
        self.main_window.ui.fgResetButton.clicked.connect(lambda: self.setSliders("R", True))
        self.main_window.ui.bgWhiteButton.clicked.connect(lambda: self.setSliders("W", False))
        self.main_window.ui.bgBlackButton.clicked.connect(lambda: self.setSliders("B", False))
        self.main_window.ui.bgDefButton.clicked.connect(lambda:   self.setSliders("D", False))
        self.main_window.ui.bgResetButton.clicked.connect(lambda: self.setSliders("R", False))

        self.main_window.ui.bgRedSlider.valueChanged.connect(lambda:   (self.updateGroupBoxColour("bg"), self.updateTestTable()))
        self.main_window.ui.bgGreenSlider.valueChanged.connect(lambda: (self.updateGroupBoxColour("bg"), self.updateTestTable()))
        self.main_window.ui.bgBlueSlider.valueChanged.connect(lambda:  (self.updateGroupBoxColour("bg"), self.updateTestTable()))
        self.main_window.ui.fgRedSlider.valueChanged.connect(lambda:   (self.updateGroupBoxColour("fg"), self.updateTestTable()))
        self.main_window.ui.fgGreenSlider.valueChanged.connect(lambda: (self.updateGroupBoxColour("fg"), self.updateTestTable()))
        self.main_window.ui.fgBlueSlider.valueChanged.connect(lambda:  (self.updateGroupBoxColour("fg"), self.updateTestTable()))

        self.main_window.ui.bgHexLine.returnPressed.connect(lambda: self.processHexInput("bg"))
        self.main_window.ui.fgHexLine.returnPressed.connect(lambda: self.processHexInput("fg"))

        self.bg_colour = {"r": 0, "g": 0, "b": 0}
        self.fg_colour = {"r": 0, "g": 0, "b": 0}

        self.sequence_number = 0

        self.updateGroupBoxColour("bg")
        self.updateGroupBoxColour("fg")
        self.updateTestTable()


    def clearConsole(self):
        """
        Clears all contents from the colour palette console, also clears the sequence number.
        """
        self.sequence_number = 0
        self.main_window.ui.colourPaletteLog.clear()


    def setSliders(self, colour, foreground):
        """
        Sets the sliders to a specific location requested via button.

        Args:
            colour:     The colour to set the sliders to.
            foreground: True if to change foreground colour, else background colour.
        """
        if foreground:
            sliders = [self.main_window.ui.fgRedSlider, self.main_window.ui.fgGreenSlider, self.main_window.ui.fgBlueSlider]
        else:
            sliders = [self.main_window.ui.bgRedSlider, self.main_window.ui.bgGreenSlider, self.main_window.ui.bgBlueSlider]

        if colour == "W":    # White.
            values = [255, 255, 255]
        elif colour == "B":  # Black.
            values = [0, 0, 0]
        elif colour == "D":  # Default Yellow/Beige.
            values = [230, 226, 190]
        elif colour == "R":  # Reset (default to 128 for neutral gray).
            values = [128, 128, 128]
        else:
            raise ValueError("Invalid colour code. Use 'W', 'B', or 'R'.")

        for slider, value in zip(sliders, values):
            slider.setValue(value)


    def updateGroupBoxColour(self, box):
        """
        Updates the group box colour based on RGB slider values.

        Args:
            box: The group box to change colour.
        """
        if box == "bg":
            r = self.main_window.ui.bgRedSlider.value()
            g = self.main_window.ui.bgGreenSlider.value()
            b = self.main_window.ui.bgBlueSlider.value()
            box = [self.main_window.ui.bgColourBox, self.main_window.ui.testBox]
            hex_line = self.main_window.ui.bgHexLine
        else:
            r = self.main_window.ui.fgRedSlider.value()
            g = self.main_window.ui.fgGreenSlider.value()
            b = self.main_window.ui.fgBlueSlider.value()
            box = self.main_window.ui.fgColourBox
            hex_line = self.main_window.ui.fgHexLine

        # Update hex display.
        hex_colour = f"#{r:02X}{g:02X}{b:02X}"
        hex_line.setText(hex_colour)

        widgets_to_style = box if isinstance(box, list) else [box]
        for widget in widgets_to_style:
            # Update the appropriate colour box.
            widget.setStyleSheet(f"""
                                QGroupBox {{
                                    border: 2px solid black;
                                    border-radius: 5px;
                                    background-color: {hex_colour};
                                    margin-top: 25px;
                                }}

                                QGroupBox::title {{
                                    subcontrol-origin: margin;
                                    subcontrol-position: top-center;
                                    top: -5px;
                                    background-color: transparent;
                                    text-align: center;
                                    width: 100%;
                                    color: black;
                                }}
                                """)

        self.updateTextBox()


    def updateTestTable(self):
        """
        Updates the test table colour based on RGB slider values.
        """
        r = self.main_window.ui.fgRedSlider.value()
        g = self.main_window.ui.fgGreenSlider.value()
        b = self.main_window.ui.fgBlueSlider.value()

        # Update hex display.
        hex_colour = f"#{r:02X}{g:02X}{b:02X}"

        self.main_window.ui.testTable.setStyleSheet(f"""
                                                    QTableWidget {{
                                                    border: 2px solid black;
                                                    background: #E6E2BE;
                                                    }}

                                                    QHeaderView::section {{
                                                        background-color: {hex_colour};
                                                        border: none;
                                                        border-right: 1px solid black;
                                                        border-bottom: 2px solid black;
                                                        color: black;
                                                    }}
                                                    """)


    def updateTextBox(self):
        """
        Updates the text box with the slider values.
        """
        self.bg_colour["r"], self.bg_colour["g"], self.bg_colour["b"] = self.main_window.ui.bgRedSlider.value(), self.main_window.ui.bgGreenSlider.value(), self.main_window.ui.bgBlueSlider.value()
        self.fg_colour["r"], self.fg_colour["g"], self.fg_colour["b"] = self.main_window.ui.fgRedSlider.value(), self.main_window.ui.fgGreenSlider.value(), self.main_window.ui.fgBlueSlider.value()

        self.main_window.ui.textLine.setStyleSheet(f"""
                                                    QLineEdit {{
                                                        color: rgb({self.fg_colour["r"]}, {self.fg_colour["g"]}, {self.fg_colour["b"]});
                                                        background-color: rgb({self.bg_colour["r"]}, {self.bg_colour["g"]}, {self.bg_colour["b"]});
                                                        border: 1px solid black;
                                                        border-radius: 5px;
                                                    }}
                                                    """)


    def appendText(self):
        """
        Appends the current text to the test console log with the background and text colour changes.
        """
        # Generate timestamp with alternating styles.
        time_stamp_style = CSS_STYLE.get(
            MessageStyleCode.TIME_STAMP_EVEN if self.sequence_number % 2 == 0 else MessageStyleCode.TIME_STAMP_ODD
        )
        timestamp = f"{CSS.START_STYLE}{time_stamp_style}{CSS.START_STYLE_END}" \
                    f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]}{CSS.END_STYLE}" \
                    f"{CSS.WHITE_SPACE}" \
                    f"{CSS.START_STYLE}{CSS_STYLE.get(MessageStyleCode.SEQUENCE_NUMBER)}{CSS.START_STYLE_END}" \
                    f"{self.sequence_number:0X}{CSS.END_STYLE}{CSS.WHITE_SPACE}"

        # Generate text and background hex colours.
        fg_hex = f"#{self.fg_colour['r']:02X}{self.fg_colour['g']:02X}{self.fg_colour['b']:02X}"
        bg_hex = f"#{self.bg_colour['r']:02X}{self.bg_colour['g']:02X}{self.bg_colour['b']:02X}"

        # Combine styles and text.
        text_style = f"color: {fg_hex}; background-color: {bg_hex};"
        test_string = f"{CSS.START_STYLE}{text_style}{CSS.START_STYLE_END}" \
                      f"{self.main_window.ui.textLine.text()}{CSS.END_STYLE} FG: {fg_hex} BG: {bg_hex}"

        # Append to the log.
        self.main_window.ui.colourPaletteLog.append(f"{timestamp}{test_string}")
        self.sequence_number += 1


    def processHexInput(self, box):
        """
        Takes the pasted in hex code and adjusts the sliders to the new value.

        Args:
            box: The group box to update the colour.
        """
        try:
            if box == "bg":
                hex_text = self.main_window.ui.bgHexLine.text().strip()
                red_slider = self.main_window.ui.bgRedSlider
                green_slider = self.main_window.ui.bgGreenSlider
                blue_slider = self.main_window.ui.bgBlueSlider
            else:
                hex_text = self.main_window.ui.fgHexLine.text().strip()
                red_slider = self.main_window.ui.fgRedSlider
                green_slider = self.main_window.ui.fgGreenSlider
                blue_slider = self.main_window.ui.fgBlueSlider

            # Remove '#' if present.
            if hex_text.startswith("#"):
                hex_text = hex_text[1:]

            # Handle different hex formats (3 or 6 characters).
            if len(hex_text) == 3:
                # Convert 3-digit hex to 6-digit (each digit is repeated).
                r = int(hex_text[0] + hex_text[0], 16)
                g = int(hex_text[1] + hex_text[1], 16)
                b = int(hex_text[2] + hex_text[2], 16)
            elif len(hex_text) == 6:
                # Standard 6-digit hex.
                r = int(hex_text[0:2], 16)
                g = int(hex_text[2:4], 16)
                b = int(hex_text[4:6], 16)
            else:
                # Invalid format - don't update.
                return

            # Block signals to prevent recursive updates while setting sliders.
            red_slider.blockSignals(True)
            green_slider.blockSignals(True)
            blue_slider.blockSignals(True)

            # Update the sliders
            red_slider.setValue(r)
            green_slider.setValue(g)
            blue_slider.setValue(b)

            # Unblock signals
            red_slider.blockSignals(False)
            green_slider.blockSignals(False)
            blue_slider.blockSignals(False)

            # Update the colour box manually since signals were blocked.
            self.updateGroupBoxColour(box)

        except Exception as e:
            print(f"E1: {__file__}: {e}")