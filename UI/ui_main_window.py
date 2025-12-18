# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QComboBox,
    QFrame, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1867, 1008)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: #BABABA;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.navigationFrame = QFrame(self.centralwidget)
        self.navigationFrame.setObjectName(u"navigationFrame")
        self.navigationFrame.setGeometry(QRect(11, 11, 355, 986))
        font = QFont()
        font.setItalic(False)
        self.navigationFrame.setFont(font)
        self.navigationFrame.setStyleSheet(u"QFrame#navigationFrame{    \n"
"	border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"}")
        self.navigationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ADCIOPageButton = QPushButton(self.navigationFrame)
        self.ADCIOPageButton.setObjectName(u"ADCIOPageButton")
        self.ADCIOPageButton.setGeometry(QRect(19, 117, 68, 48))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.ADCIOPageButton.setFont(font1)
        self.ADCIOPageButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.imageFrame = QFrame(self.navigationFrame)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setGeometry(QRect(19, 18, 317, 83))
        self.imageFrame.setStyleSheet(u"QFrame#imageFrame{\n"
"    background-color: #FFFFFF;\n"
"	border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 10px; /* Rounded corners for the border */\n"
"}")
        self.imageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.testButton1 = QPushButton(self.navigationFrame)
        self.testButton1.setObjectName(u"testButton1")
        self.testButton1.setGeometry(QRect(34, 470, 54, 34))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(7)
        font2.setBold(False)
        self.testButton1.setFont(font2)
        self.testButton1.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.testButton3 = QPushButton(self.navigationFrame)
        self.testButton3.setObjectName(u"testButton3")
        self.testButton3.setGeometry(QRect(150, 470, 54, 34))
        self.testButton3.setFont(font2)
        self.testButton3.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.testButton5 = QPushButton(self.navigationFrame)
        self.testButton5.setObjectName(u"testButton5")
        self.testButton5.setGeometry(QRect(266, 470, 54, 34))
        self.testButton5.setFont(font2)
        self.testButton5.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.testButton4 = QPushButton(self.navigationFrame)
        self.testButton4.setObjectName(u"testButton4")
        self.testButton4.setGeometry(QRect(208, 470, 54, 34))
        self.testButton4.setFont(font2)
        self.testButton4.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.testButton2 = QPushButton(self.navigationFrame)
        self.testButton2.setObjectName(u"testButton2")
        self.testButton2.setGeometry(QRect(92, 470, 54, 34))
        self.testButton2.setFont(font2)
        self.testButton2.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 1px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.colourPalettePageButton = QPushButton(self.navigationFrame)
        self.colourPalettePageButton.setObjectName(u"colourPalettePageButton")
        self.colourPalettePageButton.setGeometry(QRect(102, 117, 68, 48))
        self.colourPalettePageButton.setFont(font1)
        self.colourPalettePageButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.topLine_2 = QFrame(self.navigationFrame)
        self.topLine_2.setObjectName(u"topLine_2")
        self.topLine_2.setGeometry(QRect(18, 181, 317, 2))
        font3 = QFont()
        font3.setKerning(True)
        self.topLine_2.setFont(font3)
        self.topLine_2.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_2.setFrameShape(QFrame.Shape.HLine)
        self.topLine_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.commsTab = QTabWidget(self.navigationFrame)
        self.commsTab.setObjectName(u"commsTab")
        self.commsTab.setGeometry(QRect(19, 787, 317, 150))
        font4 = QFont()
        font4.setBold(True)
        font4.setItalic(True)
        self.commsTab.setFont(font4)
        self.commsTab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.commsTab.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px;\n"
"    margin-top: -2px; /* Adjust to connect selected tab with pane */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 80px; /* Ensures tabs have consistent minimum width */\n"
"    margin-right: 2px; /* Space between tabs */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #A6FFA7;\n"
"    border-bottom: none; /* Hides bottom border to connect with pane */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: #FFA2A7;\n"
"    margin-top: 2px; /* Makes unselected tabs slightly lower */\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: #FFB5B9; /* Slightly lighter red on hover */\n"
"}")
        self.serialTab = QWidget()
        self.serialTab.setObjectName(u"serialTab")
        self.bottomLine = QFrame(self.serialTab)
        self.bottomLine.setObjectName(u"bottomLine")
        self.bottomLine.setGeometry(QRect(8, 74, 295, 2))
        self.bottomLine.setFont(font3)
        self.bottomLine.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.bottomLine.setFrameShape(QFrame.Shape.HLine)
        self.bottomLine.setFrameShadow(QFrame.Shadow.Sunken)
        self.serialComPortBox = QComboBox(self.serialTab)
        self.serialComPortBox.setObjectName(u"serialComPortBox")
        self.serialComPortBox.setGeometry(QRect(82, 11, 75, 21))
        self.serialComPortBox.setStyleSheet(u"QComboBox{\n"
"    color: #000000;             /* Text colour */\n"
"    background: #FFFFFF;        /* Background colour */\n"
"    border: 1px solid black;    /* Border colour */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"}\n"
"QComboBox::drop-down{\n"
"    width: 0px;                 /* Hides the drop-down arrow */\n"
"    border: none;               /* No border for the drop-down */\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: none;                /* Hides the down arrow */\n"
"}")
        self.serialAutoButton = QRadioButton(self.serialTab)
        self.autoManualCommsButtonGroup = QButtonGroup(MainWindow)
        self.autoManualCommsButtonGroup.setObjectName(u"autoManualCommsButtonGroup")
        self.autoManualCommsButtonGroup.addButton(self.serialAutoButton)
        self.serialAutoButton.setObjectName(u"serialAutoButton")
        self.serialAutoButton.setGeometry(QRect(8, 41, 51, 22))
        font5 = QFont()
        font5.setPointSize(9)
        self.serialAutoButton.setFont(font5)
        self.serialAutoButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #FF0000; /* Set background color to red when checked */\n"
