# Standard library imports.
import time

# Third party imports.
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

# Local application imports.
from UI.ui_comms import UIComms # Component included here because its scope cannot be limited to one function like the other components.
from UI.ui_main_window import Ui_MainWindow
from Utilities.utils import resource_path


class UIBase(QMainWindow):
    """
    Main application window for Metrics.
    Inherits from QMainWindow and is responsible for setting up the core UI components, loading the main window, and managing the application splash screen and versioning.
    """

    def __init__(self, event_loop, splash):
        """
        Initialises the UI file.

        Args:
            event_loop:     A reference to the main thread's asyncio event loop. This is required to safely schedule function calls from this background thread back to the main async thread, for example, to add a received message to an asyncio.Queue.
            splash:         Reference to the splash screen.
        """
        super().__init__() # Initialise the parent QMainWindow.

        # Store references to the event loop and splash screen.
        self.event_loop = event_loop
        self.splash_screen = splash

        # Splash screen progress.
        self.splash_progress = 0

        # Load the UI.
        self.splash_screen.set_progress(self.splash_progress, "Loading UI...")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtWidgets.QApplication.instance().processEvents() # Forces the Qt event loop to process any pending GUI events immediately.

        # Set the window title and icon, the title contains the version.
        version = self.gatherVersion()
        self.setWindowTitle(f"Metrics - {version}")
        app_icon = QIcon(resource_path("Images/Metrics-App-Icon.png"))
        self.setWindowIcon(app_icon)

        # Prevent resizing of the main window.
        self.setFixedSize(self.width(), self.height())

        # These components do not need to be initialised unless requested by the user.
        self.ui_colour_creator = None
        self.ui_demo = None

        # Load compulsory components separately.
        self.initComponentSet1()


    def gatherVersion(self):
        """
        Gathers the Metrics version from version.txt.

        Returns:
            The version string, if found, else unknown.
        """
        with open(resource_path("General/version.txt"), "r") as f:
            for line in f:
                if line.startswith("VERSION_STRING"):
                    version_string = line.split("=", 1)[1].strip().strip('"')
                    major, minor, patch = version_string.split('.')
                    return f"V{major}.{minor}.{patch}"
        return "Unknown Version"


    def initComponentSet1(self):
        """
        First set of components to be initialised after GUI loads.
        """
        from UI.ui_adc import UIADC
        from UI.ui_console import UIConsole
        from UI.ui_comms import UIComms
        from UI.ui_gpio import UIGPIO
        from UI.ui_panel import UIPanel

        # UIConsole must be initialised before UIComms.
        components = [UIADC, UIConsole, UIGPIO, UIPanel, UIComms] # UIComms is purposely placed at the end here.
        # Allocate 100% of progress to this set.
        self.loadComponents(components, (100 / len(components)))


    def loadComponents(self, components, progress):
        """
        Helper function to set up the components and update the splash screen progress.

        Args:
            components: List of components to load.
            progress:   Progress percentage to allocate to this set.
        """
        for component in components:
            # Update the splash screen before loading component.
            self.splash_progress += progress
            self.splash_screen.set_progress(int(self.splash_progress), f"Loading {component.__name__}...")
            QtWidgets.QApplication.instance().processEvents() # Forces the Qt event loop to process any pending GUI events immediately.

            # Instantiate component (with special case for UIComms) as the event loop is required to be passed to this component.
            attr_name = f"ui_{component.__name__[2:].lower()}"  # Converts UIComms to ui_comms as an example.
            if component is UIComms:
                instance = component(self, self.event_loop)
            else:
                instance = component(self)
            setattr(self, attr_name, instance)

            # Small delay between loading each component so the splash screen progress is visible to the user.
            time.sleep(0.2)