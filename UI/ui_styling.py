# Third party imports.
from PySide6.QtGui import QColor


class Colours:
    """
    Class to store all user interface colours.
    Provides named colour constants for consistent UI styling throughout the application.
    """
    BLACK                   = QColor("#000000")  # Black
    DEFAULT                 = QColor("#E6E2BE")  # Yellow/Beige
    GRIDLINES               = QColor("#7F7F7F")  # Grey
    HIGHLIGHT_MAP_POINT     = QColor("#A6FFA7")  # Green
    LOGIC_0                 = QColor("#FFA2A7")  # Red
    LOGIC_1                 = QColor("#A6FFA7")  # Green
    MAP_DISABLED            = QColor("#FFA2A7")  # Red
    MAP_EDITING             = QColor("#FFB037")  # Orange
    MAP_FINDING             = QColor("#FFB4D8")  # Pink
    MAP_RESTRICTED          = QColor("#A6FFA7")  # Green
    ALTER                   = QColor("#F2C46F")  # Orange
    RED                     = QColor("#FF0000")  # Red
    SATURATED_RAW           = QColor("#FFA2A7")  # Red
    ECU1_ID                 = QColor("#C70000")  # Red
    ECU2_ID                 = QColor("#0033A0")  # Blue


class CSS:
    """
    Class to store CSS tags and HTML entities for UI text formatting.
    """
    END_STYLE       = '</span>'
    GREATER         = '&gt;'
    LESS            = '&lt;'
    START_STYLE     = '<span style="'
    START_STYLE_END = '">'
    WHITE_SPACE     = '&nbsp;'


class Styles:
    """
    Class to store all user interface styles.
    Contains CSS style strings for various UI elements such as buttons.
    """

    BUTTON_INACTIVE = """
    QPushButton {
        color: #000000;                 /* Text colour black */
        border: 2px solid #000000;      /* Border properties */
        border-radius: 5px;             /* Curved border */
        background-color: #FFA2A7;      /* Red background */
    }

    QPushButton:hover {
        border: 2px solid #000000;      /* Border properties */
        border-radius: 5px;             /* Curved border */
        background-color: #A6FFA7;      /* Green background */
    }

    QPushButton:pressed {
        border: 2px solid #000000;      /* Border properties */
        border-radius: 5px;             /* Curved border */
        background-color: #A6FFA7;      /* Green background */
    }
    """

    BUTTON_ACTIVE = """
    QPushButton {
        color: #000000;                 /* Text colour black */
        border: 2px solid #000000;      /* Border properties */
        border-radius: 5px;             /* Curved border */
        background-color: #A6FFA7;      /* Green background */
        font-weight: bold;              /* Bold text when selected button */
    }
    """

    BUTTON_FLASH_ON = """
    QPushButton {
        color: #000000;                 /* Text colour black */
        border: 2px solid #000000;      /* Border properties */
        border-radius: 5px;             /* Curved border */
        background-color: #A6FFA7;      /* Green background */
    }
    """

    BUTTON_FLASH_OFF = """
    QPushButton {
        color: #000000;                 /* Text colour black */
        border: 2px solid #000000;      /* Border properties */
        border-radius: 5px;             /* Curved border */
        background-color: #FFA2A7;      /* Red background */
    }
    """