"}")
        self.serialAutoButton.setChecked(True)
        self.serialConnectButton = QPushButton(self.serialTab)
        self.serialConnectButton.setObjectName(u"serialConnectButton")
        self.serialConnectButton.setGeometry(QRect(167, 11, 136, 21))
        font6 = QFont()
        font6.setBold(False)
        self.serialConnectButton.setFont(font6)
        self.serialConnectButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.serialStatus = QLineEdit(self.serialTab)
        self.serialStatus.setObjectName(u"serialStatus")
        self.serialStatus.setGeometry(QRect(167, 41, 136, 21))
        self.serialStatus.setStyleSheet(u"QLineEdit {\n"
"    color: #000000; /* Text color */\n"
"    background-color: #FFA2A7; /* Background color */\n"
"    border: 1px solid black; /* Thin black solid border */\n"
"    border-radius: 5px; /* Optional: rounded corners */\n"
"    padding: 5px; /* Adds space around the text */\n"
"    padding-top: 3px; /* Adjusts the padding at the top */\n"
"    padding-bottom: 3px; /* Adjusts the padding at the bottom */\n"
"    line-height: 20px; /* Ensures proper vertical alignment of text */\n"
"}\n"
"")
        self.serialStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.serialStatus.setReadOnly(True)
        self.serialManualButton = QRadioButton(self.serialTab)
        self.autoManualCommsButtonGroup.addButton(self.serialManualButton)
        self.serialManualButton.setObjectName(u"serialManualButton")
        self.serialManualButton.setGeometry(QRect(8, 11, 71, 22))
        self.serialManualButton.setFont(font5)
        self.serialManualButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #FF0000; /* Set background color to red when checked */\n"
"}")
        self.serialManualButton.setChecked(False)
        self.serialTxBytes = QLineEdit(self.serialTab)
        self.serialTxBytes.setObjectName(u"serialTxBytes")
        self.serialTxBytes.setGeometry(QRect(222, 86, 81, 21))
        self.serialTxBytes.setFont(font6)
        self.serialTxBytes.setStyleSheet(u"QLineEdit {\n"
"    color: #000000; /* Text color */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"    border: 1px solid black; /* Thin black solid border */\n"
"    border-radius: 5px; /* Optional: rounded corners */\n"
"    padding: 5px; /* Adds space around the text */\n"
"    padding-top: 3px; /* Adjusts the padding at the top */\n"
"    padding-bottom: 3px; /* Adjusts the padding at the bottom */\n"
"    line-height: 20px; /* Ensures proper vertical alignment of text */\n"
"}\n"
"")
        self.serialTxBytes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.serialTxBytes.setReadOnly(True)
        self.serialRxBytes = QLineEdit(self.serialTab)
        self.serialRxBytes.setObjectName(u"serialRxBytes")
        self.serialRxBytes.setGeometry(QRect(62, 86, 81, 21))
        self.serialRxBytes.setStyleSheet(u"QLineEdit {\n"
"    color: #000000; /* Text color */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"    border: 1px solid black; /* Thin black solid border */\n"
"    border-radius: 5px; /* Optional: rounded corners */\n"
"    padding: 5px; /* Adds space around the text */\n"
"    padding-top: 3px; /* Adjusts the padding at the top */\n"
"    padding-bottom: 3px; /* Adjusts the padding at the bottom */\n"
"    line-height: 20px; /* Ensures proper vertical alignment of text */\n"
"}\n"
"")
        self.serialRxBytes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.serialRxBytes.setReadOnly(True)
        self.serialTxLabel = QLabel(self.serialTab)
        self.serialTxLabel.setObjectName(u"serialTxLabel")
        self.serialTxLabel.setGeometry(QRect(152, 85, 71, 21))
        self.serialTxLabel.setStyleSheet(u"QLabel{\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}")
        self.serialBaudRateBox = QComboBox(self.serialTab)
        self.serialBaudRateBox.setObjectName(u"serialBaudRateBox")
        self.serialBaudRateBox.setGeometry(QRect(82, 41, 75, 21))
        self.serialBaudRateBox.setStyleSheet(u"QComboBox{\n"
"    color: #000000;             /* Text colour */\n"
"    background: #FFFFFF;        /* Background colour */\n"
"    border: 1px solid black;    /* Border colour */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"}\n"
"QComboBox::drop-down{\n"
"    width: 0px;                 /* Hides the drop-down arrow */\n"
"    border: none;               /* No border for the drop-down */\n"
"}\n"
"QComboBox::down-arrow{\n"
"    image: none;                /* Hides the down arrow */\n"
"}")
        self.serialRxLabel = QLabel(self.serialTab)
        self.serialRxLabel.setObjectName(u"serialRxLabel")
        self.serialRxLabel.setGeometry(QRect(8, 85, 51, 21))
        self.serialRxLabel.setStyleSheet(u"QLabel{\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}")
        self.commsTab.addTab(self.serialTab, "")
        self.bluetoothTab = QWidget()
        self.bluetoothTab.setObjectName(u"bluetoothTab")
        self.commsTab.addTab(self.bluetoothTab, "")
        self.WiFiTab = QWidget()
        self.WiFiTab.setObjectName(u"WiFiTab")
        self.commsTab.addTab(self.WiFiTab, "")
        self.authenticateLineEdit = QLineEdit(self.navigationFrame)
        self.authenticateLineEdit.setObjectName(u"authenticateLineEdit")
        self.authenticateLineEdit.setGeometry(QRect(221, 948, 115, 23))
        self.authenticateLineEdit.setStyleSheet(u"QLineEdit {\n"
"    color: #000000; /* Text color */\n"
"    background-color: #FFE200; /* Background color */\n"
"    border: 1px solid black; /* Thin black solid border */\n"
"    border-radius: 5px; /* Optional: rounded corners */\n"
"    padding: 5px; /* Adds space around the text */\n"
"    padding-top: 3px; /* Adjusts the padding at the top */\n"
"    padding-bottom: 3px; /* Adjusts the padding at the bottom */\n"
"    line-height: 20px; /* Ensures proper vertical alignment of text */\n"
"}\n"
"")
        self.authenticateLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.authenticateLineEdit.setReadOnly(True)
        self.heartbeatLED = QRadioButton(self.navigationFrame)
        self.heartbeatLED.setObjectName(u"heartbeatLED")
        self.heartbeatLED.setEnabled(False)
        self.heartbeatLED.setGeometry(QRect(29, 948, 77, 22))
        self.heartbeatLED.setFont(font5)
        self.heartbeatLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #FF0000; /* Set background color to red when checked */\n"
