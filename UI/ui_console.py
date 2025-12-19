# Standard library imports.
import os
from datetime import datetime

# Third party imports.
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QFileDialog

# Local application imports.
from Utilities.metrics_handler import formatTimestamp


class UIConsole:
    """
    Class for the console log.
    Provides methods for displaying, clearing, and saving messages in the application's console logs.
    """

    def __init__(self, main_window):
        """
        Initialises the UIConsole class.

        Args:
            main_window: Reference to the main window, used for accessing UI elements.
        """
        self.main_window = main_window
        self.main_window.ui.clearPrimaryConsoleButton.clicked.connect(self.clearConsole)
        self.main_window.ui.savePrimaryConsoleButton.clicked.connect(self.saveConsoleContents)
        self.main_window.ui.clearSecondaryConsoleButton.clicked.connect(self.clearConsole)
        self.main_window.ui.saveSecondaryConsoleButton.clicked.connect(self.saveConsoleContents)
        self.main_window.ui.clearTertiaryConsoleButton.clicked.connect(self.clearConsole)
        self.main_window.ui.saveTertiaryConsoleButton.clicked.connect(self.saveConsoleContents)

        self.debug_sequence_number = 0


    def clearConsole(self):
        """
        Clears all contents from the current console.
        """
        if self.main_window.ui.consoleTab.currentIndex() == 0:
            self.main_window.ui.primaryConsoleLog.clear()
        elif self.main_window.ui.consoleTab.currentIndex() == 1:
            self.main_window.ui.secondaryConsoleLog.clear()
        else:
            self.main_window.ui.tertiaryConsoleLog.clear()


    def logPrimaryConsole(self, msg):
        """
        Prints the received message to the primary console.

        Args:
            msg: Message to print to primary console.
        """
        if msg:
            self.main_window.ui.primaryConsoleLog.append(msg)


    def logSecondaryConsole(self, msg):
        """
        Prints the received message to the secondary console.

        Args:
            msg: Message to print to secondary console.
        """
        if msg:
            self.main_window.ui.secondaryConsoleLog.append(msg)


    def logDebugConsole(self, msg):
        """
        Prints the received message to the debug console.

        Args:
            msg: Message to print to debug console.
        """
        if msg:
            timestamp_string = formatTimestamp(self.debug_sequence_number)
            timestamp_string += msg
            self.main_window.ui.tertiaryConsoleLog.append(timestamp_string)
            self.debug_sequence_number += 1


    def saveConsoleContents(self):
        """
        Saves the contents of the current console log to an HTML file.
        """
        if self.main_window.ui.consoleTab.currentIndex() == 0:
            console = self.main_window.ui.primaryConsoleLog
            log_type = "X04"
        elif self.main_window.ui.consoleTab.currentIndex() == 1:
            console = self.main_window.ui.secondaryConsoleLog
            log_type = "X01"
        else:
            console = self.main_window.ui.tertiaryConsoleLog
            log_type = "DEBUG"

        if not console.toPlainText().strip():
            print(f"Error! {log_type} Console Log Empty. Nothing to Save.")
            return

        snapshots_dir = "Snapshots"
        if not os.path.exists(snapshots_dir):
            os.makedirs(snapshots_dir)

        # Create default filename with timestamp.
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{log_type}_Snapshot_{timestamp}.html"
        file_path = os.path.join(snapshots_dir, filename)

        # Open file dialog.
        chosen_file_path, _ = QFileDialog.getSaveFileName(self.main_window, "Save Console Log", file_path, "HTML Files (*.html);;All Files (*)")

        if chosen_file_path:
            try:
                # Get HTML content directly from QTextEdit.
                html_content = console.toHtml()

                # Get the background colour from the consoles palette.
                bg_colour = console.palette().color(QPalette.Base).name()

                # Inject CSS into the HTML to set the background colour.
                if "<head>" in html_content and "</head>" in html_content:
                    style_tag = f"<style>body{{background-color: {bg_colour};}}</style>"
                    # Insert style tag just before close 'head' tag.
                    html_content = html_content.replace("</head>", f"{style_tag}</head>", 1)

                # Save to file.
                with open(chosen_file_path, 'w', encoding='utf-8') as file:
                    file.write(html_content)

                print(f"{log_type} Snapshot Saved: {chosen_file_path}")

            except Exception as e:
                print(f"E1: {__file__}: {e}")