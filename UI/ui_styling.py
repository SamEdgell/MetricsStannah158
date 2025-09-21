from PySide6 import QtGui


class Colours:
    """
    Class to store all user interface colours.
    Provides named colour constants for consistent UI styling throughout the application.
    """
    BLACK                   = QtGui.QColor("#000000")  # Black
    DEFAULT                 = QtGui.QColor("#E6E2BE")  # Yellow/Beige
    GRIDLINES               = QtGui.QColor("#7F7F7F")  # Grey
    HIGHLIGHT_MAP_POINT     = QtGui.QColor("#A6FFA7")  # Green
    LOGIC_0                 = QtGui.QColor("#FFA2A7")  # Red
    LOGIC_1                 = QtGui.QColor("#A6FFA7")  # Green
    MAP_DISABLED            = QtGui.QColor("#FFA2A7")  # Red
    MAP_EDITING             = QtGui.QColor("#FFB037")  # Orange
    MAP_FINDING             = QtGui.QColor("#FFB4D8")  # Pink
    MAP_RESTRICTED          = QtGui.QColor("#A6FFA7")  # Green
    ALTER                   = QtGui.QColor("#F2C46F")  # Orange
    RED                     = QtGui.QColor("#FF0000")  # Red
    SATURATED_RAW           = QtGui.QColor("#FFA2A7")  # Red
    ECU1_ID                 = QtGui.QColor("#C70000")  # Red
    ECU2_ID                 = QtGui.QColor("#0033A0")  # Blue


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