"}")
        self.heartbeatLED.setChecked(False)
        self.heartbeatLED.setAutoExclusive(False)
        self.authenticateButton = QRadioButton(self.navigationFrame)
        self.authenticateButton.setObjectName(u"authenticateButton")
        self.authenticateButton.setGeometry(QRect(124, 948, 89, 22))
        self.authenticateButton.setFont(font5)
        self.authenticateButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #FF0000; /* Set background color to red when checked */\n"
"}")
        self.authenticateButton.setChecked(False)
        self.authenticateButton.setAutoExclusive(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(381, 11, 823, 825))
        self.stackedWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.stackedWidget.setStyleSheet(u"QStackedWidget{    \n"
"	border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"}")
        self.ADCIOPage = QWidget()
        self.ADCIOPage.setObjectName(u"ADCIOPage")
        self.ADCBox = QGroupBox(self.ADCIOPage)
        self.ADCBox.setObjectName(u"ADCBox")
        self.ADCBox.setGeometry(QRect(17, 17, 382, 399))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.ADCBox.setFont(font7)
        self.ADCBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #F2C46F;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.adcTable = QTableWidget(self.ADCBox)
        if (self.adcTable.columnCount() < 5):
            self.adcTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.adcTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.adcTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.adcTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.adcTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.adcTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.adcTable.setObjectName(u"adcTable")
        self.adcTable.setGeometry(QRect(18, 50, 346, 332))
        font8 = QFont()
        font8.setPointSize(7)
        self.adcTable.setFont(font8)
        self.adcTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.adcTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.adcTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;            /* Border of the table */\n"
"    background: #E6E2BE;                /* Background colour of table */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #A0BEF4;          /* Background colour of the header */\n"
"    border: none;                       /* Border of the header */\n"
"    border-right: 1px solid black;      /* Right border of the header. Splits columns visually */\n"
"    border-bottom: 2px solid black;     /* Bottom border of the header */\n"
"    color: black;                       /* Text colour of the header */\n"
"    font-weight: normal;                /* Font weight of the header text */\n"
"}\n"
"QHeaderView::section:last {\n"
"    border-right: none;                 /* Remove the right border from the last header section. This is because of an overlap with the table widget border */\n"
"}")
        self.adcTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.adcTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.adcTable.setAutoScroll(False)
        self.adcTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.adcTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.adcTable.horizontalHeader().setMinimumSectionSize(40)
        self.adcTable.horizontalHeader().setDefaultSectionSize(70)
        self.adcTable.horizontalHeader().setStretchLastSection(False)
        self.adcTable.verticalHeader().setVisible(False)
        self.adcTable.verticalHeader().setMinimumSectionSize(14)
        self.adcTable.verticalHeader().setDefaultSectionSize(14)
        self.resetADCButton = QPushButton(self.ADCBox)
        self.resetADCButton.setObjectName(u"resetADCButton")
        self.resetADCButton.setGeometry(QRect(18, 15, 51, 22))
        self.resetADCButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.alterADCButton = QPushButton(self.ADCBox)
        self.alterADCButton.setObjectName(u"alterADCButton")
        self.alterADCButton.setGeometry(QRect(313, 15, 51, 22))
        self.alterADCButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.inputsBox = QGroupBox(self.ADCIOPage)
        self.inputsBox.setObjectName(u"inputsBox")
        self.inputsBox.setGeometry(QRect(415, 17, 387, 527))
        self.inputsBox.setFont(font7)
        self.inputsBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #F2C46F;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.inputsTable = QTableWidget(self.inputsBox)
        if (self.inputsTable.columnCount() < 4):
            self.inputsTable.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.inputsTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.inputsTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.inputsTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.inputsTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.inputsTable.setObjectName(u"inputsTable")
        self.inputsTable.setGeometry(QRect(18, 50, 351, 460))
        self.inputsTable.setFont(font8)
        self.inputsTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.inputsTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.inputsTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;            /* Border of the table */\n"
"    background: #E6E2BE;                /* Background colour of table */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #A0BEF4;          /* Background colour of the header */\n"
"    border: none;                         /* Border of the header */\n"
"    border-right: 1px solid black;      /* Right border of the header. Splits columns visually */\n"
"    border-bottom: 2px solid black;     /* Bottom border of the header */\n"
"    color: black;                       /* Text colour of the header */\n"
"    font-weight: normal;                  /* Font weight of the header text */\n"
"}\n"
"QHeaderView::section:last {\n"
"    border-right: none;                   /* Remove the right border from the last header section. This is because of an overlap with the table widget border */\n"
"}")
        self.inputsTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.inputsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.inputsTable.setAutoScroll(False)
        self.inputsTable.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.inputsTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.inputsTable.horizontalHeader().setMinimumSectionSize(40)
        self.inputsTable.horizontalHeader().setDefaultSectionSize(88)
        self.inputsTable.horizontalHeader().setStretchLastSection(False)
        self.inputsTable.verticalHeader().setVisible(False)
        self.inputsTable.verticalHeader().setMinimumSectionSize(14)
        self.inputsTable.verticalHeader().setDefaultSectionSize(14)
        self.inputsTable.verticalHeader().setStretchLastSection(False)
        self.alterInputsButton = QPushButton(self.inputsBox)
        self.alterInputsButton.setObjectName(u"alterInputsButton")
        self.alterInputsButton.setGeometry(QRect(318, 14, 51, 22))
        self.alterInputsButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.resetInputsButton = QPushButton(self.inputsBox)
        self.resetInputsButton.setObjectName(u"resetInputsButton")
        self.resetInputsButton.setGeometry(QRect(18, 14, 51, 22))
        self.resetInputsButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.alterInputsButton.raise_()
        self.resetInputsButton.raise_()
        self.inputsTable.raise_()
        self.outputsBox = QGroupBox(self.ADCIOPage)
        self.outputsBox.setObjectName(u"outputsBox")
        self.outputsBox.setGeometry(QRect(17, 430, 382, 305))
        self.outputsBox.setFont(font7)
        self.outputsBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #F2C46F;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.outputsTable = QTableWidget(self.outputsBox)
        if (self.outputsTable.columnCount() < 4):
            self.outputsTable.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.outputsTable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.outputsTable.setObjectName(u"outputsTable")
        self.outputsTable.setGeometry(QRect(18, 50, 346, 230))
        self.outputsTable.setFont(font8)
        self.outputsTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.outputsTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.outputsTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;            /* Border of the table */\n"
