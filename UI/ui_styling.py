# Third party imports.
from PySide6.QtGui import QColor


class Colours:
    """
    Class to store all user interface colours.
    Provides named colour constants for consistent UI styling throughout the application.
    """
    AMBER                   = QColor("#FFC800")
    APRICOT                 = QColor("#F2C46F")
    BABY_BLUE               = QColor("#B5D7F9")
    BEIGE                   = QColor("#E6E2BE")
    BLACK                   = QColor("#000000")
    BRIGHT_CYAN             = QColor("#00CFE4")
    CANARY_YELLOW           = QColor("#FFE200")
    CORAL_PINK              = QColor("#FF787D")
    ELECTRIC_LIME           = QColor("#EBFB3D")
    FOREST_GREEN            = QColor("#004B00")
    GARNET                  = QColor("#C70000")
    GOLD                    = QColor("#FFD700")
    GOLDEN_YELLOW           = QColor("#FFC12E")
    ICTERINE                = QColor("#F6FF68")
    KELLY_GREEN             = QColor("#2CEB6C")
    LAVENDER                = QColor("#E09EF2")
    LIGHT_GREY              = QColor("#BABABA")
    LIGHT_PINK              = QColor("#FFA2A7")
    LIME_GREEN              = QColor("#B2CF4F")
    MARIGOLD                = QColor("#EBA82C")
    MEDIUM_GREY             = QColor("#7F7F7F")
    PALE_GREEN              = QColor("#A6FFA7")
    PASTEL_PINK             = QColor("#FFB4D8")
    PERIWINKLE              = QColor("#C3D4FF")
    ROYAL_BLUE              = QColor("#0033A0")
    WHITE                   = QColor("#FFFFFF")
    WHITE_SMOKE             = QColor("#F6F6F6")
    YELLOW                  = QColor("#FFFF00")


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
    BUTTON_INACTIVE = f"""
    QPushButton {{
        color: {Colours.BLACK.name()};                  /* Text colour black */
        border: 2px solid {Colours.BLACK.name()};       /* Border properties */
        border-radius: 5px;                             /* Curved border */
        background-color: {Colours.LIGHT_PINK.name()};  /* Light pink background */
    }}

    QPushButton:hover {{
        border: 2px solid {Colours.BLACK.name()};       /* Border properties */
        border-radius: 5px;                             /* Curved border */
        background-color: {Colours.PALE_GREEN.name()};  /* Green background */
    }}

    QPushButton:pressed {{
        border: 2px solid {Colours.BLACK.name()};       /* Border properties */
        border-radius: 5px;                             /* Curved border */
        background-color: {Colours.PALE_GREEN.name()};  /* Green background */
    }}
    """

    BUTTON_ACTIVE = f"""
    QPushButton {{
        color: {Colours.BLACK.name()};                  /* Text colour black */
        border: 2px solid {Colours.BLACK.name()};       /* Border properties */
        border-radius: 5px;                             /* Curved border */
        background-color: {Colours.PALE_GREEN.name()};  /* Green background */
        font-weight: bold;                              /* Bold text when selected button */
    }}
    """

    BUTTON_FLASH_ON = f"""
    QPushButton {{
        color: {Colours.BLACK.name()};                  /* Text colour black */
        border: 2px solid {Colours.BLACK.name()};       /* Border properties */
        border-radius: 5px;                             /* Curved border */
        background-color: {Colours.PALE_GREEN.name()};  /* Green background */
    }}
    """

    BUTTON_FLASH_OFF = f"""
    QPushButton {{
        color: {Colours.BLACK.name()};                  /* Text colour black */
        border: 2px solid {Colours.BLACK.name()};       /* Border properties */
        border-radius: 5px;                             /* Curved border */
        background-color: {Colours.LIGHT_PINK.name()};  /* Light pink background */
    }}
    """