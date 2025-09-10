from PySide6.QtWidgets import QFrame, QLabel, QProgressBar, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from UI.ui_custom_widgets import ScalableLabel


class SplashScreen(QWidget):
    """
    Splash screen window for the Metrics application.
    Inherits from QWidget to provide a styled, frameless window with a logo, loading text, and a progress bar to indicate application startup progress.
    """

    def __init__(self):
        """
        Initialises the splash screen.
        """
        super().__init__() # Initialise the parent QWidget.
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground) # Make window background transparent.
        self.setFixedSize(400, 250)

        # Create the main container frame and enable CSS styling.
        container = QFrame(self)
        container.setObjectName("container")

        # Set stylesheet for the splash screen.
        self.setStyleSheet("""
            #container {
                background-color: #BABABA;
                border: 2px solid #000000;
                border-radius: 15px;
            }
            #metrics_image_frame {
                border: 2px solid #000000;
                border-radius: 10px;
                margin-top: 8px;
            }
            QLabel {
                color: #000000;
                font-size: 16px;
                font-weight: bold;
                border: none;
                background-color: transparent;
            }
            QProgressBar {
                border: 2px solid #000000;
                border-radius: 8px;
                text-align: center;
                color: #000000;
                background-color: #D3D3D3;
            }
            QProgressBar::chunk {
                background-color: #A6FFA7;
                border-radius: 8px;
            }
        """)

        # Vertical layout for arranging all widgets in the container.
        splash_screen = QVBoxLayout(container)
        splash_screen.setContentsMargins(0, 12, 0, 0)

        # Create the Metrics logo frame.
        metrics_image_frame = QFrame(container)
        metrics_image_frame.setObjectName("metrics_image_frame")
        metrics_image_frame.setFixedSize(364, 92)

        # Layout to ensure the logo label fills the image frame.
        image_frame_layout = QVBoxLayout(metrics_image_frame)
        image_frame_layout.setContentsMargins(0, 0, 0, 0)

        # Add the scalable logo label to the image frame.
        logo_label = ScalableLabel(metrics_image_frame)
        pixmap = QPixmap("Images/Metrics-Logo.png")
        logo_label.setPixmap(pixmap)
        image_frame_layout.addWidget(logo_label)

        # Add the logo frame to the splash screen layout.
        splash_screen.addWidget(metrics_image_frame, 0, Qt.AlignCenter)

        # Create a frame to hold the loading text label and set its fixed height.
        label_frame = QFrame(container)
        label_frame.setFixedHeight(65)

        # Layout for the label frame, centring the label.
        label_layout = QVBoxLayout(label_frame)
        label_layout.setContentsMargins(0, 25, 0, 0)
        label_layout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        # Create and centre the loading text label.
        self.label = QLabel("Loading MetricsGUI...", label_frame)
        self.label.setAlignment(Qt.AlignCenter)
        label_layout.addWidget(self.label)

        # Add the label frame to the splash screen layout.
        splash_screen.addWidget(label_frame)

        # Create and centre the progress bar, matching the logo frame width.
        self.progress = QProgressBar(self)
        self.progress.setFixedWidth(364)
        self.progress.setRange(0, 100)
        splash_screen.addWidget(self.progress, 0, Qt.AlignCenter)

        # Main layout for the transparent splash window.
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(container)
        self.setLayout(main_layout)


    def set_progress(self, value, text=None):
        """
        Updates the current progress of the progress bar.

        Args:
            value:  The new value to set.
            text:   Optional text to display on the label.
        """
        self.progress.setValue(value)
        if text:
            self.label.setText(text)