"    background: #E6E2BE;                /* Background colour of table */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #A0BEF4;          /* Background colour of the header */\n"
"    border: none;                         /* Border of the header */\n"
"    border-right: 1px solid black;      /* Right border of the header. Splits columns visually */\n"
"    border-bottom: 2px solid black;     /* Bottom border of the header */\n"
"    color: black;                       /* Text colour of the header */\n"
"    font-weight: normal;                  /* Font weight of the header text */\n"
"}\n"
"QHeaderView::section:last {\n"
"    border-right: none;                   /* Remove the right border from the last header section. This is because of an overlap with the table widget border */\n"
"}")
        self.outputsTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.outputsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.outputsTable.setAutoScroll(False)
        self.outputsTable.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.outputsTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.outputsTable.horizontalHeader().setMinimumSectionSize(40)
        self.outputsTable.horizontalHeader().setDefaultSectionSize(88)
        self.outputsTable.horizontalHeader().setStretchLastSection(False)
        self.outputsTable.verticalHeader().setVisible(False)
        self.outputsTable.verticalHeader().setMinimumSectionSize(14)
        self.outputsTable.verticalHeader().setDefaultSectionSize(14)
        self.outputsTable.verticalHeader().setStretchLastSection(False)
        self.resetOutputsButton = QPushButton(self.outputsBox)
        self.resetOutputsButton.setObjectName(u"resetOutputsButton")
        self.resetOutputsButton.setGeometry(QRect(17, 14, 51, 22))
        self.resetOutputsButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.alterOutputsButton = QPushButton(self.outputsBox)
        self.alterOutputsButton.setObjectName(u"alterOutputsButton")
        self.alterOutputsButton.setGeometry(QRect(313, 14, 51, 22))
        self.alterOutputsButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.stackedWidget.addWidget(self.ADCIOPage)
        self.ADCBox.raise_()
        self.outputsBox.raise_()
        self.inputsBox.raise_()
        self.colourPalettePage = QWidget()
        self.colourPalettePage.setObjectName(u"colourPalettePage")
        self.colourPaletteLog = QTextEdit(self.colourPalettePage)
        self.colourPaletteLog.setObjectName(u"colourPaletteLog")
        self.colourPaletteLog.setGeometry(QRect(17, 15, 784, 299))
        font9 = QFont()
        font9.setFamilies([u"Consolas"])
        font9.setPointSize(8)
        self.colourPaletteLog.setFont(font9)
        self.colourPaletteLog.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.colourPaletteLog.setStyleSheet(u"QTextEdit {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 1px; /* Smallest rounded corners for the border */\n"
"    background-color: #E6E2BE; /* Yellowish-beige background color */\n"
"    padding-top: 1px; /* Add padding to the top */\n"
"    padding-bottom: 1px; /* Add padding to the bottom */\n"
"    padding-right: 1px; /* Add padding to the right to move the scrollbar inward */\n"
"	color: black;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #E6E2BE; /* Background color of the scrollbar track */\n"
"    width: 10px; /* Width of the scrollbar */\n"
"    border-radius: 1px; /* Smallest rounded corners for the scrollbar track */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #FFA2A7; /* Background color of the handle */\n"
"    border: 1px solid black; /* Border color of the handle */\n"
"    border-radius: 4px; /* Smallest rounded corners for the handle */\n"
"    min-height: 20px; /* Minimum height of the handle */\n"
"}\n"
"\n"
"QScrol"
                        "lBar::handle:vertical:hover {\n"
"    background: #A6FFA7; /* Change background color to green when hovered */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #A6FFA7; /* Change background color to green when selected */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: #FFFFFF; /* Match the background color of the QTextBrowser */\n"
"    height: 0px; /* Height set to 0 to hide the add-line and sub-line */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* No background for the up-arrow and down-arrow */\n"
"    height: 0px; /* Height set to 0 to hide the up-arrow and down-arrow */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* No background for the add-page and sub-page */\n"
"    border: none; /* Remove any border */\n"
"}")
        self.colourPaletteLog.setReadOnly(True)
        self.fgColourBox = QGroupBox(self.colourPalettePage)
        self.fgColourBox.setObjectName(u"fgColourBox")
        self.fgColourBox.setGeometry(QRect(60, 337, 164, 248))
        font10 = QFont()
        font10.setPointSize(15)
        font10.setBold(True)
        self.fgColourBox.setFont(font10)
        self.fgColourBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: #000000;\n"
"    margin-top: 25px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"	subcontrol-position: top-center;\n"
"    top: -5px;\n"
"    background-color: transparent;\n"
"    text-align: center; /* Force text to be centered */\n"
"    width: 100%; /* Make title span the full width */\n"
"	color: black;\n"
"}")
        self.fgColourBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fgBlueSlider = QSlider(self.fgColourBox)
        self.fgBlueSlider.setObjectName(u"fgBlueSlider")
        self.fgBlueSlider.setGeometry(QRect(111, 50, 22, 160))
        self.fgBlueSlider.setStyleSheet(u"QSlider{\n"
"	background: transparent;\n"
"}\n"
"QSlider::handle {\n"
"    background: #46B8FF;\n"
"    border-radius: 4px;\n"
"}")
        self.fgBlueSlider.setMaximum(255)
        self.fgBlueSlider.setSliderPosition(0)
        self.fgBlueSlider.setOrientation(Qt.Orientation.Vertical)
        self.fgGreenSlider = QSlider(self.fgColourBox)
        self.fgGreenSlider.setObjectName(u"fgGreenSlider")
        self.fgGreenSlider.setGeometry(QRect(72, 50, 22, 160))
        self.fgGreenSlider.setStyleSheet(u"QSlider{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background: #2CEB6C;\n"
"    border-radius: 4px;\n"
"}")
        self.fgGreenSlider.setMaximum(255)
        self.fgGreenSlider.setSliderPosition(0)
        self.fgGreenSlider.setOrientation(Qt.Orientation.Vertical)
        self.fgRedSlider = QSlider(self.fgColourBox)
        self.fgRedSlider.setObjectName(u"fgRedSlider")
        self.fgRedSlider.setGeometry(QRect(32, 50, 22, 160))
        self.fgRedSlider.setStyleSheet(u"QSlider{\n"
"	background: transparent;\n"
"}\n"
"QSlider::handle {\n"
"    background: #F03F3F;\n"
"    border-radius: 4px;\n"
"}")
        self.fgRedSlider.setMaximum(255)
        self.fgRedSlider.setValue(0)
        self.fgRedSlider.setSliderPosition(0)
        self.fgRedSlider.setOrientation(Qt.Orientation.Vertical)
        self.fgRedSlider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.bgColourBox = QGroupBox(self.colourPalettePage)
        self.bgColourBox.setObjectName(u"bgColourBox")
        self.bgColourBox.setGeometry(QRect(592, 337, 164, 248))
        self.bgColourBox.setFont(font10)
        self.bgColourBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: #FFFFFF;\n"
"    margin-top: 25px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"	subcontrol-position: top-center;\n"
"    top: -5px;\n"
"    background-color: transparent;\n"
"    text-align: center; /* Force text to be centered */\n"
"    width: 100%; /* Make title span the full width */\n"
"	color: black;\n"
"}")
        self.bgColourBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bgBlueSlider = QSlider(self.bgColourBox)
        self.bgBlueSlider.setObjectName(u"bgBlueSlider")
        self.bgBlueSlider.setGeometry(QRect(111, 50, 22, 160))
        self.bgBlueSlider.setStyleSheet(u"QSlider{\n"
"	background: transparent;\n"
"}\n"
"QSlider::handle {\n"
"    background: #46B8FF;\n"
"    border-radius: 4px;\n"
"}")
        self.bgBlueSlider.setMaximum(255)
        self.bgBlueSlider.setValue(255)
        self.bgBlueSlider.setOrientation(Qt.Orientation.Vertical)
        self.bgGreenSlider = QSlider(self.bgColourBox)
        self.bgGreenSlider.setObjectName(u"bgGreenSlider")
        self.bgGreenSlider.setGeometry(QRect(72, 50, 22, 160))
        self.bgGreenSlider.setStyleSheet(u"QSlider{\n"
"	background: transparent;\n"
"}\n"
"QSlider::handle {\n"
"    background: #2CEB6C;\n"
"    border-radius: 4px;\n"
"}")
        self.bgGreenSlider.setMaximum(255)
        self.bgGreenSlider.setValue(255)
        self.bgGreenSlider.setOrientation(Qt.Orientation.Vertical)
        self.bgRedSlider = QSlider(self.bgColourBox)
        self.bgRedSlider.setObjectName(u"bgRedSlider")
        self.bgRedSlider.setGeometry(QRect(32, 50, 22, 160))
        self.bgRedSlider.setStyleSheet(u"QSlider{\n"
"	background: transparent;\n"
"}\n"
"QSlider::handle {\n"
"    background: #F03F3F;\n"
"    border-radius: 4px;\n"
"}")
        self.bgRedSlider.setMaximum(255)
        self.bgRedSlider.setValue(255)
        self.bgRedSlider.setOrientation(Qt.Orientation.Vertical)
        self.bgRedSlider.setTickPosition(QSlider.TickPosition.NoTicks)
        self.fgHexLine = QLineEdit(self.colourPalettePage)
        self.fgHexLine.setObjectName(u"fgHexLine")
        self.fgHexLine.setGeometry(QRect(86, 600, 113, 22))
        self.fgHexLine.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"	color: black;\n"
"}")
        self.fgHexLine.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bgHexLine = QLineEdit(self.colourPalettePage)
        self.bgHexLine.setObjectName(u"bgHexLine")
        self.bgHexLine.setGeometry(QRect(620, 600, 113, 22))
        self.bgHexLine.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"	color: black;\n"
"}")
        self.bgHexLine.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textLine = QLineEdit(self.colourPalettePage)
        self.textLine.setObjectName(u"textLine")
        self.textLine.setGeometry(QRect(142, 710, 539, 25))
        self.textLine.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.textLine.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.appendButton = QPushButton(self.colourPalettePage)
        self.appendButton.setObjectName(u"appendButton")
        self.appendButton.setGeometry(QRect(384, 750, 54, 34))
        self.appendButton.setFont(font2)
        self.appendButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.fgWhiteButton = QPushButton(self.colourPalettePage)
        self.fgWhiteButton.setObjectName(u"fgWhiteButton")
        self.fgWhiteButton.setGeometry(QRect(237, 366, 29, 26))
        font11 = QFont()
        font11.setFamilies([u"Verdana"])
        font11.setPointSize(7)
        font11.setBold(True)
        self.fgWhiteButton.setFont(font11)
        self.fgWhiteButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.fgBlackButton = QPushButton(self.colourPalettePage)
        self.fgBlackButton.setObjectName(u"fgBlackButton")
        self.fgBlackButton.setGeometry(QRect(237, 400, 29, 26))
        self.fgBlackButton.setFont(font11)
        self.fgBlackButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.fgResetButton = QPushButton(self.colourPalettePage)
        self.fgResetButton.setObjectName(u"fgResetButton")
        self.fgResetButton.setGeometry(QRect(237, 558, 29, 26))
        self.fgResetButton.setFont(font11)
        self.fgResetButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.bgBlackButton = QPushButton(self.colourPalettePage)
        self.bgBlackButton.setObjectName(u"bgBlackButton")
        self.bgBlackButton.setGeometry(QRect(550, 400, 29, 26))
        self.bgBlackButton.setFont(font11)
        self.bgBlackButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.bgWhiteButton = QPushButton(self.colourPalettePage)
        self.bgWhiteButton.setObjectName(u"bgWhiteButton")
        self.bgWhiteButton.setGeometry(QRect(550, 366, 29, 26))
        self.bgWhiteButton.setFont(font11)
        self.bgWhiteButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.bgResetButton = QPushButton(self.colourPalettePage)
        self.bgResetButton.setObjectName(u"bgResetButton")
        self.bgResetButton.setGeometry(QRect(550, 558, 29, 26))
        self.bgResetButton.setFont(font11)
        self.bgResetButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.label = QLabel(self.colourPalettePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(239, 450, 344, 81))
        self.label.setStyleSheet(u"color: black;")
        self.testBox = QGroupBox(self.colourPalettePage)
        self.testBox.setObjectName(u"testBox")
        self.testBox.setGeometry(QRect(332, 545, 157, 121))
        self.testBox.setFont(font7)
        self.testBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"    background-color: #FFFFFF;\n"
"    margin-top: 25px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"	subcontrol-position: top-center;\n"
"    top: -5px;\n"
"    background-color: transparent;\n"
"    text-align: center; /* Force text to be centered */\n"
"    width: 100%; /* Make title span the full width */\n"
"	color: black;\n"
"}")
        self.testTable = QTableWidget(self.testBox)
        if (self.testTable.columnCount() < 2):
            self.testTable.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.testTable.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.testTable.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        self.testTable.setObjectName(u"testTable")
        self.testTable.setGeometry(QRect(17, 50, 123, 53))
        font12 = QFont()
        font12.setPointSize(8)
        self.testTable.setFont(font12)
        self.testTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.testTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.testTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.testTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.testTable.setAutoScroll(False)
        self.testTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.testTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.testTable.horizontalHeader().setMinimumSectionSize(40)
        self.testTable.horizontalHeader().setDefaultSectionSize(60)
        self.testTable.horizontalHeader().setStretchLastSection(False)
        self.testTable.verticalHeader().setVisible(False)
        self.testTable.verticalHeader().setMinimumSectionSize(16)
        self.testTable.verticalHeader().setDefaultSectionSize(16)
        self.bgDefButton = QPushButton(self.colourPalettePage)
        self.bgDefButton.setObjectName(u"bgDefButton")
        self.bgDefButton.setGeometry(QRect(550, 434, 29, 26))
        self.bgDefButton.setFont(font11)
        self.bgDefButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 5px;\n"
"    background-color: #A6FFA7;\n"
"}")
        self.clearPaletteConsoleButton = QPushButton(self.colourPalettePage)
        self.clearPaletteConsoleButton.setObjectName(u"clearPaletteConsoleButton")
        self.clearPaletteConsoleButton.setGeometry(QRect(727, 269, 51, 22))
        self.clearPaletteConsoleButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.stackedWidget.addWidget(self.colourPalettePage)
        self.consoleTab = QTabWidget(self.centralwidget)
        self.consoleTab.setObjectName(u"consoleTab")
        self.consoleTab.setGeometry(QRect(1219, 11, 636, 986))
        self.consoleTab.setFont(font4)
        self.consoleTab.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.consoleTab.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px;\n"
"    margin-top: -2px; /* Adjust to connect selected tab with pane */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 80px; /* Ensures tabs have consistent minimum width */\n"
"    margin-right: 2px; /* Space between tabs */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #A6FFA7;\n"
"    border-bottom: none; /* Hides bottom border to connect with pane */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: #FFA2A7;\n"
"    margin-top: 2px; /* Makes unselected tabs slightly lower */\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: #FFB5B9; /* Slightly lighter red on hover */\n"
"}")
        self.primaryTab = QWidget()
        self.primaryTab.setObjectName(u"primaryTab")
        self.clearPrimaryConsoleButton = QPushButton(self.primaryTab)
        self.clearPrimaryConsoleButton.setObjectName(u"clearPrimaryConsoleButton")
        self.clearPrimaryConsoleButton.setGeometry(QRect(540, 864, 51, 22))
        self.clearPrimaryConsoleButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.savePrimaryConsoleButton = QPushButton(self.primaryTab)
        self.savePrimaryConsoleButton.setObjectName(u"savePrimaryConsoleButton")
        self.savePrimaryConsoleButton.setGeometry(QRect(540, 894, 51, 22))
        self.savePrimaryConsoleButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.primaryConsoleLog = QTextBrowser(self.primaryTab)
        self.primaryConsoleLog.setObjectName(u"primaryConsoleLog")
        self.primaryConsoleLog.setGeometry(QRect(16, 15, 600, 924))
        self.primaryConsoleLog.setFont(font9)
        self.primaryConsoleLog.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.primaryConsoleLog.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 1px; /* Smallest rounded corners for the border */\n"
"    background-color: #E6E2BE; /* Yellowish-beige background color */\n"
"    padding-top: 1px; /* Add padding to the top */\n"
"    padding-bottom: 1px; /* Add padding to the bottom */\n"
"    padding-right: 1px; /* Add padding to the right to move the scrollbar inward */\n"
"	color: black; /* Default black text colour */\n"
"}\n"
"\n"
"/* Vertical scroll bar */\n"
"QScrollBar:vertical {\n"
"    background: #E6E2BE; /* Background color of the scrollbar track */\n"
"    width: 10px; /* Width of the scrollbar */\n"
"    border-radius: 1px; /* Smallest rounded corners for the scrollbar track */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #FFA2A7; /* Background color of the handle */\n"
"    border: 1px solid black; /* Border color of the handle */\n"
"    border-radius: 4px; /* Smallest rounded corners for the handle */\n"
"    min-heigh"
                        "t: 20px; /* Minimum height of the handle */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #A6FFA7; /* Change background color to green when hovered */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #A6FFA7; /* Change background color to green when selected */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; /* Match the background color of the QTextBrowser */\n"
"    height: 0px; /* Height set to 0 to hide the add-line and sub-line */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* No background for the up-arrow and down-arrow */\n"
"    height: 0px; /* Height set to 0 to hide the up-arrow and down-arrow */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* No background for the add-page and sub-page "
                        "*/\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"/* Horizontal scroll bar */\n"
"QScrollBar:horizontal {\n"
"    background: #E6E2BE; /* Background color of the scrollbar track */\n"
"    height: 10px; /* Height of the scrollbar */\n"
"    border-radius: 1px; /* Smallest rounded corners for the scrollbar track */\n"
"	padding-left: 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #FFA2A7; /* Background color of the handle */\n"
"    border: 1px solid black; /* Border color of the handle */\n"
"    border-radius: 4px; /* Smallest rounded corners for the handle */\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #A6FFA7; /* Change background color to green when hovered */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: #A6FFA7; /* Change background color to green when selected */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"  "
                        "  background: none; /* Consistent background for hiding */\n"
"    width: 0px; /* Use width for horizontal scrollbar buttons */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none; /* No background for the arrows */\n"
"    width: 0px; /* Use width for horizontal scrollbar arrows */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none; /* No background for the add-page and sub-page */\n"
"    border: none; /* Remove any border */\n"
"}")
        self.primaryConsoleLog.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.consoleTab.addTab(self.primaryTab, "")
        self.primaryConsoleLog.raise_()
        self.savePrimaryConsoleButton.raise_()
        self.clearPrimaryConsoleButton.raise_()
        self.secondaryTab = QWidget()
        self.secondaryTab.setObjectName(u"secondaryTab")
        self.saveSecondaryConsoleButton = QPushButton(self.secondaryTab)
        self.saveSecondaryConsoleButton.setObjectName(u"saveSecondaryConsoleButton")
        self.saveSecondaryConsoleButton.setGeometry(QRect(540, 894, 51, 22))
        self.saveSecondaryConsoleButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.clearSecondaryConsoleButton = QPushButton(self.secondaryTab)
        self.clearSecondaryConsoleButton.setObjectName(u"clearSecondaryConsoleButton")
        self.clearSecondaryConsoleButton.setGeometry(QRect(540, 864, 51, 22))
        self.clearSecondaryConsoleButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.secondaryConsoleLog = QTextBrowser(self.secondaryTab)
        self.secondaryConsoleLog.setObjectName(u"secondaryConsoleLog")
        self.secondaryConsoleLog.setGeometry(QRect(16, 15, 600, 924))
        self.secondaryConsoleLog.setFont(font9)
        self.secondaryConsoleLog.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.secondaryConsoleLog.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 1px; /* Smallest rounded corners for the border */\n"
"    background-color: #E6E2BE; /* Yellowish-beige background color */\n"
"    padding-top: 1px; /* Add padding to the top */\n"
"    padding-bottom: 1px; /* Add padding to the bottom */\n"
"    padding-right: 1px; /* Add padding to the right to move the scrollbar inward */\n"
"	color: black; /* Default black text colour */\n"
"}\n"
"\n"
"/* Vertical scroll bar */\n"
"QScrollBar:vertical {\n"
"    background: #E6E2BE; /* Background color of the scrollbar track */\n"
"    width: 10px; /* Width of the scrollbar */\n"
"    border-radius: 1px; /* Smallest rounded corners for the scrollbar track */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #FFA2A7; /* Background color of the handle */\n"
"    border: 1px solid black; /* Border color of the handle */\n"
"    border-radius: 4px; /* Smallest rounded corners for the handle */\n"
"    min-heigh"
                        "t: 20px; /* Minimum height of the handle */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #A6FFA7; /* Change background color to green when hovered */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #A6FFA7; /* Change background color to green when selected */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; /* Match the background color of the QTextBrowser */\n"
"    height: 0px; /* Height set to 0 to hide the add-line and sub-line */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* No background for the up-arrow and down-arrow */\n"
"    height: 0px; /* Height set to 0 to hide the up-arrow and down-arrow */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* No background for the add-page and sub-page "
                        "*/\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"/* Horizontal scroll bar */\n"
"QScrollBar:horizontal {\n"
"    background: #E6E2BE; /* Background color of the scrollbar track */\n"
"    height: 10px; /* Height of the scrollbar */\n"
"    border-radius: 1px; /* Smallest rounded corners for the scrollbar track */\n"
"	padding-left: 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #FFA2A7; /* Background color of the handle */\n"
"    border: 1px solid black; /* Border color of the handle */\n"
"    border-radius: 4px; /* Smallest rounded corners for the handle */\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #A6FFA7; /* Change background color to green when hovered */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: #A6FFA7; /* Change background color to green when selected */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"  "
                        "  background: none; /* Consistent background for hiding */\n"
"    width: 0px; /* Use width for horizontal scrollbar buttons */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none; /* No background for the arrows */\n"
"    width: 0px; /* Use width for horizontal scrollbar arrows */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none; /* No background for the add-page and sub-page */\n"
"    border: none; /* Remove any border */\n"
"}")
        self.secondaryConsoleLog.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.consoleTab.addTab(self.secondaryTab, "")
        self.secondaryConsoleLog.raise_()
        self.clearSecondaryConsoleButton.raise_()
        self.saveSecondaryConsoleButton.raise_()
        self.tertiaryTab = QWidget()
        self.tertiaryTab.setObjectName(u"tertiaryTab")
        self.tertiaryConsoleLog = QTextBrowser(self.tertiaryTab)
        self.tertiaryConsoleLog.setObjectName(u"tertiaryConsoleLog")
        self.tertiaryConsoleLog.setGeometry(QRect(16, 15, 600, 924))
        self.tertiaryConsoleLog.setFont(font9)
        self.tertiaryConsoleLog.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tertiaryConsoleLog.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 1px; /* Smallest rounded corners for the border */\n"
"    background-color: #E6E2BE; /* Yellowish-beige background color */\n"
"    padding-top: 1px; /* Add padding to the top */\n"
"    padding-bottom: 1px; /* Add padding to the bottom */\n"
"    padding-right: 1px; /* Add padding to the right to move the scrollbar inward */\n"
"	color: black; /* Default black text colour */\n"
"}\n"
"\n"
"/* Vertical scroll bar */\n"
"QScrollBar:vertical {\n"
"    background: #E6E2BE; /* Background color of the scrollbar track */\n"
"    width: 10px; /* Width of the scrollbar */\n"
"    border-radius: 1px; /* Smallest rounded corners for the scrollbar track */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #FFA2A7; /* Background color of the handle */\n"
"    border: 1px solid black; /* Border color of the handle */\n"
"    border-radius: 4px; /* Smallest rounded corners for the handle */\n"
"    min-heigh"
                        "t: 20px; /* Minimum height of the handle */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #A6FFA7; /* Change background color to green when hovered */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #A6FFA7; /* Change background color to green when selected */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none; /* Match the background color of the QTextBrowser */\n"
"    height: 0px; /* Height set to 0 to hide the add-line and sub-line */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none; /* No background for the up-arrow and down-arrow */\n"
"    height: 0px; /* Height set to 0 to hide the up-arrow and down-arrow */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none; /* No background for the add-page and sub-page "
                        "*/\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"/* Horizontal scroll bar */\n"
"QScrollBar:horizontal {\n"
"    background: #E6E2BE; /* Background color of the scrollbar track */\n"
"    height: 10px; /* Height of the scrollbar */\n"
"    border-radius: 1px; /* Smallest rounded corners for the scrollbar track */\n"
"	padding-left: 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #FFA2A7; /* Background color of the handle */\n"
"    border: 1px solid black; /* Border color of the handle */\n"
"    border-radius: 4px; /* Smallest rounded corners for the handle */\n"
"    min-width: 20px; /* Minimum width of the handle */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #A6FFA7; /* Change background color to green when hovered */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: #A6FFA7; /* Change background color to green when selected */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"  "
                        "  background: none; /* Consistent background for hiding */\n"
"    width: 0px; /* Use width for horizontal scrollbar buttons */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none; /* No background for the arrows */\n"
"    width: 0px; /* Use width for horizontal scrollbar arrows */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none; /* No background for the add-page and sub-page */\n"
"    border: none; /* Remove any border */\n"
"}\n"
"\n"
"")
        self.tertiaryConsoleLog.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.clearTertiaryConsoleButton = QPushButton(self.tertiaryTab)
        self.clearTertiaryConsoleButton.setObjectName(u"clearTertiaryConsoleButton")
        self.clearTertiaryConsoleButton.setGeometry(QRect(540, 864, 51, 22))
        self.clearTertiaryConsoleButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.saveTertiaryConsoleButton = QPushButton(self.tertiaryTab)
        self.saveTertiaryConsoleButton.setObjectName(u"saveTertiaryConsoleButton")
        self.saveTertiaryConsoleButton.setGeometry(QRect(540, 894, 51, 22))
        self.saveTertiaryConsoleButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #F6F6F6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.consoleTab.addTab(self.tertiaryTab, "")
        self.sysFrame = QFrame(self.centralwidget)
        self.sysFrame.setObjectName(u"sysFrame")
        self.sysFrame.setGeometry(QRect(381, 848, 822, 149))
        self.sysFrame.setStyleSheet(u"QFrame#sysFrame{    \n"
"	border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"}")
        self.sysFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sysFrame.setFrameShadow(QFrame.Shadow.Raised)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.commsTab.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.consoleTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metrics", None))
        self.ADCIOPageButton.setText(QCoreApplication.translate("MainWindow", u"ADC/IO", None))
        self.testButton1.setText(QCoreApplication.translate("MainWindow", u"Test \n"
" Button 1", None))
        self.testButton3.setText(QCoreApplication.translate("MainWindow", u"Test \n"
" Button 3", None))
        self.testButton5.setText(QCoreApplication.translate("MainWindow", u"Test \n"
" Button 5", None))
        self.testButton4.setText(QCoreApplication.translate("MainWindow", u"Test \n"
" Button 4", None))
        self.testButton2.setText(QCoreApplication.translate("MainWindow", u"Test \n"
" Button 2", None))
        self.colourPalettePageButton.setText(QCoreApplication.translate("MainWindow", u"Colour\n"
"Palette", None))
        self.serialAutoButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.serialConnectButton.setText(QCoreApplication.translate("MainWindow", u"Select Manual", None))
        self.serialStatus.setText(QCoreApplication.translate("MainWindow", u"Not Connected", None))
        self.serialManualButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.serialTxBytes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.serialRxBytes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.serialTxLabel.setText(QCoreApplication.translate("MainWindow", u"Transmitted", None))
        self.serialRxLabel.setText(QCoreApplication.translate("MainWindow", u"Received", None))
        self.commsTab.setTabText(self.commsTab.indexOf(self.serialTab), QCoreApplication.translate("MainWindow", u"Serial", None))
        self.commsTab.setTabText(self.commsTab.indexOf(self.bluetoothTab), QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.commsTab.setTabText(self.commsTab.indexOf(self.WiFiTab), QCoreApplication.translate("MainWindow", u"WiFi", None))
        self.authenticateLineEdit.setText(QCoreApplication.translate("MainWindow", u"Not Required", None))
        self.heartbeatLED.setText(QCoreApplication.translate("MainWindow", u"Heartbeat", None))
        self.authenticateButton.setText(QCoreApplication.translate("MainWindow", u"Authenticate", None))
        self.ADCBox.setTitle(QCoreApplication.translate("MainWindow", u"ADC", None))
        ___qtablewidgetitem = self.adcTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ECU-ID", None));
        ___qtablewidgetitem1 = self.adcTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Channel", None));
        ___qtablewidgetitem2 = self.adcTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Scaled", None));
        ___qtablewidgetitem3 = self.adcTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Raw", None));
        ___qtablewidgetitem4 = self.adcTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Alter Raw", None));
        self.resetADCButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.alterADCButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.inputsBox.setTitle(QCoreApplication.translate("MainWindow", u"GPIO Inputs", None))
        ___qtablewidgetitem5 = self.inputsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ECU-ID", None));
        ___qtablewidgetitem6 = self.inputsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Input", None));
        ___qtablewidgetitem7 = self.inputsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem8 = self.inputsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        self.alterInputsButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.resetInputsButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.outputsBox.setTitle(QCoreApplication.translate("MainWindow", u"GPIO Outputs", None))
        ___qtablewidgetitem9 = self.outputsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"ECU-ID", None));
        ___qtablewidgetitem10 = self.outputsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Output", None));
        ___qtablewidgetitem11 = self.outputsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem12 = self.outputsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        self.resetOutputsButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.alterOutputsButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.colourPaletteLog.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.fgColourBox.setTitle(QCoreApplication.translate("MainWindow", u"Foreground", None))
        self.bgColourBox.setTitle(QCoreApplication.translate("MainWindow", u"Background", None))
        self.appendButton.setText(QCoreApplication.translate("MainWindow", u"Append", None))
        self.fgWhiteButton.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.fgBlackButton.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.fgResetButton.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.bgBlackButton.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.bgWhiteButton.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.bgResetButton.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1) Paste text into text box.\n"
"2) Select foreground and background colour using the sliders.\n"
"3) Append text to test log to see how it may look on the screen.", None))
        self.testBox.setTitle("")
        ___qtablewidgetitem13 = self.testTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem14 = self.testTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.bgDefButton.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.clearPaletteConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.clearPrimaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.savePrimaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.consoleTab.setTabText(self.consoleTab.indexOf(self.primaryTab), QCoreApplication.translate("MainWindow", u"ECU1", None))
        self.saveSecondaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.clearSecondaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.consoleTab.setTabText(self.consoleTab.indexOf(self.secondaryTab), QCoreApplication.translate("MainWindow", u"ECU2", None))
        self.clearTertiaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.saveTertiaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.consoleTab.setTabText(self.consoleTab.indexOf(self.tertiaryTab), QCoreApplication.translate("MainWindow", u"Debug", None))
    # retranslateUi

