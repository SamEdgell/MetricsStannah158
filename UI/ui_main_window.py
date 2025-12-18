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
    QFrame, QGroupBox, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QWidget)

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
        self.swivelPageButton = QPushButton(self.navigationFrame)
        self.swivelPageButton.setObjectName(u"swivelPageButton")
        self.swivelPageButton.setGeometry(QRect(268, 281, 68, 48))
        self.swivelPageButton.setFont(font1)
        self.swivelPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.configurationPageButton = QPushButton(self.navigationFrame)
        self.configurationPageButton.setObjectName(u"configurationPageButton")
        self.configurationPageButton.setGeometry(QRect(268, 117, 68, 48))
        self.configurationPageButton.setFont(font1)
        self.configurationPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.railMappingPageButton = QPushButton(self.navigationFrame)
        self.railMappingPageButton.setObjectName(u"railMappingPageButton")
        self.railMappingPageButton.setGeometry(QRect(185, 199, 68, 48))
        self.railMappingPageButton.setFont(font1)
        self.railMappingPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.metricsVersionText = QLineEdit(self.imageFrame)
        self.metricsVersionText.setObjectName(u"metricsVersionText")
        self.metricsVersionText.setGeometry(QRect(5, 61, 50, 22))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.metricsVersionText.setFont(font2)
        self.metricsVersionText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.metricsVersionText.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.metricsVersionText.setReadOnly(True)
        self.callFrame = QFrame(self.navigationFrame)
        self.callFrame.setObjectName(u"callFrame")
        self.callFrame.setGeometry(QRect(17, 489, 320, 286))
        self.callFrame.setStyleSheet(u"QFrame#callFrame{    \n"
"	border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"}")
        self.callFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.callFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.carriageLeftCallButton = QPushButton(self.callFrame)
        self.carriageLeftCallButton.setObjectName(u"carriageLeftCallButton")
        self.carriageLeftCallButton.setGeometry(QRect(17, 175, 54, 48))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(7)
        font3.setBold(False)
        self.carriageLeftCallButton.setFont(font3)
        self.carriageLeftCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #6DFFE9;\n"
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
        self.footrestUnfoldCallButton = QPushButton(self.callFrame)
        self.footrestUnfoldCallButton.setObjectName(u"footrestUnfoldCallButton")
        self.footrestUnfoldCallButton.setGeometry(QRect(75, 68, 54, 48))
        self.footrestUnfoldCallButton.setFont(font3)
        self.footrestUnfoldCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFB037;\n"
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
        self.swivelLeftCallButton = QPushButton(self.callFrame)
        self.swivelLeftCallButton.setObjectName(u"swivelLeftCallButton")
        self.swivelLeftCallButton.setGeometry(QRect(133, 68, 54, 48))
        self.swivelLeftCallButton.setFont(font3)
        self.swivelLeftCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFA4FF;\n"
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
        self.chairFoldCallButton = QPushButton(self.callFrame)
        self.chairFoldCallButton.setObjectName(u"chairFoldCallButton")
        self.chairFoldCallButton.setGeometry(QRect(74, 15, 54, 48))
        self.chairFoldCallButton.setFont(font3)
        self.chairFoldCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6FF68;\n"
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
        self.swivelRightCallButton = QPushButton(self.callFrame)
        self.swivelRightCallButton.setObjectName(u"swivelRightCallButton")
        self.swivelRightCallButton.setGeometry(QRect(249, 68, 54, 48))
        self.swivelRightCallButton.setFont(font3)
        self.swivelRightCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFA4FF;\n"
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
        self.chairPartFoldCallButton = QPushButton(self.callFrame)
        self.chairPartFoldCallButton.setObjectName(u"chairPartFoldCallButton")
        self.chairPartFoldCallButton.setGeometry(QRect(132, 15, 54, 48))
        self.chairPartFoldCallButton.setFont(font3)
        self.chairPartFoldCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6FF68;\n"
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
        self.footrestFoldCallButton = QPushButton(self.callFrame)
        self.footrestFoldCallButton.setObjectName(u"footrestFoldCallButton")
        self.footrestFoldCallButton.setGeometry(QRect(17, 68, 54, 48))
        self.footrestFoldCallButton.setFont(font3)
        self.footrestFoldCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFB037;\n"
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
        self.carriageRightCallButton = QPushButton(self.callFrame)
        self.carriageRightCallButton.setObjectName(u"carriageRightCallButton")
        self.carriageRightCallButton.setGeometry(QRect(75, 175, 54, 48))
        self.carriageRightCallButton.setFont(font3)
        self.carriageRightCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #6DFFE9;\n"
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
        self.swivelCentreCallButton = QPushButton(self.callFrame)
        self.swivelCentreCallButton.setObjectName(u"swivelCentreCallButton")
        self.swivelCentreCallButton.setGeometry(QRect(191, 68, 54, 48))
        self.swivelCentreCallButton.setFont(font3)
        self.swivelCentreCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFA4FF;\n"
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
        self.chairUnfoldCallButton = QPushButton(self.callFrame)
        self.chairUnfoldCallButton.setObjectName(u"chairUnfoldCallButton")
        self.chairUnfoldCallButton.setGeometry(QRect(190, 15, 54, 48))
        self.chairUnfoldCallButton.setFont(font3)
        self.chairUnfoldCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #F6FF68;\n"
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
        self.localLeftCallButton = QPushButton(self.callFrame)
        self.localLeftCallButton.setObjectName(u"localLeftCallButton")
        self.localLeftCallButton.setGeometry(QRect(17, 122, 54, 48))
        self.localLeftCallButton.setFont(font3)
        self.localLeftCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #35E0FF;\n"
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
        self.localRightCallButton = QPushButton(self.callFrame)
        self.localRightCallButton.setObjectName(u"localRightCallButton")
        self.localRightCallButton.setGeometry(QRect(75, 122, 54, 48))
        self.localRightCallButton.setFont(font3)
        self.localRightCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #35E0FF;\n"
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
        self.remoteUpCallButton = QPushButton(self.callFrame)
        self.remoteUpCallButton.setObjectName(u"remoteUpCallButton")
        self.remoteUpCallButton.setGeometry(QRect(191, 122, 54, 48))
        self.remoteUpCallButton.setFont(font3)
        self.remoteUpCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #35E0FF;\n"
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
        self.remoteDownCallButton = QPushButton(self.callFrame)
        self.remoteDownCallButton.setObjectName(u"remoteDownCallButton")
        self.remoteDownCallButton.setGeometry(QRect(249, 122, 54, 48))
        self.remoteDownCallButton.setFont(font3)
        self.remoteDownCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #35E0FF;\n"
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
        self.repeatCallButton = QPushButton(self.callFrame)
        self.repeatCallButton.setObjectName(u"repeatCallButton")
        self.repeatCallButton.setGeometry(QRect(17, 235, 286, 37))
        self.repeatCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #A6FFA7;\n"
"}")
        self.carriageDownCallButton = QPushButton(self.callFrame)
        self.carriageDownCallButton.setObjectName(u"carriageDownCallButton")
        self.carriageDownCallButton.setGeometry(QRect(249, 175, 54, 48))
        self.carriageDownCallButton.setFont(font3)
        self.carriageDownCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #6DFFE9;\n"
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
        self.carriageUpCallButton = QPushButton(self.callFrame)
        self.carriageUpCallButton.setObjectName(u"carriageUpCallButton")
        self.carriageUpCallButton.setGeometry(QRect(191, 175, 54, 48))
        self.carriageUpCallButton.setFont(font3)
        self.carriageUpCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #6DFFE9;\n"
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
        self.noCallButton = QPushButton(self.callFrame)
        self.noCallButton.setObjectName(u"noCallButton")
        self.noCallButton.setGeometry(QRect(133, 122, 54, 48))
        self.noCallButton.setFont(font3)
        self.noCallButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 10px;\n"
"    background-color: #FFA2A7;\n"
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
        self.testButton1 = QPushButton(self.navigationFrame)
        self.testButton1.setObjectName(u"testButton1")
        self.testButton1.setGeometry(QRect(34, 444, 54, 34))
        self.testButton1.setFont(font3)
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
        self.testButton3.setGeometry(QRect(150, 444, 54, 34))
        self.testButton3.setFont(font3)
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
        self.testButton5.setGeometry(QRect(266, 444, 54, 34))
        self.testButton5.setFont(font3)
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
        self.testButton4.setGeometry(QRect(208, 444, 54, 34))
        self.testButton4.setFont(font3)
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
        self.testButton2.setGeometry(QRect(92, 444, 54, 34))
        self.testButton2.setFont(font3)
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
        self.colourPalettePageButton.setGeometry(QRect(185, 117, 68, 48))
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
        self.chairFoldPageButton = QPushButton(self.navigationFrame)
        self.chairFoldPageButton.setObjectName(u"chairFoldPageButton")
        self.chairFoldPageButton.setGeometry(QRect(19, 281, 68, 48))
        self.chairFoldPageButton.setFont(font1)
        self.chairFoldPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.footrestPageButton = QPushButton(self.navigationFrame)
        self.footrestPageButton.setObjectName(u"footrestPageButton")
        self.footrestPageButton.setGeometry(QRect(102, 281, 68, 48))
        self.footrestPageButton.setFont(font1)
        self.footrestPageButton.setStyleSheet(u"QPushButton {\n"
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
        font4 = QFont()
        font4.setKerning(True)
        self.topLine_2.setFont(font4)
        self.topLine_2.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_2.setFrameShape(QFrame.Shape.HLine)
        self.topLine_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.mainDrivePageButton = QPushButton(self.navigationFrame)
        self.mainDrivePageButton.setObjectName(u"mainDrivePageButton")
        self.mainDrivePageButton.setGeometry(QRect(185, 281, 68, 48))
        self.mainDrivePageButton.setFont(font1)
        self.mainDrivePageButton.setStyleSheet(u"QPushButton {\n"
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
        self.topLine_5 = QFrame(self.navigationFrame)
        self.topLine_5.setObjectName(u"topLine_5")
        self.topLine_5.setGeometry(QRect(18, 263, 317, 2))
        self.topLine_5.setFont(font4)
        self.topLine_5.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_5.setFrameShape(QFrame.Shape.HLine)
        self.topLine_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.systemPageButton = QPushButton(self.navigationFrame)
        self.systemPageButton.setObjectName(u"systemPageButton")
        self.systemPageButton.setGeometry(QRect(268, 199, 68, 48))
        self.systemPageButton.setFont(font1)
        self.systemPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.keyWiringPageButton = QPushButton(self.navigationFrame)
        self.keyWiringPageButton.setObjectName(u"keyWiringPageButton")
        self.keyWiringPageButton.setGeometry(QRect(102, 199, 68, 48))
        self.keyWiringPageButton.setFont(font1)
        self.keyWiringPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.debuggingPageButton = QPushButton(self.navigationFrame)
        self.debuggingPageButton.setObjectName(u"debuggingPageButton")
        self.debuggingPageButton.setGeometry(QRect(19, 199, 68, 48))
        self.debuggingPageButton.setFont(font1)
        self.debuggingPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.topLine_21 = QFrame(self.navigationFrame)
        self.topLine_21.setObjectName(u"topLine_21")
        self.topLine_21.setGeometry(QRect(18, 345, 317, 2))
        self.topLine_21.setFont(font4)
        self.topLine_21.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_21.setFrameShape(QFrame.Shape.HLine)
        self.topLine_21.setFrameShadow(QFrame.Shadow.Sunken)
        self.callAndDemandPageButton = QPushButton(self.navigationFrame)
        self.callAndDemandPageButton.setObjectName(u"callAndDemandPageButton")
        self.callAndDemandPageButton.setGeometry(QRect(102, 117, 68, 48))
        self.callAndDemandPageButton.setFont(font1)
        self.callAndDemandPageButton.setStyleSheet(u"QPushButton {\n"
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
        self.enableDemoModeButton = QRadioButton(self.navigationFrame)
        self.enableDemoModeButton.setObjectName(u"enableDemoModeButton")
        self.enableDemoModeButton.setGeometry(QRect(200, 377, 139, 22))
        font5 = QFont()
        font5.setPointSize(9)
        self.enableDemoModeButton.setFont(font5)
        self.enableDemoModeButton.setStyleSheet(u"QRadioButton {\n"
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
        self.enableDemoModeButton.setChecked(False)
        self.enableDemoModeButton.setAutoExclusive(False)
        self.x06PageButton = QPushButton(self.navigationFrame)
        self.x06PageButton.setObjectName(u"x06PageButton")
        self.x06PageButton.setGeometry(QRect(19, 364, 68, 48))
        self.x06PageButton.setFont(font1)
        self.x06PageButton.setStyleSheet(u"QPushButton {\n"
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
        self.keyWiringPageButton.raise_()
        self.ADCIOPageButton.raise_()
        self.configurationPageButton.raise_()
        self.railMappingPageButton.raise_()
        self.imageFrame.raise_()
        self.callFrame.raise_()
        self.testButton1.raise_()
        self.testButton3.raise_()
        self.testButton5.raise_()
        self.testButton4.raise_()
        self.testButton2.raise_()
        self.colourPalettePageButton.raise_()
        self.chairFoldPageButton.raise_()
        self.footrestPageButton.raise_()
        self.topLine_2.raise_()
        self.mainDrivePageButton.raise_()
        self.topLine_5.raise_()
        self.systemPageButton.raise_()
        self.debuggingPageButton.raise_()
        self.topLine_21.raise_()
        self.swivelPageButton.raise_()
        self.callAndDemandPageButton.raise_()
        self.x06PageButton.raise_()
        self.enableDemoModeButton.raise_()
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
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.ADCBox.setFont(font6)
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
        font7 = QFont()
        font7.setPointSize(7)
        self.adcTable.setFont(font7)
        self.adcTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.adcTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.adcTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #A0BEF4;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
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
        self.inputsBox.setFont(font6)
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
        self.inputsTable.setFont(font7)
        self.inputsTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.inputsTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.inputsTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #A0BEF4;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
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
        self.outputsBox.setFont(font6)
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
        self.outputsTable.setFont(font7)
        self.outputsTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.outputsTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.outputsTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #A0BEF4;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
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
        self.callAndDemandPage = QWidget()
        self.callAndDemandPage.setObjectName(u"callAndDemandPage")
        self.callDetectionGroup = QGroupBox(self.callAndDemandPage)
        self.callDetectionGroup.setObjectName(u"callDetectionGroup")
        self.callDetectionGroup.setGeometry(QRect(110, 31, 278, 253))
        self.callDetectionGroup.setFont(font6)
        self.callDetectionGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.callDetectionTable = QTableWidget(self.callDetectionGroup)
        if (self.callDetectionTable.columnCount() < 2):
            self.callDetectionTable.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.callDetectionTable.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.callDetectionTable.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        self.callDetectionTable.setObjectName(u"callDetectionTable")
        self.callDetectionTable.setGeometry(QRect(18, 51, 241, 183))
        font8 = QFont()
        font8.setPointSize(8)
        self.callDetectionTable.setFont(font8)
        self.callDetectionTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.callDetectionTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.callDetectionTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.callDetectionTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.callDetectionTable.setAutoScroll(False)
        self.callDetectionTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.callDetectionTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.callDetectionTable.horizontalHeader().setVisible(False)
        self.callDetectionTable.horizontalHeader().setMinimumSectionSize(80)
        self.callDetectionTable.horizontalHeader().setDefaultSectionSize(120)
        self.callDetectionTable.horizontalHeader().setStretchLastSection(False)
        self.callDetectionTable.verticalHeader().setVisible(False)
        self.callDetectionTable.verticalHeader().setMinimumSectionSize(16)
        self.callDetectionTable.verticalHeader().setDefaultSectionSize(18)
        self.demandProcessorGroup = QGroupBox(self.callAndDemandPage)
        self.demandProcessorGroup.setObjectName(u"demandProcessorGroup")
        self.demandProcessorGroup.setGeometry(QRect(404, 31, 278, 253))
        self.demandProcessorGroup.setFont(font6)
        self.demandProcessorGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.demandProcessorTable = QTableWidget(self.demandProcessorGroup)
        if (self.demandProcessorTable.columnCount() < 2):
            self.demandProcessorTable.setColumnCount(2)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.demandProcessorTable.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.demandProcessorTable.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        self.demandProcessorTable.setObjectName(u"demandProcessorTable")
        self.demandProcessorTable.setGeometry(QRect(18, 51, 241, 183))
        self.demandProcessorTable.setFont(font8)
        self.demandProcessorTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.demandProcessorTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.demandProcessorTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.demandProcessorTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.demandProcessorTable.setAutoScroll(False)
        self.demandProcessorTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.demandProcessorTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.demandProcessorTable.horizontalHeader().setVisible(False)
        self.demandProcessorTable.horizontalHeader().setMinimumSectionSize(80)
        self.demandProcessorTable.horizontalHeader().setDefaultSectionSize(120)
        self.demandProcessorTable.horizontalHeader().setStretchLastSection(False)
        self.demandProcessorTable.verticalHeader().setVisible(False)
        self.demandProcessorTable.verticalHeader().setMinimumSectionSize(16)
        self.demandProcessorTable.verticalHeader().setDefaultSectionSize(18)
        self.stackedWidget.addWidget(self.callAndDemandPage)
        self.colourPalettePage = QWidget()
        self.colourPalettePage.setObjectName(u"colourPalettePage")
        self.testColourLog = QTextEdit(self.colourPalettePage)
        self.testColourLog.setObjectName(u"testColourLog")
        self.testColourLog.setGeometry(QRect(17, 15, 784, 299))
        font9 = QFont()
        font9.setFamilies([u"Consolas"])
        font9.setPointSize(8)
        self.testColourLog.setFont(font9)
        self.testColourLog.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.testColourLog.setStyleSheet(u"QTextEdit {\n"
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
        self.testColourLog.setReadOnly(True)
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
"    background: #2CEB6C; /* You can keep the handle visible */\n"
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
        self.appendButton.setFont(font3)
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
        self.testBox.setFont(font6)
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
        __qtablewidgetitem17 = QTableWidgetItem()
        self.testTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.testTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        self.testTable.setObjectName(u"testTable")
        self.testTable.setGeometry(QRect(17, 50, 123, 53))
        self.testTable.setFont(font8)
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
        self.stackedWidget.addWidget(self.colourPalettePage)
        self.configurationPage = QWidget()
        self.configurationPage.setObjectName(u"configurationPage")
        self.configBox = QGroupBox(self.configurationPage)
        self.configBox.setObjectName(u"configBox")
        self.configBox.setGeometry(QRect(54, 20, 518, 661))
        self.configBox.setFont(font6)
        self.configBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.configTable = QTableWidget(self.configBox)
        if (self.configTable.columnCount() < 4):
            self.configTable.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.configTable.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.configTable.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.configTable.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.configTable.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.configTable.setObjectName(u"configTable")
        self.configTable.setGeometry(QRect(17, 50, 483, 550))
        self.configTable.setFont(font7)
        self.configTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.configTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.configTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.configTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.configTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.configTable.setAutoScroll(False)
        self.configTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.configTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.configTable.horizontalHeader().setMinimumSectionSize(40)
        self.configTable.horizontalHeader().setDefaultSectionSize(120)
        self.configTable.horizontalHeader().setStretchLastSection(False)
        self.configTable.verticalHeader().setVisible(False)
        self.configTable.verticalHeader().setMinimumSectionSize(14)
        self.configTable.verticalHeader().setDefaultSectionSize(14)
        self.loadConfigButton = QPushButton(self.configBox)
        self.loadConfigButton.setObjectName(u"loadConfigButton")
        self.loadConfigButton.setGeometry(QRect(174, 620, 51, 22))
        self.loadConfigButton.setStyleSheet(u"QPushButton {\n"
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
        self.alterConfigButton = QPushButton(self.configBox)
        self.alterConfigButton.setObjectName(u"alterConfigButton")
        self.alterConfigButton.setGeometry(QRect(294, 620, 51, 22))
        self.alterConfigButton.setStyleSheet(u"QPushButton {\n"
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
        self.restoreConfigButton = QPushButton(self.configBox)
        self.restoreConfigButton.setObjectName(u"restoreConfigButton")
        self.restoreConfigButton.setGeometry(QRect(17, 15, 51, 22))
        self.restoreConfigButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #000000;\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: #000000;\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.resetConfigButton = QPushButton(self.configBox)
        self.resetConfigButton.setObjectName(u"resetConfigButton")
        self.resetConfigButton.setGeometry(QRect(234, 620, 51, 22))
        self.resetConfigButton.setStyleSheet(u"QPushButton {\n"
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
        self.confirmRestoreButton = QRadioButton(self.configBox)
        self.confirmRestoreButton.setObjectName(u"confirmRestoreButton")
        self.confirmRestoreButton.setGeometry(QRect(80, 15, 68, 22))
        self.confirmRestoreButton.setFont(font5)
        self.confirmRestoreButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.confirmRestoreButton.setChecked(False)
        self.saveConfigButton = QPushButton(self.configBox)
        self.saveConfigButton.setObjectName(u"saveConfigButton")
        self.saveConfigButton.setGeometry(QRect(449, 15, 51, 22))
        self.saveConfigButton.setStyleSheet(u"QPushButton {\n"
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
        self.injectConfigButton = QPushButton(self.configBox)
        self.injectConfigButton.setObjectName(u"injectConfigButton")
        self.injectConfigButton.setGeometry(QRect(390, 15, 51, 22))
        self.injectConfigButton.setStyleSheet(u"QPushButton {\n"
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
        self.sdCardBox = QGroupBox(self.configurationPage)
        self.sdCardBox.setObjectName(u"sdCardBox")
        self.sdCardBox.setGeometry(QRect(589, 20, 180, 119))
        self.sdCardBox.setFont(font6)
        self.sdCardBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.eraseSDCardButton = QPushButton(self.sdCardBox)
        self.eraseSDCardButton.setObjectName(u"eraseSDCardButton")
        self.eraseSDCardButton.setGeometry(QRect(26, 50, 51, 22))
        self.eraseSDCardButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #000000;\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: #000000;\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.sdCardTextEdit = QLineEdit(self.sdCardBox)
        self.sdCardTextEdit.setObjectName(u"sdCardTextEdit")
        self.sdCardTextEdit.setGeometry(QRect(12, 85, 156, 22))
        self.sdCardTextEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.sdCardTextEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sdCardTextEdit.setReadOnly(True)
        self.confirmEraseButton = QRadioButton(self.sdCardBox)
        self.confirmEraseButton.setObjectName(u"confirmEraseButton")
        self.confirmEraseButton.setGeometry(QRect(86, 50, 68, 22))
        self.confirmEraseButton.setFont(font5)
        self.confirmEraseButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.confirmEraseButton.setChecked(False)
        self.stackedWidget.addWidget(self.configurationPage)
        self.debuggingPage = QWidget()
        self.debuggingPage.setObjectName(u"debuggingPage")
        self.debugGroup1 = QGroupBox(self.debuggingPage)
        self.debugGroup1.setObjectName(u"debugGroup1")
        self.debugGroup1.setGeometry(QRect(120, 16, 278, 253))
        self.debugGroup1.setFont(font6)
        self.debugGroup1.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.debugTable1 = QTableWidget(self.debugGroup1)
        if (self.debugTable1.columnCount() < 2):
            self.debugTable1.setColumnCount(2)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.debugTable1.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.debugTable1.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        self.debugTable1.setObjectName(u"debugTable1")
        self.debugTable1.setGeometry(QRect(18, 51, 241, 183))
        self.debugTable1.setFont(font8)
        self.debugTable1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.debugTable1.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.debugTable1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable1.setAutoScroll(False)
        self.debugTable1.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debugTable1.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.debugTable1.horizontalHeader().setVisible(False)
        self.debugTable1.horizontalHeader().setMinimumSectionSize(80)
        self.debugTable1.horizontalHeader().setDefaultSectionSize(120)
        self.debugTable1.horizontalHeader().setStretchLastSection(False)
        self.debugTable1.verticalHeader().setVisible(False)
        self.debugTable1.verticalHeader().setMinimumSectionSize(16)
        self.debugTable1.verticalHeader().setDefaultSectionSize(18)
        self.debugGroup2 = QGroupBox(self.debuggingPage)
        self.debugGroup2.setObjectName(u"debugGroup2")
        self.debugGroup2.setGeometry(QRect(412, 16, 278, 253))
        self.debugGroup2.setFont(font6)
        self.debugGroup2.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.debugTable2 = QTableWidget(self.debugGroup2)
        if (self.debugTable2.columnCount() < 2):
            self.debugTable2.setColumnCount(2)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.debugTable2.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.debugTable2.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        self.debugTable2.setObjectName(u"debugTable2")
        self.debugTable2.setGeometry(QRect(18, 51, 241, 183))
        self.debugTable2.setFont(font8)
        self.debugTable2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.debugTable2.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.debugTable2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable2.setAutoScroll(False)
        self.debugTable2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debugTable2.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.debugTable2.horizontalHeader().setVisible(False)
        self.debugTable2.horizontalHeader().setMinimumSectionSize(80)
        self.debugTable2.horizontalHeader().setDefaultSectionSize(120)
        self.debugTable2.horizontalHeader().setStretchLastSection(False)
        self.debugTable2.verticalHeader().setVisible(False)
        self.debugTable2.verticalHeader().setMinimumSectionSize(16)
        self.debugTable2.verticalHeader().setDefaultSectionSize(18)
        self.debugGroup3 = QGroupBox(self.debuggingPage)
        self.debugGroup3.setObjectName(u"debugGroup3")
        self.debugGroup3.setGeometry(QRect(120, 283, 278, 253))
        self.debugGroup3.setFont(font6)
        self.debugGroup3.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.debugTable3 = QTableWidget(self.debugGroup3)
        if (self.debugTable3.columnCount() < 2):
            self.debugTable3.setColumnCount(2)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.debugTable3.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.debugTable3.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        self.debugTable3.setObjectName(u"debugTable3")
        self.debugTable3.setGeometry(QRect(18, 51, 241, 183))
        self.debugTable3.setFont(font8)
        self.debugTable3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.debugTable3.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.debugTable3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable3.setAutoScroll(False)
        self.debugTable3.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debugTable3.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.debugTable3.horizontalHeader().setVisible(False)
        self.debugTable3.horizontalHeader().setMinimumSectionSize(80)
        self.debugTable3.horizontalHeader().setDefaultSectionSize(120)
        self.debugTable3.horizontalHeader().setStretchLastSection(False)
        self.debugTable3.verticalHeader().setVisible(False)
        self.debugTable3.verticalHeader().setMinimumSectionSize(16)
        self.debugTable3.verticalHeader().setDefaultSectionSize(18)
        self.debugGroup4 = QGroupBox(self.debuggingPage)
        self.debugGroup4.setObjectName(u"debugGroup4")
        self.debugGroup4.setGeometry(QRect(412, 283, 278, 253))
        self.debugGroup4.setFont(font6)
        self.debugGroup4.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.debugTable4 = QTableWidget(self.debugGroup4)
        if (self.debugTable4.columnCount() < 2):
            self.debugTable4.setColumnCount(2)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.debugTable4.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.debugTable4.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        self.debugTable4.setObjectName(u"debugTable4")
        self.debugTable4.setGeometry(QRect(18, 51, 241, 183))
        self.debugTable4.setFont(font8)
        self.debugTable4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.debugTable4.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.debugTable4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable4.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable4.setAutoScroll(False)
        self.debugTable4.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debugTable4.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.debugTable4.horizontalHeader().setVisible(False)
        self.debugTable4.horizontalHeader().setMinimumSectionSize(80)
        self.debugTable4.horizontalHeader().setDefaultSectionSize(120)
        self.debugTable4.horizontalHeader().setStretchLastSection(False)
        self.debugTable4.verticalHeader().setVisible(False)
        self.debugTable4.verticalHeader().setMinimumSectionSize(16)
        self.debugTable4.verticalHeader().setDefaultSectionSize(18)
        self.debugGroup6 = QGroupBox(self.debuggingPage)
        self.debugGroup6.setObjectName(u"debugGroup6")
        self.debugGroup6.setGeometry(QRect(412, 550, 278, 253))
        self.debugGroup6.setFont(font6)
        self.debugGroup6.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.debugTable6 = QTableWidget(self.debugGroup6)
        if (self.debugTable6.columnCount() < 2):
            self.debugTable6.setColumnCount(2)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.debugTable6.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.debugTable6.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        self.debugTable6.setObjectName(u"debugTable6")
        self.debugTable6.setGeometry(QRect(18, 51, 241, 183))
        self.debugTable6.setFont(font8)
        self.debugTable6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.debugTable6.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.debugTable6.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable6.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable6.setAutoScroll(False)
        self.debugTable6.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debugTable6.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.debugTable6.horizontalHeader().setVisible(False)
        self.debugTable6.horizontalHeader().setMinimumSectionSize(80)
        self.debugTable6.horizontalHeader().setDefaultSectionSize(120)
        self.debugTable6.horizontalHeader().setStretchLastSection(False)
        self.debugTable6.verticalHeader().setVisible(False)
        self.debugTable6.verticalHeader().setMinimumSectionSize(16)
        self.debugTable6.verticalHeader().setDefaultSectionSize(18)
        self.debugGroup5 = QGroupBox(self.debuggingPage)
        self.debugGroup5.setObjectName(u"debugGroup5")
        self.debugGroup5.setGeometry(QRect(120, 550, 278, 253))
        self.debugGroup5.setFont(font6)
        self.debugGroup5.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.debugTable5 = QTableWidget(self.debugGroup5)
        if (self.debugTable5.columnCount() < 2):
            self.debugTable5.setColumnCount(2)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.debugTable5.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.debugTable5.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        self.debugTable5.setObjectName(u"debugTable5")
        self.debugTable5.setGeometry(QRect(18, 51, 241, 183))
        self.debugTable5.setFont(font8)
        self.debugTable5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.debugTable5.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.debugTable5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable5.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.debugTable5.setAutoScroll(False)
        self.debugTable5.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.debugTable5.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.debugTable5.horizontalHeader().setVisible(False)
        self.debugTable5.horizontalHeader().setMinimumSectionSize(80)
        self.debugTable5.horizontalHeader().setDefaultSectionSize(120)
        self.debugTable5.horizontalHeader().setStretchLastSection(False)
        self.debugTable5.verticalHeader().setVisible(False)
        self.debugTable5.verticalHeader().setMinimumSectionSize(16)
        self.debugTable5.verticalHeader().setDefaultSectionSize(18)
        self.stackedWidget.addWidget(self.debuggingPage)
        self.keyWiringPage = QWidget()
        self.keyWiringPage.setObjectName(u"keyWiringPage")
        self.rightStopLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup = QButtonGroup(MainWindow)
        self.keyWiringButtonGroup.setObjectName(u"keyWiringButtonGroup")
        self.keyWiringButtonGroup.setExclusive(False)
        self.keyWiringButtonGroup.addButton(self.rightStopLED)
        self.rightStopLED.setObjectName(u"rightStopLED")
        self.rightStopLED.setEnabled(False)
        self.rightStopLED.setGeometry(QRect(562, 385, 25, 30))
        self.rightStopLED.setFont(font5)
        self.rightStopLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.rightStopLED.setChecked(False)
        self.rightStopLED.setAutoExclusive(True)
        self.rightSafetyLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.rightSafetyLED)
        self.rightSafetyLED.setObjectName(u"rightSafetyLED")
        self.rightSafetyLED.setEnabled(False)
        self.rightSafetyLED.setGeometry(QRect(562, 505, 25, 30))
        self.rightSafetyLED.setFont(font5)
        self.rightSafetyLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.rightSafetyLED.setChecked(False)
        self.rightSafetyLED.setAutoExclusive(False)
        self.callDownLabel = QLabel(self.keyWiringPage)
        self.callDownLabel.setObjectName(u"callDownLabel")
        self.callDownLabel.setGeometry(QRect(172, 275, 82, 35))
        self.callDownLabel.setFont(font6)
        self.callDownLabel.setStyleSheet(u"color: black;")
        self.callDownLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leftFootrestLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.leftFootrestLED)
        self.leftFootrestLED.setObjectName(u"leftFootrestLED")
        self.leftFootrestLED.setEnabled(False)
        self.leftFootrestLED.setGeometry(QRect(239, 565, 25, 30))
        self.leftFootrestLED.setFont(font5)
        self.leftFootrestLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.leftFootrestLED.setChecked(False)
        self.leftFootrestLED.setAutoExclusive(False)
        self.leftSkateLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.leftSkateLED)
        self.leftSkateLED.setObjectName(u"leftSkateLED")
        self.leftSkateLED.setEnabled(False)
        self.leftSkateLED.setGeometry(QRect(239, 445, 25, 30))
        self.leftSkateLED.setFont(font5)
        self.leftSkateLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.leftSkateLED.setChecked(False)
        self.leftSkateLED.setAutoExclusive(False)
        self.leftSafetyLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.leftSafetyLED)
        self.leftSafetyLED.setObjectName(u"leftSafetyLED")
        self.leftSafetyLED.setEnabled(False)
        self.leftSafetyLED.setGeometry(QRect(239, 505, 25, 30))
        self.leftSafetyLED.setFont(font5)
        self.leftSafetyLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.leftSafetyLED.setChecked(False)
        self.leftSafetyLED.setAutoExclusive(False)
        self.handing4Label = QLabel(self.keyWiringPage)
        self.handing4Label.setObjectName(u"handing4Label")
        self.handing4Label.setGeometry(QRect(462, 211, 83, 35))
        self.handing4Label.setFont(font6)
        self.handing4Label.setStyleSheet(u"color: black;\n"
"background: transparent;")
        self.handing4Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leftSkateLabel = QLabel(self.keyWiringPage)
        self.leftSkateLabel.setObjectName(u"leftSkateLabel")
        self.leftSkateLabel.setGeometry(QRect(137, 443, 82, 35))
        self.leftSkateLabel.setFont(font6)
        self.leftSkateLabel.setStyleSheet(u"color: black;")
        self.leftSkateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.osgReturnLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.osgReturnLED)
        self.osgReturnLED.setObjectName(u"osgReturnLED")
        self.osgReturnLED.setEnabled(False)
        self.osgReturnLED.setGeometry(QRect(82, 96, 25, 30))
        self.osgReturnLED.setFont(font5)
        self.osgReturnLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.osgReturnLED.setChecked(False)
        self.osgReturnLED.setAutoExclusive(False)
        self.osgReturnLabel = QLabel(self.keyWiringPage)
        self.osgReturnLabel.setObjectName(u"osgReturnLabel")
        self.osgReturnLabel.setGeometry(QRect(53, 59, 82, 35))
        self.osgReturnLabel.setFont(font6)
        self.osgReturnLabel.setStyleSheet(u"color: black;")
        self.osgReturnLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.callUpLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.callUpLED)
        self.callUpLED.setObjectName(u"callUpLED")
        self.callUpLED.setEnabled(False)
        self.callUpLED.setGeometry(QRect(201, 181, 25, 30))
        self.callUpLED.setFont(font5)
        self.callUpLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.callUpLED.setChecked(False)
        self.callUpLED.setAutoExclusive(False)
        self.handing2LED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.handing2LED)
        self.handing2LED.setObjectName(u"handing2LED")
        self.handing2LED.setEnabled(False)
        self.handing2LED.setGeometry(QRect(562, 182, 25, 30))
        self.handing2LED.setFont(font5)
        self.handing2LED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.handing2LED.setChecked(False)
        self.handing2LED.setAutoExclusive(False)
        self.bistableReturnLabel = QLabel(self.keyWiringPage)
        self.bistableReturnLabel.setObjectName(u"bistableReturnLabel")
        self.bistableReturnLabel.setGeometry(QRect(371, 56, 82, 35))
        self.bistableReturnLabel.setFont(font6)
        self.bistableReturnLabel.setStyleSheet(u"color: black;")
        self.bistableReturnLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ultimateLabel = QLabel(self.keyWiringPage)
        self.ultimateLabel.setObjectName(u"ultimateLabel")
        self.ultimateLabel.setGeometry(QRect(691, 75, 71, 16))
        self.ultimateLabel.setFont(font6)
        self.ultimateLabel.setStyleSheet(u"color: black;")
        self.ultimateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bottomFootrestLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.bottomFootrestLED)
        self.bottomFootrestLED.setObjectName(u"bottomFootrestLED")
        self.bottomFootrestLED.setEnabled(False)
        self.bottomFootrestLED.setGeometry(QRect(297, 240, 25, 30))
        self.bottomFootrestLED.setFont(font5)
        self.bottomFootrestLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.bottomFootrestLED.setChecked(False)
        self.bottomFootrestLED.setAutoExclusive(False)
        self.rightFootrestLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.rightFootrestLED)
        self.rightFootrestLED.setObjectName(u"rightFootrestLED")
        self.rightFootrestLED.setEnabled(False)
        self.rightFootrestLED.setGeometry(QRect(562, 565, 25, 30))
        self.rightFootrestLED.setFont(font5)
        self.rightFootrestLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.rightFootrestLED.setChecked(False)
        self.rightFootrestLED.setAutoExclusive(False)
        self.ultimateLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.ultimateLED)
        self.ultimateLED.setObjectName(u"ultimateLED")
        self.ultimateLED.setEnabled(False)
        self.ultimateLED.setGeometry(QRect(712, 96, 25, 30))
        self.ultimateLED.setFont(font5)
        self.ultimateLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.ultimateLED.setCheckable(True)
        self.ultimateLED.setChecked(False)
        self.ultimateLED.setAutoExclusive(False)
        self.relayCoilMonitorLabel = QLabel(self.keyWiringPage)
        self.relayCoilMonitorLabel.setObjectName(u"relayCoilMonitorLabel")
        self.relayCoilMonitorLabel.setGeometry(QRect(337, 585, 155, 35))
        self.relayCoilMonitorLabel.setFont(font6)
        self.relayCoilMonitorLabel.setStyleSheet(u"color: black;")
        self.relayCoilMonitorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leftSafetyLabel = QLabel(self.keyWiringPage)
        self.leftSafetyLabel.setObjectName(u"leftSafetyLabel")
        self.leftSafetyLabel.setGeometry(QRect(134, 502, 87, 35))
        self.leftSafetyLabel.setFont(font6)
        self.leftSafetyLabel.setStyleSheet(u"color: black;")
        self.leftSafetyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.callUpLabel = QLabel(self.keyWiringPage)
        self.callUpLabel.setObjectName(u"callUpLabel")
        self.callUpLabel.setGeometry(QRect(172, 145, 82, 35))
        self.callUpLabel.setFont(font6)
        self.callUpLabel.setStyleSheet(u"color: black;")
        self.callUpLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rightSafetyLabel = QLabel(self.keyWiringPage)
        self.rightSafetyLabel.setObjectName(u"rightSafetyLabel")
        self.rightSafetyLabel.setGeometry(QRect(597, 502, 99, 35))
        self.rightSafetyLabel.setFont(font6)
        self.rightSafetyLabel.setStyleSheet(u"color: black;")
        self.rightSafetyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.swivelOverrideLabel = QLabel(self.keyWiringPage)
        self.swivelOverrideLabel.setObjectName(u"swivelOverrideLabel")
        self.swivelOverrideLabel.setGeometry(QRect(211, 56, 82, 35))
        self.swivelOverrideLabel.setFont(font6)
        self.swivelOverrideLabel.setStyleSheet(u"color: black;")
        self.swivelOverrideLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leftFootrestLabel = QLabel(self.keyWiringPage)
        self.leftFootrestLabel.setObjectName(u"leftFootrestLabel")
        self.leftFootrestLabel.setGeometry(QRect(122, 562, 103, 35))
        self.leftFootrestLabel.setFont(font6)
        self.leftFootrestLabel.setStyleSheet(u"color: black;")
        self.leftFootrestLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bistableReturnLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.bistableReturnLED)
        self.bistableReturnLED.setObjectName(u"bistableReturnLED")
        self.bistableReturnLED.setEnabled(False)
        self.bistableReturnLED.setGeometry(QRect(399, 96, 25, 30))
        self.bistableReturnLED.setFont(font5)
        self.bistableReturnLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.bistableReturnLED.setCheckable(True)
        self.bistableReturnLED.setChecked(False)
        self.bistableReturnLED.setAutoExclusive(False)
        self.handing4LED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.handing4LED)
        self.handing4LED.setObjectName(u"handing4LED")
        self.handing4LED.setEnabled(False)
        self.handing4LED.setGeometry(QRect(492, 239, 25, 30))
        self.handing4LED.setFont(font5)
        self.handing4LED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.handing4LED.setChecked(False)
        self.handing4LED.setAutoExclusive(False)
        self.bistableFeedLabel = QLabel(self.keyWiringPage)
        self.bistableFeedLabel.setObjectName(u"bistableFeedLabel")
        self.bistableFeedLabel.setGeometry(QRect(530, 56, 82, 35))
        self.bistableFeedLabel.setFont(font6)
        self.bistableFeedLabel.setStyleSheet(u"color: black;")
        self.bistableFeedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rightSkateLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.rightSkateLED)
        self.rightSkateLED.setObjectName(u"rightSkateLED")
        self.rightSkateLED.setEnabled(False)
        self.rightSkateLED.setGeometry(QRect(562, 445, 25, 30))
        self.rightSkateLED.setFont(font5)
        self.rightSkateLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.rightSkateLED.setChecked(False)
        self.rightSkateLED.setAutoExclusive(False)
        self.rightStopLabel = QLabel(self.keyWiringPage)
        self.rightStopLabel.setObjectName(u"rightStopLabel")
        self.rightStopLabel.setGeometry(QRect(594, 383, 90, 35))
        self.rightStopLabel.setFont(font6)
        self.rightStopLabel.setStyleSheet(u"color: black;")
        self.rightStopLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bistableFeedLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.bistableFeedLED)
        self.bistableFeedLED.setObjectName(u"bistableFeedLED")
        self.bistableFeedLED.setEnabled(False)
        self.bistableFeedLED.setGeometry(QRect(558, 96, 25, 30))
        self.bistableFeedLED.setFont(font5)
        self.bistableFeedLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.bistableFeedLED.setCheckable(True)
        self.bistableFeedLED.setChecked(False)
        self.bistableFeedLED.setAutoExclusive(False)
        self.handing2Label = QLabel(self.keyWiringPage)
        self.handing2Label.setObjectName(u"handing2Label")
        self.handing2Label.setGeometry(QRect(462, 155, 87, 35))
        self.handing2Label.setFont(font6)
        self.handing2Label.setStyleSheet(u"color: black;\n"
"background: transparent;")
        self.handing2Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.callDownLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.callDownLED)
        self.callDownLED.setObjectName(u"callDownLED")
        self.callDownLED.setEnabled(False)
        self.callDownLED.setGeometry(QRect(201, 240, 25, 30))
        self.callDownLED.setFont(font5)
        self.callDownLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.callDownLED.setChecked(False)
        self.callDownLED.setAutoExclusive(False)
        self.leftStopLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.leftStopLED)
        self.leftStopLED.setObjectName(u"leftStopLED")
        self.leftStopLED.setEnabled(False)
        self.leftStopLED.setGeometry(QRect(239, 385, 25, 30))
        self.leftStopLED.setFont(font5)
        self.leftStopLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.leftStopLED.setChecked(False)
        self.leftStopLED.setAutoExclusive(False)
        self.leftStopLabel = QLabel(self.keyWiringPage)
        self.leftStopLabel.setObjectName(u"leftStopLabel")
        self.leftStopLabel.setGeometry(QRect(138, 383, 82, 35))
        self.leftStopLabel.setFont(font6)
        self.leftStopLabel.setStyleSheet(u"color: black;")
        self.leftStopLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bottomFootrestLabel = QLabel(self.keyWiringPage)
        self.bottomFootrestLabel.setObjectName(u"bottomFootrestLabel")
        self.bottomFootrestLabel.setGeometry(QRect(268, 276, 82, 35))
        self.bottomFootrestLabel.setFont(font6)
        self.bottomFootrestLabel.setStyleSheet(u"color: black;")
        self.bottomFootrestLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rightSkateLabel = QLabel(self.keyWiringPage)
        self.rightSkateLabel.setObjectName(u"rightSkateLabel")
        self.rightSkateLabel.setGeometry(QRect(598, 443, 91, 35))
        self.rightSkateLabel.setFont(font6)
        self.rightSkateLabel.setStyleSheet(u"color: black;")
        self.rightSkateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rightFootrestLabel = QLabel(self.keyWiringPage)
        self.rightFootrestLabel.setObjectName(u"rightFootrestLabel")
        self.rightFootrestLabel.setGeometry(QRect(595, 562, 115, 35))
        self.rightFootrestLabel.setFont(font6)
        self.rightFootrestLabel.setStyleSheet(u"color: black;")
        self.rightFootrestLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.relayCoilMonitorLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.relayCoilMonitorLED)
        self.relayCoilMonitorLED.setObjectName(u"relayCoilMonitorLED")
        self.relayCoilMonitorLED.setEnabled(False)
        self.relayCoilMonitorLED.setGeometry(QRect(402, 623, 25, 30))
        self.relayCoilMonitorLED.setFont(font5)
        self.relayCoilMonitorLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.relayCoilMonitorLED.setChecked(False)
        self.relayCoilMonitorLED.setAutoExclusive(False)
        self.swivelOverrideLED = QRadioButton(self.keyWiringPage)
        self.keyWiringButtonGroup.addButton(self.swivelOverrideLED)
        self.swivelOverrideLED.setObjectName(u"swivelOverrideLED")
        self.swivelOverrideLED.setEnabled(False)
        self.swivelOverrideLED.setGeometry(QRect(239, 96, 25, 30))
        self.swivelOverrideLED.setFont(font5)
        self.swivelOverrideLED.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px; /* Size of the circle */\n"
"    height: 20px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 10px; /* Makes the circle rounded */\n"
"    background-color: #FF0000; /* Background of the circle */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00FF00; /* Set background color to green when checked */\n"
"}")
        self.swivelOverrideLED.setCheckable(True)
        self.swivelOverrideLED.setChecked(False)
        self.swivelOverrideLED.setAutoExclusive(False)
        self.handingLink4 = QRadioButton(self.keyWiringPage)
        self.handingLink4.setObjectName(u"handingLink4")
        self.handingLink4.setGeometry(QRect(417, 244, 16, 22))
        self.handingLink4.setFont(font5)
        self.handingLink4.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink4.setCheckable(False)
        self.handingLink4.setChecked(False)
        self.handingLink4.setAutoExclusive(False)
        self.line_8 = QFrame(self.keyWiringPage)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(503, 255, 2, 96))
        self.line_8.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(self.keyWiringPage)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(142, 194, 2, 61))
        self.line_4.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_9 = QFrame(self.keyWiringPage)
        self.topLine_9.setObjectName(u"topLine_9")
        self.topLine_9.setGeometry(QRect(143, 194, 237, 2))
        self.topLine_9.setFont(font4)
        self.topLine_9.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_9.setFrameShape(QFrame.Shape.HLine)
        self.topLine_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_15 = QFrame(self.keyWiringPage)
        self.topLine_15.setObjectName(u"topLine_15")
        self.topLine_15.setGeometry(QRect(251, 636, 323, 2))
        self.topLine_15.setFont(font4)
        self.topLine_15.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_15.setFrameShape(QFrame.Shape.HLine)
        self.topLine_15.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_12 = QFrame(self.keyWiringPage)
        self.topLine_12.setObjectName(u"topLine_12")
        self.topLine_12.setGeometry(QRect(380, 284, 44, 2))
        self.topLine_12.setFont(font4)
        self.topLine_12.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_12.setFrameShape(QFrame.Shape.HLine)
        self.topLine_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.keyWiringPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(93, 109, 2, 116))
        self.line_2.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_8 = QFrame(self.keyWiringPage)
        self.topLine_8.setObjectName(u"topLine_8")
        self.topLine_8.setGeometry(QRect(94, 223, 49, 2))
        self.topLine_8.setFont(font4)
        self.topLine_8.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_8.setFrameShape(QFrame.Shape.HLine)
        self.topLine_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5 = QFrame(self.keyWiringPage)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(423, 165, 2, 27))
        self.line_5.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.handingLinkLabel3 = QLabel(self.keyWiringPage)
        self.handingLinkLabel3.setObjectName(u"handingLinkLabel3")
        self.handingLinkLabel3.setGeometry(QRect(434, 217, 16, 16))
        self.handingLinkLabel3.setFont(font6)
        self.handingLinkLabel3.setStyleSheet(u"color: black;")
        self.handingLinkLabel3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_9 = QFrame(self.keyWiringPage)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(250, 351, 2, 287))
        self.line_9.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.handingLinkLabel2 = QLabel(self.keyWiringPage)
        self.handingLinkLabel2.setObjectName(u"handingLinkLabel2")
        self.handingLinkLabel2.setGeometry(QRect(435, 186, 16, 16))
        self.handingLinkLabel2.setFont(font6)
        self.handingLinkLabel2.setStyleSheet(u"color: black;")
        self.handingLinkLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.handingLink3 = QRadioButton(self.keyWiringPage)
        self.handingLink3.setObjectName(u"handingLink3")
        self.handingLink3.setGeometry(QRect(417, 214, 16, 22))
        self.handingLink3.setFont(font5)
        self.handingLink3.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink3.setCheckable(False)
        self.handingLink3.setChecked(False)
        self.handingLink3.setAutoExclusive(False)
        self.line_10 = QFrame(self.keyWiringPage)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(413, 637, 2, 104))
        self.line_10.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.handingLinkLabel5 = QLabel(self.keyWiringPage)
        self.handingLinkLabel5.setObjectName(u"handingLinkLabel5")
        self.handingLinkLabel5.setGeometry(QRect(435, 277, 16, 16))
        self.handingLinkLabel5.setFont(font6)
        self.handingLinkLabel5.setStyleSheet(u"color: black;")
        self.handingLinkLabel5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.handingLinkLabel4 = QLabel(self.keyWiringPage)
        self.handingLinkLabel4.setObjectName(u"handingLinkLabel4")
        self.handingLinkLabel4.setGeometry(QRect(435, 247, 16, 16))
        self.handingLinkLabel4.setFont(font6)
        self.handingLinkLabel4.setStyleSheet(u"color: black;")
        self.handingLinkLabel4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.topLine_13 = QFrame(self.keyWiringPage)
        self.topLine_13.setObjectName(u"topLine_13")
        self.topLine_13.setGeometry(QRect(424, 196, 149, 2))
        self.topLine_13.setFont(font4)
        self.topLine_13.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_13.setFrameShape(QFrame.Shape.HLine)
        self.topLine_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_14 = QFrame(self.keyWiringPage)
        self.topLine_14.setObjectName(u"topLine_14")
        self.topLine_14.setGeometry(QRect(424, 252, 71, 2))
        self.topLine_14.setFont(font4)
        self.topLine_14.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_14.setFrameShape(QFrame.Shape.HLine)
        self.topLine_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.handingLink5 = QRadioButton(self.keyWiringPage)
        self.handingLink5.setObjectName(u"handingLink5")
        self.handingLink5.setGeometry(QRect(417, 274, 16, 22))
        self.handingLink5.setFont(font5)
        self.handingLink5.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink5.setCheckable(False)
        self.handingLink5.setChecked(False)
        self.handingLink5.setAutoExclusive(False)
        self.lineEdit = QLineEdit(self.keyWiringPage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(404, 144, 54, 160))
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid black;\n"
"}")
        self.topLine_10 = QFrame(self.keyWiringPage)
        self.topLine_10.setObjectName(u"topLine_10")
        self.topLine_10.setGeometry(QRect(142, 253, 239, 2))
        self.topLine_10.setFont(font4)
        self.topLine_10.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_10.setFrameShape(QFrame.Shape.HLine)
        self.topLine_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.handingLinkLabel1 = QLabel(self.keyWiringPage)
        self.handingLinkLabel1.setObjectName(u"handingLinkLabel1")
        self.handingLinkLabel1.setGeometry(QRect(435, 161, 16, 16))
        self.handingLinkLabel1.setFont(font6)
        self.handingLinkLabel1.setStyleSheet(u"color: black;")
        self.handingLinkLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.topLine_7 = QFrame(self.keyWiringPage)
        self.topLine_7.setObjectName(u"topLine_7")
        self.topLine_7.setGeometry(QRect(92, 109, 633, 2))
        self.topLine_7.setFont(font4)
        self.topLine_7.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_7.setFrameShape(QFrame.Shape.HLine)
        self.topLine_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_6 = QFrame(self.keyWiringPage)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(423, 228, 2, 27))
        self.line_6.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.keyWiringPage)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(573, 194, 2, 444))
        self.line_3.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_16 = QFrame(self.keyWiringPage)
        self.topLine_16.setObjectName(u"topLine_16")
        self.topLine_16.setGeometry(QRect(250, 350, 255, 2))
        self.topLine_16.setFont(font4)
        self.topLine_16.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_16.setFrameShape(QFrame.Shape.HLine)
        self.topLine_16.setFrameShadow(QFrame.Shadow.Sunken)
        self.handingLink1 = QRadioButton(self.keyWiringPage)
        self.handingLink1.setObjectName(u"handingLink1")
        self.handingLink1.setGeometry(QRect(417, 158, 16, 22))
        self.handingLink1.setFont(font5)
        self.handingLink1.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink1.setCheckable(False)
        self.handingLink1.setChecked(False)
        self.handingLink1.setAutoExclusive(False)
        self.handingLink4_2 = QRadioButton(self.keyWiringPage)
        self.handingLink4_2.setObjectName(u"handingLink4_2")
        self.handingLink4_2.setGeometry(QRect(417, 242, 16, 22))
        self.handingLink4_2.setFont(font5)
        self.handingLink4_2.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink4_2.setCheckable(False)
        self.handingLink4_2.setChecked(False)
        self.handingLink4_2.setAutoExclusive(False)
        self.handingLinkLabel3_2 = QLabel(self.keyWiringPage)
        self.handingLinkLabel3_2.setObjectName(u"handingLinkLabel3_2")
        self.handingLinkLabel3_2.setGeometry(QRect(435, 217, 16, 16))
        self.handingLinkLabel3_2.setFont(font6)
        self.handingLinkLabel3_2.setStyleSheet(u"color: black;")
        self.handingLinkLabel3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.handingLinkLabel2_2 = QLabel(self.keyWiringPage)
        self.handingLinkLabel2_2.setObjectName(u"handingLinkLabel2_2")
        self.handingLinkLabel2_2.setGeometry(QRect(435, 189, 16, 16))
        self.handingLinkLabel2_2.setFont(font6)
        self.handingLinkLabel2_2.setStyleSheet(u"color: black;")
        self.handingLinkLabel2_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.handingLink3_2 = QRadioButton(self.keyWiringPage)
        self.handingLink3_2.setObjectName(u"handingLink3_2")
        self.handingLink3_2.setGeometry(QRect(417, 214, 16, 22))
        self.handingLink3_2.setFont(font5)
        self.handingLink3_2.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink3_2.setCheckable(False)
        self.handingLink3_2.setChecked(False)
        self.handingLink3_2.setAutoExclusive(False)
        self.handingLinkLabel5_2 = QLabel(self.keyWiringPage)
        self.handingLinkLabel5_2.setObjectName(u"handingLinkLabel5_2")
        self.handingLinkLabel5_2.setGeometry(QRect(435, 273, 16, 16))
        self.handingLinkLabel5_2.setFont(font6)
        self.handingLinkLabel5_2.setStyleSheet(u"color: black;")
        self.handingLinkLabel5_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.handingLinkLabel4_2 = QLabel(self.keyWiringPage)
        self.handingLinkLabel4_2.setObjectName(u"handingLinkLabel4_2")
        self.handingLinkLabel4_2.setGeometry(QRect(435, 245, 16, 16))
        self.handingLinkLabel4_2.setFont(font6)
        self.handingLinkLabel4_2.setStyleSheet(u"color: black;")
        self.handingLinkLabel4_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.handingLink5_2 = QRadioButton(self.keyWiringPage)
        self.handingLink5_2.setObjectName(u"handingLink5_2")
        self.handingLink5_2.setGeometry(QRect(417, 270, 16, 22))
        self.handingLink5_2.setFont(font5)
        self.handingLink5_2.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink5_2.setCheckable(False)
        self.handingLink5_2.setChecked(False)
        self.handingLink5_2.setAutoExclusive(False)
        self.handingLink2_2 = QRadioButton(self.keyWiringPage)
        self.handingLink2_2.setObjectName(u"handingLink2_2")
        self.handingLink2_2.setGeometry(QRect(417, 186, 16, 22))
        self.handingLink2_2.setFont(font5)
        self.handingLink2_2.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #FFFFFF; /* Background of the circle */\n"
"}")
        self.handingLink2_2.setCheckable(False)
        self.handingLink2_2.setChecked(False)
        self.handingLink2_2.setAutoExclusive(False)
        self.line_7 = QFrame(self.keyWiringPage)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(423, 166, 2, 27))
        self.line_7.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_11 = QFrame(self.keyWiringPage)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(380, 169, 2, 117))
        self.line_11.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-width: 2px;          /* Restrict height to 1px */\n"
"    min-width: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.handingLinkJoin = QRadioButton(self.keyWiringPage)
        self.handingLinkJoin.setObjectName(u"handingLinkJoin")
        self.handingLinkJoin.setGeometry(QRect(374, 184, 16, 22))
        self.handingLinkJoin.setFont(font5)
        self.handingLinkJoin.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 10px; /* Size of the circle */\n"
"    height: 10px; /* Size of the circle */\n"
"    border: 2px solid #000000; /* Border of the circle */\n"
"    border-radius: 5px; /* Makes the circle rounded */\n"
"    background-color: #000000; /* Background of the circle */\n"
"}")
        self.handingLinkJoin.setCheckable(False)
        self.handingLinkJoin.setChecked(False)
        self.topLine_17 = QFrame(self.keyWiringPage)
        self.topLine_17.setObjectName(u"topLine_17")
        self.topLine_17.setGeometry(QRect(380, 168, 44, 2))
        self.topLine_17.setFont(font4)
        self.topLine_17.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_17.setFrameShape(QFrame.Shape.HLine)
        self.topLine_17.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit = QTextEdit(self.keyWiringPage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(600, 157, 202, 66))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setItalic(True)
        self.textEdit.setFont(font12)
        self.textEdit.setStyleSheet(u"background: transparent;\n"
"border: none;\n"
"color: black;")
        self.stackedWidget.addWidget(self.keyWiringPage)
        self.line_9.raise_()
        self.line_10.raise_()
        self.topLine_15.raise_()
        self.line_8.raise_()
        self.topLine_14.raise_()
        self.line_3.raise_()
        self.topLine_13.raise_()
        self.topLine_10.raise_()
        self.topLine_9.raise_()
        self.line_2.raise_()
        self.topLine_7.raise_()
        self.rightStopLED.raise_()
        self.rightSafetyLED.raise_()
        self.callDownLabel.raise_()
        self.leftFootrestLED.raise_()
        self.leftSkateLED.raise_()
        self.leftSafetyLED.raise_()
        self.handing4Label.raise_()
        self.leftSkateLabel.raise_()
        self.osgReturnLED.raise_()
        self.osgReturnLabel.raise_()
        self.callUpLED.raise_()
        self.handing2LED.raise_()
        self.bistableReturnLabel.raise_()
        self.ultimateLabel.raise_()
        self.bottomFootrestLED.raise_()
        self.rightFootrestLED.raise_()
        self.ultimateLED.raise_()
        self.relayCoilMonitorLabel.raise_()
        self.leftSafetyLabel.raise_()
        self.callUpLabel.raise_()
        self.rightSafetyLabel.raise_()
        self.swivelOverrideLabel.raise_()
        self.leftFootrestLabel.raise_()
        self.bistableReturnLED.raise_()
        self.handing4LED.raise_()
        self.bistableFeedLabel.raise_()
        self.rightSkateLED.raise_()
        self.rightStopLabel.raise_()
        self.bistableFeedLED.raise_()
        self.handing2Label.raise_()
        self.callDownLED.raise_()
        self.leftStopLED.raise_()
        self.leftStopLabel.raise_()
        self.bottomFootrestLabel.raise_()
        self.rightSkateLabel.raise_()
        self.rightFootrestLabel.raise_()
        self.relayCoilMonitorLED.raise_()
        self.swivelOverrideLED.raise_()
        self.handingLink4.raise_()
        self.line_4.raise_()
        self.topLine_12.raise_()
        self.topLine_8.raise_()
        self.line_5.raise_()
        self.handingLinkLabel3.raise_()
        self.handingLinkLabel2.raise_()
        self.handingLink3.raise_()
        self.handingLinkLabel5.raise_()
        self.handingLinkLabel4.raise_()
        self.handingLink5.raise_()
        self.lineEdit.raise_()
        self.handingLinkLabel1.raise_()
        self.line_6.raise_()
        self.topLine_16.raise_()
        self.handingLink4_2.raise_()
        self.handingLinkLabel3_2.raise_()
        self.handingLinkLabel2_2.raise_()
        self.handingLink3_2.raise_()
        self.handingLinkLabel5_2.raise_()
        self.handingLinkLabel4_2.raise_()
        self.handingLink5_2.raise_()
        self.line_7.raise_()
        self.line_11.raise_()
        self.handingLinkJoin.raise_()
        self.topLine_17.raise_()
        self.handingLink1.raise_()
        self.handingLink2_2.raise_()
        self.textEdit.raise_()
        self.railMappingPage = QWidget()
        self.railMappingPage.setObjectName(u"railMappingPage")
        self.railMapBox = QGroupBox(self.railMappingPage)
        self.railMapBox.setObjectName(u"railMapBox")
        self.railMapBox.setGeometry(QRect(16, 15, 787, 793))
        self.railMapBox.setFont(font6)
        self.railMapBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.mapPointsTable = QTableWidget(self.railMapBox)
        if (self.mapPointsTable.columnCount() < 3):
            self.mapPointsTable.setColumnCount(3)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.mapPointsTable.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.mapPointsTable.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.mapPointsTable.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        self.mapPointsTable.setObjectName(u"mapPointsTable")
        self.mapPointsTable.setGeometry(QRect(19, 50, 270, 209))
        self.mapPointsTable.setFont(font8)
        self.mapPointsTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.mapPointsTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mapPointsTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.mapPointsTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mapPointsTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mapPointsTable.setAutoScroll(False)
        self.mapPointsTable.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        self.mapPointsTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.mapPointsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.mapPointsTable.horizontalHeader().setMinimumSectionSize(40)
        self.mapPointsTable.horizontalHeader().setDefaultSectionSize(89)
        self.mapPointsTable.horizontalHeader().setStretchLastSection(False)
        self.mapPointsTable.verticalHeader().setVisible(False)
        self.mapPointsTable.verticalHeader().setMinimumSectionSize(14)
        self.mapPointsTable.verticalHeader().setDefaultSectionSize(18)
        self.mainMapModeGroup = QGroupBox(self.railMapBox)
        self.mainMapModeGroup.setObjectName(u"mainMapModeGroup")
        self.mainMapModeGroup.setGeometry(QRect(578, 190, 191, 587))
        self.mainMapModeGroup.setFont(font6)
        self.mainMapModeGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 10px;\n"
"}")
        self.modeRemoteDButton = QRadioButton(self.mainMapModeGroup)
        self.modeRemoteDButton.setObjectName(u"modeRemoteDButton")
        self.modeRemoteDButton.setEnabled(True)
        self.modeRemoteDButton.setGeometry(QRect(33, 380, 134, 22))
        self.modeRemoteDButton.setFont(font5)
        self.modeRemoteDButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeRemoteDButton.setChecked(False)
        self.modeRemoteDButton.setAutoExclusive(False)
        self.modePartialUnfoldButton = QRadioButton(self.mainMapModeGroup)
        self.modePartialUnfoldButton.setObjectName(u"modePartialUnfoldButton")
        self.modePartialUnfoldButton.setGeometry(QRect(33, 222, 126, 22))
        self.modePartialUnfoldButton.setFont(font5)
        self.modePartialUnfoldButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modePartialUnfoldButton.setChecked(False)
        self.modePartialUnfoldButton.setAutoExclusive(False)
        self.modeHalfSpeedButton = QRadioButton(self.mainMapModeGroup)
        self.modeHalfSpeedButton.setObjectName(u"modeHalfSpeedButton")
        self.modeHalfSpeedButton.setGeometry(QRect(33, 246, 128, 22))
        self.modeHalfSpeedButton.setFont(font5)
        self.modeHalfSpeedButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeHalfSpeedButton.setChecked(False)
        self.modeHalfSpeedButton.setAutoExclusive(False)
        self.modeRemoteBButton = QRadioButton(self.mainMapModeGroup)
        self.modeRemoteBButton.setObjectName(u"modeRemoteBButton")
        self.modeRemoteBButton.setGeometry(QRect(33, 331, 128, 22))
        self.modeRemoteBButton.setFont(font5)
        self.modeRemoteBButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeRemoteBButton.setChecked(False)
        self.modeRemoteBButton.setAutoExclusive(False)
        self.modeRemoteCButton = QRadioButton(self.mainMapModeGroup)
        self.modeRemoteCButton.setObjectName(u"modeRemoteCButton")
        self.modeRemoteCButton.setGeometry(QRect(33, 356, 134, 22))
        self.modeRemoteCButton.setFont(font5)
        self.modeRemoteCButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeRemoteCButton.setChecked(False)
        self.modeRemoteCButton.setAutoExclusive(False)
        self.modeSwivelRightButton = QRadioButton(self.mainMapModeGroup)
        self.modeSwivelRightButton.setObjectName(u"modeSwivelRightButton")
        self.modeSwivelRightButton.setGeometry(QRect(33, 182, 134, 22))
        self.modeSwivelRightButton.setFont(font5)
        self.modeSwivelRightButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeSwivelRightButton.setChecked(False)
        self.modeSwivelRightButton.setAutoExclusive(False)
        self.modeRemoteAButton = QRadioButton(self.mainMapModeGroup)
        self.modeRemoteAButton.setObjectName(u"modeRemoteAButton")
        self.modeRemoteAButton.setGeometry(QRect(33, 307, 126, 22))
        self.modeRemoteAButton.setFont(font5)
        self.modeRemoteAButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeRemoteAButton.setChecked(False)
        self.modeRemoteAButton.setAutoExclusive(False)
        self.modeUnpackButton = QRadioButton(self.mainMapModeGroup)
        self.modeUnpackButton.setObjectName(u"modeUnpackButton")
        self.modeUnpackButton.setGeometry(QRect(33, 133, 119, 22))
        self.modeUnpackButton.setFont(font5)
        self.modeUnpackButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeUnpackButton.setChecked(False)
        self.modeUnpackButton.setAutoExclusive(False)
        self.modeFullSwivelButton = QRadioButton(self.mainMapModeGroup)
        self.modeFullSwivelButton.setObjectName(u"modeFullSwivelButton")
        self.modeFullSwivelButton.setGeometry(QRect(33, 271, 134, 22))
        self.modeFullSwivelButton.setFont(font5)
        self.modeFullSwivelButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeFullSwivelButton.setChecked(False)
        self.modeFullSwivelButton.setAutoExclusive(False)
        self.modeParkingPointButton = QRadioButton(self.mainMapModeGroup)
        self.modeParkingPointButton.setObjectName(u"modeParkingPointButton")
        self.modeParkingPointButton.setGeometry(QRect(33, 93, 78, 22))
        self.modeParkingPointButton.setFont(font5)
        self.modeParkingPointButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeParkingPointButton.setChecked(False)
        self.modeParkingPointButton.setAutoExclusive(False)
        self.modeSwivelLeftButton = QRadioButton(self.mainMapModeGroup)
        self.modeSwivelLeftButton.setObjectName(u"modeSwivelLeftButton")
        self.modeSwivelLeftButton.setGeometry(QRect(33, 157, 128, 22))
        self.modeSwivelLeftButton.setFont(font5)
        self.modeSwivelLeftButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeSwivelLeftButton.setChecked(False)
        self.modeSwivelLeftButton.setAutoExclusive(False)
        self.modeBoardingPointButton = QRadioButton(self.mainMapModeGroup)
        self.modeBoardingPointButton.setObjectName(u"modeBoardingPointButton")
        self.modeBoardingPointButton.setGeometry(QRect(33, 69, 78, 22))
        self.modeBoardingPointButton.setFont(font5)
        self.modeBoardingPointButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeBoardingPointButton.setChecked(False)
        self.modeBoardingPointButton.setAutoExclusive(False)
        self.topLine_18 = QFrame(self.mainMapModeGroup)
        self.topLine_18.setObjectName(u"topLine_18")
        self.topLine_18.setGeometry(QRect(23, 124, 145, 2))
        self.topLine_18.setFont(font4)
        self.topLine_18.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_18.setFrameShape(QFrame.Shape.HLine)
        self.topLine_18.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_19 = QFrame(self.mainMapModeGroup)
        self.topLine_19.setObjectName(u"topLine_19")
        self.topLine_19.setGeometry(QRect(23, 212, 145, 2))
        self.topLine_19.setFont(font4)
        self.topLine_19.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_19.setFrameShape(QFrame.Shape.HLine)
        self.topLine_19.setFrameShadow(QFrame.Shadow.Sunken)
        self.topLine_20 = QFrame(self.mainMapModeGroup)
        self.topLine_20.setObjectName(u"topLine_20")
        self.topLine_20.setGeometry(QRect(23, 300, 145, 2))
        self.topLine_20.setFont(font4)
        self.topLine_20.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_20.setFrameShape(QFrame.Shape.HLine)
        self.topLine_20.setFrameShadow(QFrame.Shadow.Sunken)
        self.updatePointButton = QPushButton(self.mainMapModeGroup)
        self.updatePointButton.setObjectName(u"updatePointButton")
        self.updatePointButton.setGeometry(QRect(47, 540, 93, 28))
        self.updatePointButton.setStyleSheet(u"QPushButton {\n"
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
        self.modeEnabledButton = QRadioButton(self.mainMapModeGroup)
        self.modeEnabledButton.setObjectName(u"modeEnabledButton")
        self.modeEnabledButton.setGeometry(QRect(33, 46, 70, 20))
        self.modeEnabledButton.setFont(font5)
        self.modeEnabledButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.modeEnabledButton.setChecked(False)
        self.modeEnabledButton.setAutoExclusive(False)
        self.zoneWidthText = QLineEdit(self.mainMapModeGroup)
        self.zoneWidthText.setObjectName(u"zoneWidthText")
        self.zoneWidthText.setGeometry(QRect(31, 416, 127, 22))
        self.zoneWidthText.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"	background-color: #FFFFFF;\n"
"	color: black;\n"
"}")
        self.zoneWidthText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zoneWidthLabel = QLabel(self.mainMapModeGroup)
        self.zoneWidthLabel.setObjectName(u"zoneWidthLabel")
        self.zoneWidthLabel.setGeometry(QRect(46, 441, 98, 20))
        self.zoneWidthLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.newPointPositionText = QLineEdit(self.mainMapModeGroup)
        self.newPointPositionText.setObjectName(u"newPointPositionText")
        self.newPointPositionText.setGeometry(QRect(16, 480, 108, 22))
        self.newPointPositionText.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"	background-color: #FFFFFF;\n"
"	color: black;\n"
"}")
        self.newPointPositionText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pointPositionLabel = QLabel(self.mainMapModeGroup)
        self.pointPositionLabel.setObjectName(u"pointPositionLabel")
        self.pointPositionLabel.setGeometry(QRect(30, 505, 80, 20))
        self.pointPositionLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.copyPositionButton = QPushButton(self.mainMapModeGroup)
        self.copyPositionButton.setObjectName(u"copyPositionButton")
        self.copyPositionButton.setGeometry(QRect(131, 480, 43, 22))
        self.copyPositionButton.setStyleSheet(u"QPushButton {\n"
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
        self.mainCurrentPointGroup = QGroupBox(self.railMapBox)
        self.mainCurrentPointGroup.setObjectName(u"mainCurrentPointGroup")
        self.mainCurrentPointGroup.setGeometry(QRect(19, 639, 543, 138))
        self.mainCurrentPointGroup.setFont(font6)
        self.mainCurrentPointGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 10px;\n"
"}")
        self.leftStopButton = QRadioButton(self.mainCurrentPointGroup)
        self.leftStopButton.setObjectName(u"leftStopButton")
        self.leftStopButton.setEnabled(False)
        self.leftStopButton.setGeometry(QRect(17, 39, 78, 22))
        self.leftStopButton.setFont(font5)
        self.leftStopButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.leftStopButton.setChecked(False)
        self.leftStopButton.setAutoExclusive(False)
        self.middleStopButton = QRadioButton(self.mainCurrentPointGroup)
        self.middleStopButton.setObjectName(u"middleStopButton")
        self.middleStopButton.setEnabled(False)
        self.middleStopButton.setGeometry(QRect(17, 60, 91, 22))
        self.middleStopButton.setFont(font5)
        self.middleStopButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.middleStopButton.setChecked(False)
        self.middleStopButton.setAutoExclusive(False)
        self.rightStopButton = QRadioButton(self.mainCurrentPointGroup)
        self.rightStopButton.setObjectName(u"rightStopButton")
        self.rightStopButton.setEnabled(False)
        self.rightStopButton.setGeometry(QRect(17, 80, 78, 22))
        self.rightStopButton.setFont(font5)
        self.rightStopButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.rightStopButton.setChecked(False)
        self.rightStopButton.setAutoExclusive(False)
        self.parkPointButton = QRadioButton(self.mainCurrentPointGroup)
        self.parkPointButton.setObjectName(u"parkPointButton")
        self.parkPointButton.setEnabled(False)
        self.parkPointButton.setGeometry(QRect(17, 100, 91, 22))
        self.parkPointButton.setFont(font5)
        self.parkPointButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.parkPointButton.setChecked(False)
        self.parkPointButton.setAutoExclusive(False)
        self.partialUnfoldLeftButton = QRadioButton(self.mainCurrentPointGroup)
        self.partialUnfoldLeftButton.setObjectName(u"partialUnfoldLeftButton")
        self.partialUnfoldLeftButton.setEnabled(False)
        self.partialUnfoldLeftButton.setGeometry(QRect(187, 80, 136, 22))
        self.partialUnfoldLeftButton.setFont(font5)
        self.partialUnfoldLeftButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.partialUnfoldLeftButton.setChecked(False)
        self.partialUnfoldLeftButton.setAutoExclusive(False)
        self.halfSpeedButton = QRadioButton(self.mainCurrentPointGroup)
        self.halfSpeedButton.setObjectName(u"halfSpeedButton")
        self.halfSpeedButton.setEnabled(False)
        self.halfSpeedButton.setGeometry(QRect(187, 39, 113, 22))
        self.halfSpeedButton.setFont(font5)
        self.halfSpeedButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.halfSpeedButton.setChecked(False)
        self.halfSpeedButton.setAutoExclusive(False)
        self.partialUnfoldRightButton = QRadioButton(self.mainCurrentPointGroup)
        self.partialUnfoldRightButton.setObjectName(u"partialUnfoldRightButton")
        self.partialUnfoldRightButton.setEnabled(False)
        self.partialUnfoldRightButton.setGeometry(QRect(187, 100, 142, 22))
        self.partialUnfoldRightButton.setFont(font5)
        self.partialUnfoldRightButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.partialUnfoldRightButton.setChecked(False)
        self.partialUnfoldRightButton.setAutoExclusive(False)
        self.partialUnfoldZoneButton = QRadioButton(self.mainCurrentPointGroup)
        self.partialUnfoldZoneButton.setObjectName(u"partialUnfoldZoneButton")
        self.partialUnfoldZoneButton.setEnabled(False)
        self.partialUnfoldZoneButton.setGeometry(QRect(187, 60, 132, 22))
        self.partialUnfoldZoneButton.setFont(font5)
        self.partialUnfoldZoneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.partialUnfoldZoneButton.setChecked(False)
        self.partialUnfoldZoneButton.setAutoExclusive(False)
        self.swivelFullAngleButton = QRadioButton(self.mainCurrentPointGroup)
        self.swivelFullAngleButton.setObjectName(u"swivelFullAngleButton")
        self.swivelFullAngleButton.setEnabled(False)
        self.swivelFullAngleButton.setGeometry(QRect(397, 80, 123, 22))
        self.swivelFullAngleButton.setFont(font5)
        self.swivelFullAngleButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.swivelFullAngleButton.setChecked(False)
        self.swivelFullAngleButton.setAutoExclusive(False)
        self.swivelLeftButton = QRadioButton(self.mainCurrentPointGroup)
        self.swivelLeftButton.setObjectName(u"swivelLeftButton")
        self.swivelLeftButton.setEnabled(False)
        self.swivelLeftButton.setGeometry(QRect(397, 39, 130, 22))
        self.swivelLeftButton.setFont(font5)
        self.swivelLeftButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.swivelLeftButton.setChecked(False)
        self.swivelLeftButton.setAutoExclusive(False)
        self.unpackArrivalButton = QRadioButton(self.mainCurrentPointGroup)
        self.unpackArrivalButton.setObjectName(u"unpackArrivalButton")
        self.unpackArrivalButton.setEnabled(False)
        self.unpackArrivalButton.setGeometry(QRect(397, 100, 125, 22))
        self.unpackArrivalButton.setFont(font5)
        self.unpackArrivalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.unpackArrivalButton.setChecked(False)
        self.unpackArrivalButton.setAutoExclusive(False)
        self.swivelRightButton = QRadioButton(self.mainCurrentPointGroup)
        self.swivelRightButton.setObjectName(u"swivelRightButton")
        self.swivelRightButton.setEnabled(False)
        self.swivelRightButton.setGeometry(QRect(397, 60, 135, 22))
        self.swivelRightButton.setFont(font5)
        self.swivelRightButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.swivelRightButton.setChecked(False)
        self.swivelRightButton.setAutoExclusive(False)
        self.mainCalibrationGroup = QGroupBox(self.railMapBox)
        self.mainCalibrationGroup.setObjectName(u"mainCalibrationGroup")
        self.mainCalibrationGroup.setGeometry(QRect(578, 50, 191, 123))
        self.mainCalibrationGroup.setFont(font6)
        self.mainCalibrationGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.autoMainCalButton = QRadioButton(self.mainCalibrationGroup)
        self.autoMainCalButton.setObjectName(u"autoMainCalButton")
        self.autoMainCalButton.setGeometry(QRect(29, 90, 63, 22))
        self.autoMainCalButton.setFont(font5)
        self.autoMainCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoMainCalButton.setChecked(False)
        self.autoMainCalButton.setAutoExclusive(True)
        self.manualMainCalButton = QRadioButton(self.mainCalibrationGroup)
        self.manualMainCalButton.setObjectName(u"manualMainCalButton")
        self.manualMainCalButton.setGeometry(QRect(99, 90, 72, 22))
        self.manualMainCalButton.setFont(font5)
        self.manualMainCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualMainCalButton.setChecked(True)
        self.manualMainCalButton.setAutoExclusive(True)
        self.startMainCalButton = QPushButton(self.mainCalibrationGroup)
        self.startMainCalButton.setObjectName(u"startMainCalButton")
        self.startMainCalButton.setGeometry(QRect(10, 50, 49, 27))
        self.startMainCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.acceptMainCalButton = QPushButton(self.mainCalibrationGroup)
        self.acceptMainCalButton.setObjectName(u"acceptMainCalButton")
        self.acceptMainCalButton.setGeometry(QRect(70, 50, 49, 27))
        self.acceptMainCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.rejectMainCalButton = QPushButton(self.mainCalibrationGroup)
        self.rejectMainCalButton.setObjectName(u"rejectMainCalButton")
        self.rejectMainCalButton.setGeometry(QRect(130, 50, 49, 27))
        self.rejectMainCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.mainNewPositionText = QLineEdit(self.railMapBox)
        self.mainNewPositionText.setObjectName(u"mainNewPositionText")
        self.mainNewPositionText.setGeometry(QRect(305, 210, 138, 22))
        self.mainNewPositionText.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"	background-color: #FFFFFF;\n"
"	color: black;\n"
"}")
        self.mainNewPositionText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setPositionButton = QPushButton(self.railMapBox)
        self.setPositionButton.setObjectName(u"setPositionButton")
        self.setPositionButton.setGeometry(QRect(451, 210, 51, 22))
        self.setPositionButton.setStyleSheet(u"QPushButton {\n"
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
        self.zeroPositionButton = QPushButton(self.railMapBox)
        self.zeroPositionButton.setObjectName(u"zeroPositionButton")
        self.zeroPositionButton.setGeometry(QRect(511, 210, 51, 22))
        self.zeroPositionButton.setStyleSheet(u"QPushButton {\n"
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
        self.mapDataTable = QTableWidget(self.railMapBox)
        if (self.mapDataTable.columnCount() < 2):
            self.mapDataTable.setColumnCount(2)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.mapDataTable.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.mapDataTable.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        self.mapDataTable.setObjectName(u"mapDataTable")
        self.mapDataTable.setGeometry(QRect(305, 50, 257, 147))
        self.mapDataTable.setFont(font8)
        self.mapDataTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mapDataTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.mapDataTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mapDataTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mapDataTable.setAutoScroll(False)
        self.mapDataTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.mapDataTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.mapDataTable.horizontalHeader().setVisible(False)
        self.mapDataTable.horizontalHeader().setMinimumSectionSize(100)
        self.mapDataTable.horizontalHeader().setDefaultSectionSize(127)
        self.mapDataTable.horizontalHeader().setStretchLastSection(False)
        self.mapDataTable.verticalHeader().setVisible(False)
        self.mapDataTable.verticalHeader().setMinimumSectionSize(18)
        self.mapDataTable.verticalHeader().setDefaultSectionSize(18)
        self.saveMapFileButton = QPushButton(self.railMapBox)
        self.saveMapFileButton.setObjectName(u"saveMapFileButton")
        self.saveMapFileButton.setGeometry(QRect(238, 16, 51, 22))
        self.saveMapFileButton.setStyleSheet(u"QPushButton {\n"
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
        self.injectMapButton = QPushButton(self.railMapBox)
        self.injectMapButton.setObjectName(u"injectMapButton")
        self.injectMapButton.setGeometry(QRect(179, 16, 51, 22))
        self.injectMapButton.setStyleSheet(u"QPushButton {\n"
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
        self.mainPointGroup_2 = QGroupBox(self.railMapBox)
        self.mainPointGroup_2.setObjectName(u"mainPointGroup_2")
        self.mainPointGroup_2.setGeometry(QRect(19, 272, 271, 212))
        self.mainPointGroup_2.setFont(font6)
        self.mainPointGroup_2.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #FFC559;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 10px;\n"
"}")
        self.wipeMapButton = QPushButton(self.mainPointGroup_2)
        self.wipeMapButton.setObjectName(u"wipeMapButton")
        self.wipeMapButton.setGeometry(QRect(21, 150, 51, 37))
        self.wipeMapButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.deleteMapPoint = QPushButton(self.mainPointGroup_2)
        self.deleteMapPoint.setObjectName(u"deleteMapPoint")
        self.deleteMapPoint.setGeometry(QRect(21, 100, 51, 37))
        self.deleteMapPoint.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.saveMapButton = QPushButton(self.mainPointGroup_2)
        self.saveMapButton.setObjectName(u"saveMapButton")
        self.saveMapButton.setGeometry(QRect(201, 150, 50, 37))
        self.saveMapButton.setStyleSheet(u"QPushButton {\n"
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
        self.disableModeButton = QPushButton(self.mainPointGroup_2)
        self.disableModeButton.setObjectName(u"disableModeButton")
        self.disableModeButton.setGeometry(QRect(21, 43, 51, 37))
        self.disableModeButton.setStyleSheet(u"QPushButton {\n"
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
        self.editModeButton = QPushButton(self.mainPointGroup_2)
        self.editModeButton.setObjectName(u"editModeButton")
        self.editModeButton.setGeometry(QRect(81, 43, 51, 37))
        self.editModeButton.setStyleSheet(u"QPushButton {\n"
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
        self.confirmWipeMapButton = QRadioButton(self.mainPointGroup_2)
        self.confirmWipeMapButton.setObjectName(u"confirmWipeMapButton")
        self.confirmWipeMapButton.setEnabled(True)
        self.confirmWipeMapButton.setGeometry(QRect(81, 157, 69, 22))
        self.confirmWipeMapButton.setFont(font5)
        self.confirmWipeMapButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.confirmWipeMapButton.setChecked(False)
        self.confirmWipeMapButton.setAutoExclusive(False)
        self.findModeButton = QPushButton(self.mainPointGroup_2)
        self.findModeButton.setObjectName(u"findModeButton")
        self.findModeButton.setGeometry(QRect(141, 43, 50, 37))
        self.findModeButton.setStyleSheet(u"QPushButton {\n"
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
        self.confirmDeletePointButton = QRadioButton(self.mainPointGroup_2)
        self.confirmDeletePointButton.setObjectName(u"confirmDeletePointButton")
        self.confirmDeletePointButton.setEnabled(True)
        self.confirmDeletePointButton.setGeometry(QRect(81, 107, 69, 22))
        self.confirmDeletePointButton.setFont(font5)
        self.confirmDeletePointButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.confirmDeletePointButton.setChecked(False)
        self.confirmDeletePointButton.setAutoExclusive(False)
        self.loadMapButton = QPushButton(self.mainPointGroup_2)
        self.loadMapButton.setObjectName(u"loadMapButton")
        self.loadMapButton.setGeometry(QRect(201, 100, 50, 37))
        self.loadMapButton.setStyleSheet(u"QPushButton {\n"
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
        self.restrictModeButton = QPushButton(self.mainPointGroup_2)
        self.restrictModeButton.setObjectName(u"restrictModeButton")
        self.restrictModeButton.setGeometry(QRect(201, 43, 50, 37))
        self.restrictModeButton.setStyleSheet(u"QPushButton {\n"
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
        self.mainPointGroup = QGroupBox(self.railMapBox)
        self.mainPointGroup.setObjectName(u"mainPointGroup")
        self.mainPointGroup.setGeometry(QRect(19, 497, 271, 129))
        self.mainPointGroup.setFont(font6)
        self.mainPointGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #FFC559;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 10px;\n"
"}")
        self.boardingPointButton = QPushButton(self.mainPointGroup)
        self.boardingPointButton.setObjectName(u"boardingPointButton")
        self.boardingPointButton.setGeometry(QRect(19, 44, 55, 37))
        self.boardingPointButton.setStyleSheet(u"QPushButton {\n"
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
        self.partFoldPointButton = QPushButton(self.mainPointGroup)
        self.partFoldPointButton.setObjectName(u"partFoldPointButton")
        self.partFoldPointButton.setGeometry(QRect(196, 44, 55, 37))
        self.partFoldPointButton.setStyleSheet(u"QPushButton {\n"
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
        self.parkingPointButton = QPushButton(self.mainPointGroup)
        self.parkingPointButton.setObjectName(u"parkingPointButton")
        self.parkingPointButton.setGeometry(QRect(78, 44, 55, 37))
        self.parkingPointButton.setStyleSheet(u"QPushButton {\n"
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
        self.halfSpeedPointButton = QPushButton(self.mainPointGroup)
        self.halfSpeedPointButton.setObjectName(u"halfSpeedPointButton")
        self.halfSpeedPointButton.setGeometry(QRect(137, 44, 55, 37))
        self.halfSpeedPointButton.setStyleSheet(u"QPushButton {\n"
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
        self.positionToSpecifyText = QLineEdit(self.mainPointGroup)
        self.positionToSpecifyText.setObjectName(u"positionToSpecifyText")
        self.positionToSpecifyText.setGeometry(QRect(138, 93, 114, 22))
        self.positionToSpecifyText.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"	background-color: #FFFFFF;\n"
"	color: black;\n"
"}")
        self.positionToSpecifyText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.specifyPositionButton = QRadioButton(self.mainPointGroup)
        self.specifyPositionButton.setObjectName(u"specifyPositionButton")
        self.specifyPositionButton.setEnabled(True)
        self.specifyPositionButton.setGeometry(QRect(19, 92, 109, 23))
        self.specifyPositionButton.setFont(font5)
        self.specifyPositionButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.specifyPositionButton.setChecked(False)
        self.specifyPositionButton.setAutoExclusive(False)
        self.boardingPointButton.raise_()
        self.parkingPointButton.raise_()
        self.partFoldPointButton.raise_()
        self.halfSpeedPointButton.raise_()
        self.positionToSpecifyText.raise_()
        self.specifyPositionButton.raise_()
        self.mainLocatingGroup = QGroupBox(self.railMapBox)
        self.mainLocatingGroup.setObjectName(u"mainLocatingGroup")
        self.mainLocatingGroup.setGeometry(QRect(305, 246, 257, 238))
        self.mainLocatingGroup.setFont(font6)
        self.mainLocatingGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #FFC559;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 10px;\n"
"}")
        self.findLeftPosButton = QRadioButton(self.mainLocatingGroup)
        self.rmmLocatingButtonGroup = QButtonGroup(MainWindow)
        self.rmmLocatingButtonGroup.setObjectName(u"rmmLocatingButtonGroup")
        self.rmmLocatingButtonGroup.addButton(self.findLeftPosButton)
        self.findLeftPosButton.setObjectName(u"findLeftPosButton")
        self.findLeftPosButton.setEnabled(True)
        self.findLeftPosButton.setGeometry(QRect(15, 200, 69, 22))
        self.findLeftPosButton.setFont(font5)
        self.findLeftPosButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.findLeftPosButton.setChecked(True)
        self.findLeftPosButton.setAutoExclusive(False)
        self.findBothPosButton = QRadioButton(self.mainLocatingGroup)
        self.rmmLocatingButtonGroup.addButton(self.findBothPosButton)
        self.findBothPosButton.setObjectName(u"findBothPosButton")
        self.findBothPosButton.setEnabled(True)
        self.findBothPosButton.setGeometry(QRect(105, 200, 69, 22))
        self.findBothPosButton.setFont(font5)
        self.findBothPosButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.findBothPosButton.setChecked(False)
        self.findBothPosButton.setAutoExclusive(False)
        self.findRightPosButton = QRadioButton(self.mainLocatingGroup)
        self.rmmLocatingButtonGroup.addButton(self.findRightPosButton)
        self.findRightPosButton.setObjectName(u"findRightPosButton")
        self.findRightPosButton.setEnabled(True)
        self.findRightPosButton.setGeometry(QRect(196, 200, 54, 22))
        self.findRightPosButton.setFont(font5)
        self.findRightPosButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background: transparent;\n"
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
        self.findRightPosButton.setChecked(False)
        self.findRightPosButton.setAutoExclusive(False)
        self.locateBoardingButton = QPushButton(self.mainLocatingGroup)
        self.locateBoardingButton.setObjectName(u"locateBoardingButton")
        self.locateBoardingButton.setGeometry(QRect(39, 46, 55, 37))
        self.locateBoardingButton.setStyleSheet(u"QPushButton {\n"
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
        self.locateParkingButton = QPushButton(self.mainLocatingGroup)
        self.locateParkingButton.setObjectName(u"locateParkingButton")
        self.locateParkingButton.setGeometry(QRect(102, 46, 55, 37))
        self.locateParkingButton.setStyleSheet(u"QPushButton {\n"
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
        self.locateRemoteAButton = QPushButton(self.mainLocatingGroup)
        self.locateRemoteAButton.setObjectName(u"locateRemoteAButton")
        self.locateRemoteAButton.setGeometry(QRect(62, 92, 55, 37))
        self.locateRemoteAButton.setStyleSheet(u"QPushButton {\n"
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
        self.locateRemoteBButton = QPushButton(self.mainLocatingGroup)
        self.locateRemoteBButton.setObjectName(u"locateRemoteBButton")
        self.locateRemoteBButton.setGeometry(QRect(125, 92, 55, 37))
        self.locateRemoteBButton.setStyleSheet(u"QPushButton {\n"
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
        self.locateRemoteCButton = QPushButton(self.mainLocatingGroup)
        self.locateRemoteCButton.setObjectName(u"locateRemoteCButton")
        self.locateRemoteCButton.setGeometry(QRect(62, 140, 55, 37))
        self.locateRemoteCButton.setStyleSheet(u"QPushButton {\n"
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
        self.locateRemoteDButton = QPushButton(self.mainLocatingGroup)
        self.locateRemoteDButton.setObjectName(u"locateRemoteDButton")
        self.locateRemoteDButton.setGeometry(QRect(125, 140, 55, 37))
        self.locateRemoteDButton.setStyleSheet(u"QPushButton {\n"
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
        self.locateNextRailButton = QPushButton(self.mainLocatingGroup)
        self.locateNextRailButton.setObjectName(u"locateNextRailButton")
        self.locateNextRailButton.setGeometry(QRect(165, 46, 55, 37))
        self.locateNextRailButton.setStyleSheet(u"QPushButton {\n"
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
        self.clearMapTableButton = QPushButton(self.railMapBox)
        self.clearMapTableButton.setObjectName(u"clearMapTableButton")
        self.clearMapTableButton.setGeometry(QRect(19, 16, 51, 22))
        self.clearMapTableButton.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.railMappingPage)
        self.systemPage = QWidget()
        self.systemPage.setObjectName(u"systemPage")
        self.sysVersionGroup = QGroupBox(self.systemPage)
        self.sysVersionGroup.setObjectName(u"sysVersionGroup")
        self.sysVersionGroup.setGeometry(QRect(17, 16, 278, 215))
        self.sysVersionGroup.setFont(font6)
        self.sysVersionGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.requestSystemVersionButton = QPushButton(self.sysVersionGroup)
        self.requestSystemVersionButton.setObjectName(u"requestSystemVersionButton")
        self.requestSystemVersionButton.setGeometry(QRect(18, 15, 51, 22))
        self.requestSystemVersionButton.setStyleSheet(u"QPushButton {\n"
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
        self.sysVerTable = QTableWidget(self.sysVersionGroup)
        if (self.sysVerTable.columnCount() < 2):
            self.sysVerTable.setColumnCount(2)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.sysVerTable.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.sysVerTable.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        self.sysVerTable.setObjectName(u"sysVerTable")
        self.sysVerTable.setGeometry(QRect(18, 51, 241, 147))
        self.sysVerTable.setFont(font8)
        self.sysVerTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.sysVerTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.sysVerTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.sysVerTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.sysVerTable.setAutoScroll(False)
        self.sysVerTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.sysVerTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.sysVerTable.horizontalHeader().setVisible(False)
        self.sysVerTable.horizontalHeader().setMinimumSectionSize(80)
        self.sysVerTable.horizontalHeader().setDefaultSectionSize(120)
        self.sysVerTable.horizontalHeader().setStretchLastSection(False)
        self.sysVerTable.verticalHeader().setVisible(False)
        self.sysVerTable.verticalHeader().setMinimumSectionSize(16)
        self.sysVerTable.verticalHeader().setDefaultSectionSize(18)
        self.timeGroup = QGroupBox(self.systemPage)
        self.timeGroup.setObjectName(u"timeGroup")
        self.timeGroup.setGeometry(QRect(313, 16, 278, 178))
        self.timeGroup.setFont(font6)
        self.timeGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.setRTCButton = QPushButton(self.timeGroup)
        self.setRTCButton.setObjectName(u"setRTCButton")
        self.setRTCButton.setGeometry(QRect(18, 140, 241, 22))
        self.setRTCButton.setStyleSheet(u"QPushButton {\n"
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
        self.timeTable = QTableWidget(self.timeGroup)
        if (self.timeTable.columnCount() < 2):
            self.timeTable.setColumnCount(2)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.timeTable.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.timeTable.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        self.timeTable.setObjectName(u"timeTable")
        self.timeTable.setGeometry(QRect(18, 51, 242, 75))
        self.timeTable.setFont(font8)
        self.timeTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.timeTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.timeTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.timeTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.timeTable.setAutoScroll(False)
        self.timeTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.timeTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.timeTable.horizontalHeader().setVisible(False)
        self.timeTable.horizontalHeader().setMinimumSectionSize(80)
        self.timeTable.horizontalHeader().setDefaultSectionSize(120)
        self.timeTable.horizontalHeader().setStretchLastSection(False)
        self.timeTable.verticalHeader().setVisible(False)
        self.timeTable.verticalHeader().setMinimumSectionSize(16)
        self.timeTable.verticalHeader().setDefaultSectionSize(18)
        self.stackedWidget.addWidget(self.systemPage)
        self.chairFoldPage = QWidget()
        self.chairFoldPage.setObjectName(u"chairFoldPage")
        self.chairDrivePositionGroup = QGroupBox(self.chairFoldPage)
        self.chairDrivePositionGroup.setObjectName(u"chairDrivePositionGroup")
        self.chairDrivePositionGroup.setGeometry(QRect(564, 16, 238, 197))
        self.chairDrivePositionGroup.setFont(font6)
        self.chairDrivePositionGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.chairDrivePositionTable = QTableWidget(self.chairDrivePositionGroup)
        if (self.chairDrivePositionTable.columnCount() < 2):
            self.chairDrivePositionTable.setColumnCount(2)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.chairDrivePositionTable.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.chairDrivePositionTable.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        self.chairDrivePositionTable.setObjectName(u"chairDrivePositionTable")
        self.chairDrivePositionTable.setGeometry(QRect(17, 50, 203, 129))
        self.chairDrivePositionTable.setFont(font8)
        self.chairDrivePositionTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.chairDrivePositionTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.chairDrivePositionTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairDrivePositionTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairDrivePositionTable.setAutoScroll(False)
        self.chairDrivePositionTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.chairDrivePositionTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.chairDrivePositionTable.horizontalHeader().setVisible(False)
        self.chairDrivePositionTable.horizontalHeader().setMinimumSectionSize(40)
        self.chairDrivePositionTable.horizontalHeader().setDefaultSectionSize(100)
        self.chairDrivePositionTable.horizontalHeader().setStretchLastSection(False)
        self.chairDrivePositionTable.verticalHeader().setVisible(False)
        self.chairDrivePositionTable.verticalHeader().setMinimumSectionSize(16)
        self.chairDrivePositionTable.verticalHeader().setDefaultSectionSize(18)
        self.requestChairPositionButton = QPushButton(self.chairDrivePositionGroup)
        self.requestChairPositionButton.setObjectName(u"requestChairPositionButton")
        self.requestChairPositionButton.setGeometry(QRect(17, 16, 51, 22))
        self.requestChairPositionButton.setStyleSheet(u"QPushButton {\n"
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
        self.chairDriveControlGroup = QGroupBox(self.chairFoldPage)
        self.chairDriveControlGroup.setObjectName(u"chairDriveControlGroup")
        self.chairDriveControlGroup.setGeometry(QRect(16, 16, 532, 521))
        self.chairDriveControlGroup.setFont(font6)
        self.chairDriveControlGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 170px 0px 0px; /* Added left padding to move it left */\n"
"    top: 15px;\n"
"}")
        self.plotChairButton = QPushButton(self.chairDriveControlGroup)
        self.plotChairButton.setObjectName(u"plotChairButton")
        self.plotChairButton.setGeometry(QRect(117, 472, 69, 33))
        self.plotChairButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid #000000; /* Border color */\n"
"    border-radius: 1px; /* Rounded corners */\n"
"}")
        self.chairPIDPosTable = QTableWidget(self.chairDriveControlGroup)
        if (self.chairPIDPosTable.columnCount() < 3):
            self.chairPIDPosTable.setColumnCount(3)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.chairPIDPosTable.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.chairPIDPosTable.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.chairPIDPosTable.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        self.chairPIDPosTable.setObjectName(u"chairPIDPosTable")
        self.chairPIDPosTable.setGeometry(QRect(277, 50, 238, 97))
        self.chairPIDPosTable.setFont(font8)
        self.chairPIDPosTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.chairPIDPosTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.chairPIDPosTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.chairPIDPosTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairPIDPosTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairPIDPosTable.setAutoScroll(False)
        self.chairPIDPosTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.chairPIDPosTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.chairPIDPosTable.horizontalHeader().setMinimumSectionSize(40)
        self.chairPIDPosTable.horizontalHeader().setDefaultSectionSize(79)
        self.chairPIDPosTable.horizontalHeader().setStretchLastSection(False)
        self.chairPIDPosTable.verticalHeader().setVisible(False)
        self.chairPIDPosTable.verticalHeader().setMinimumSectionSize(16)
        self.chairPIDPosTable.verticalHeader().setDefaultSectionSize(18)
        self.chairPIDSpeedTable = QTableWidget(self.chairDriveControlGroup)
        if (self.chairPIDSpeedTable.columnCount() < 3):
            self.chairPIDSpeedTable.setColumnCount(3)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.chairPIDSpeedTable.setHorizontalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.chairPIDSpeedTable.setHorizontalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.chairPIDSpeedTable.setHorizontalHeaderItem(2, __qtablewidgetitem51)
        self.chairPIDSpeedTable.setObjectName(u"chairPIDSpeedTable")
        self.chairPIDSpeedTable.setGeometry(QRect(277, 190, 238, 82))
        self.chairPIDSpeedTable.setFont(font8)
        self.chairPIDSpeedTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.chairPIDSpeedTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.chairPIDSpeedTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.chairPIDSpeedTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairPIDSpeedTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairPIDSpeedTable.setAutoScroll(False)
        self.chairPIDSpeedTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.chairPIDSpeedTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.chairPIDSpeedTable.horizontalHeader().setMinimumSectionSize(40)
        self.chairPIDSpeedTable.horizontalHeader().setDefaultSectionSize(79)
        self.chairPIDSpeedTable.horizontalHeader().setStretchLastSection(False)
        self.chairPIDSpeedTable.verticalHeader().setVisible(False)
        self.chairPIDSpeedTable.verticalHeader().setMinimumSectionSize(16)
        self.chairPIDSpeedTable.verticalHeader().setDefaultSectionSize(18)
        self.enableChairSpeedButton = QRadioButton(self.chairDriveControlGroup)
        self.enableChairSpeedButton.setObjectName(u"enableChairSpeedButton")
        self.enableChairSpeedButton.setGeometry(QRect(330, 160, 144, 22))
        self.enableChairSpeedButton.setFont(font5)
        self.enableChairSpeedButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableChairSpeedButton.setChecked(False)
        self.enableChairSpeedButton.setAutoExclusive(False)
        self.requestChairTuningButton = QPushButton(self.chairDriveControlGroup)
        self.requestChairTuningButton.setObjectName(u"requestChairTuningButton")
        self.requestChairTuningButton.setGeometry(QRect(280, 285, 51, 22))
        self.requestChairTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.copyChairTuningButton = QPushButton(self.chairDriveControlGroup)
        self.copyChairTuningButton.setObjectName(u"copyChairTuningButton")
        self.copyChairTuningButton.setGeometry(QRect(340, 285, 51, 22))
        self.copyChairTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.alterChairTuningButton = QPushButton(self.chairDriveControlGroup)
        self.alterChairTuningButton.setObjectName(u"alterChairTuningButton")
        self.alterChairTuningButton.setGeometry(QRect(460, 285, 51, 22))
        self.alterChairTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.topLine_3 = QFrame(self.chairDriveControlGroup)
        self.topLine_3.setObjectName(u"topLine_3")
        self.topLine_3.setGeometry(QRect(277, 322, 237, 2))
        self.topLine_3.setFont(font4)
        self.topLine_3.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_3.setFrameShape(QFrame.Shape.HLine)
        self.topLine_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.autoChairPlotButton = QRadioButton(self.chairDriveControlGroup)
        self.chairPlotModeButtonGroup = QButtonGroup(MainWindow)
        self.chairPlotModeButtonGroup.setObjectName(u"chairPlotModeButtonGroup")
        self.chairPlotModeButtonGroup.addButton(self.autoChairPlotButton)
        self.autoChairPlotButton.setObjectName(u"autoChairPlotButton")
        self.autoChairPlotButton.setGeometry(QRect(19, 463, 63, 22))
        self.autoChairPlotButton.setFont(font5)
        self.autoChairPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoChairPlotButton.setChecked(False)
        self.autoChairPlotButton.setAutoExclusive(True)
        self.manualChairPlotButton = QRadioButton(self.chairDriveControlGroup)
        self.chairPlotModeButtonGroup.addButton(self.manualChairPlotButton)
        self.manualChairPlotButton.setObjectName(u"manualChairPlotButton")
        self.manualChairPlotButton.setGeometry(QRect(19, 488, 72, 22))
        self.manualChairPlotButton.setFont(font5)
        self.manualChairPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualChairPlotButton.setChecked(True)
        self.manualChairPlotButton.setAutoExclusive(True)
        self.openChairPlotButton = QPushButton(self.chairDriveControlGroup)
        self.openChairPlotButton.setObjectName(u"openChairPlotButton")
        self.openChairPlotButton.setGeometry(QRect(194, 472, 69, 33))
        self.openChairPlotButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
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
        self.chairDriveControlTable = QTableWidget(self.chairDriveControlGroup)
        if (self.chairDriveControlTable.columnCount() < 3):
            self.chairDriveControlTable.setColumnCount(3)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.chairDriveControlTable.setHorizontalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.chairDriveControlTable.setHorizontalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.chairDriveControlTable.setHorizontalHeaderItem(2, __qtablewidgetitem54)
        self.chairDriveControlTable.setObjectName(u"chairDriveControlTable")
        self.chairDriveControlTable.setGeometry(QRect(17, 50, 246, 407))
        self.chairDriveControlTable.setFont(font8)
        self.chairDriveControlTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.chairDriveControlTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.chairDriveControlTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairDriveControlTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairDriveControlTable.setAutoScroll(False)
        self.chairDriveControlTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.chairDriveControlTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.chairDriveControlTable.horizontalHeader().setMinimumSectionSize(40)
        self.chairDriveControlTable.horizontalHeader().setDefaultSectionSize(81)
        self.chairDriveControlTable.horizontalHeader().setStretchLastSection(False)
        self.chairDriveControlTable.verticalHeader().setVisible(False)
        self.chairDriveControlTable.verticalHeader().setMinimumSectionSize(16)
        self.chairDriveControlTable.verticalHeader().setDefaultSectionSize(18)
        self.requestChairLoggingButton = QPushButton(self.chairDriveControlGroup)
        self.requestChairLoggingButton.setObjectName(u"requestChairLoggingButton")
        self.requestChairLoggingButton.setGeometry(QRect(17, 17, 79, 22))
        self.requestChairLoggingButton.setStyleSheet(u"QPushButton {\n"
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
        self.chairFolder = QLineEdit(self.chairDriveControlGroup)
        self.chairFolder.setObjectName(u"chairFolder")
        self.chairFolder.setGeometry(QRect(278, 337, 236, 22))
        self.chairFolder.setFont(font8)
        self.chairFolder.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.chairFolder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chairFolder.setReadOnly(True)
        self.selectChairFolderButton = QPushButton(self.chairDriveControlGroup)
        self.selectChairFolderButton.setObjectName(u"selectChairFolderButton")
        self.selectChairFolderButton.setGeometry(QRect(340, 370, 111, 22))
        self.selectChairFolderButton.setStyleSheet(u"QPushButton {\n"
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
        self.resetChairTuningButton = QPushButton(self.chairDriveControlGroup)
        self.resetChairTuningButton.setObjectName(u"resetChairTuningButton")
        self.resetChairTuningButton.setGeometry(QRect(400, 285, 51, 22))
        self.resetChairTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.chairFoldTuneButton = QRadioButton(self.chairDriveControlGroup)
        self.chairTuneButtonGroup = QButtonGroup(MainWindow)
        self.chairTuneButtonGroup.setObjectName(u"chairTuneButtonGroup")
        self.chairTuneButtonGroup.addButton(self.chairFoldTuneButton)
        self.chairFoldTuneButton.setObjectName(u"chairFoldTuneButton")
        self.chairFoldTuneButton.setGeometry(QRect(300, 20, 50, 22))
        self.chairFoldTuneButton.setFont(font5)
        self.chairFoldTuneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.chairFoldTuneButton.setChecked(True)
        self.chairFoldTuneButton.setAutoExclusive(True)
        self.chairPartFoldTuneButton = QRadioButton(self.chairDriveControlGroup)
        self.chairTuneButtonGroup.addButton(self.chairPartFoldTuneButton)
        self.chairPartFoldTuneButton.setObjectName(u"chairPartFoldTuneButton")
        self.chairPartFoldTuneButton.setGeometry(QRect(356, 20, 73, 22))
        self.chairPartFoldTuneButton.setFont(font5)
        self.chairPartFoldTuneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.chairPartFoldTuneButton.setChecked(False)
        self.chairPartFoldTuneButton.setAutoExclusive(True)
        self.chairUnfoldTuneButton = QRadioButton(self.chairDriveControlGroup)
        self.chairTuneButtonGroup.addButton(self.chairUnfoldTuneButton)
        self.chairUnfoldTuneButton.setObjectName(u"chairUnfoldTuneButton")
        self.chairUnfoldTuneButton.setGeometry(QRect(434, 20, 58, 22))
        self.chairUnfoldTuneButton.setFont(font5)
        self.chairUnfoldTuneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.chairUnfoldTuneButton.setChecked(False)
        self.chairUnfoldTuneButton.setAutoExclusive(True)
        self.chairPlottingLabel = QLabel(self.chairDriveControlGroup)
        self.chairPlottingLabel.setObjectName(u"chairPlottingLabel")
        self.chairPlottingLabel.setGeometry(QRect(316, 486, 78, 16))
        self.chairPlottingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.chairHSLabel = QLabel(self.chairDriveControlGroup)
        self.chairHSLabel.setObjectName(u"chairHSLabel")
        self.chairHSLabel.setGeometry(QRect(297, 434, 97, 17))
        self.chairHSLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.chairLoggingLabel = QLabel(self.chairDriveControlGroup)
        self.chairLoggingLabel.setObjectName(u"chairLoggingLabel")
        self.chairLoggingLabel.setGeometry(QRect(314, 460, 81, 16))
        self.chairLoggingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.chairHSState = QLineEdit(self.chairDriveControlGroup)
        self.chairHSState.setObjectName(u"chairHSState")
        self.chairHSState.setGeometry(QRect(397, 431, 121, 22))
        self.chairHSState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.chairHSState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chairHSState.setReadOnly(True)
        self.chairLoggingState = QLineEdit(self.chairDriveControlGroup)
        self.chairLoggingState.setObjectName(u"chairLoggingState")
        self.chairLoggingState.setGeometry(QRect(397, 457, 121, 22))
        self.chairLoggingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.chairLoggingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chairLoggingState.setReadOnly(True)
        self.chairPlottingState = QLineEdit(self.chairDriveControlGroup)
        self.chairPlottingState.setObjectName(u"chairPlottingState")
        self.chairPlottingState.setGeometry(QRect(397, 483, 121, 22))
        self.chairPlottingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.chairPlottingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chairPlottingState.setReadOnly(True)
        self.plotChairButton.raise_()
        self.chairPIDPosTable.raise_()
        self.chairPIDSpeedTable.raise_()
        self.enableChairSpeedButton.raise_()
        self.requestChairTuningButton.raise_()
        self.copyChairTuningButton.raise_()
        self.alterChairTuningButton.raise_()
        self.topLine_3.raise_()
        self.autoChairPlotButton.raise_()
        self.manualChairPlotButton.raise_()
        self.openChairPlotButton.raise_()
        self.chairDriveControlTable.raise_()
        self.requestChairLoggingButton.raise_()
        self.resetChairTuningButton.raise_()
        self.chairFoldTuneButton.raise_()
        self.chairPartFoldTuneButton.raise_()
        self.chairUnfoldTuneButton.raise_()
        self.selectChairFolderButton.raise_()
        self.chairFolder.raise_()
        self.chairPlottingLabel.raise_()
        self.chairHSLabel.raise_()
        self.chairLoggingLabel.raise_()
        self.chairHSState.raise_()
        self.chairLoggingState.raise_()
        self.chairPlottingState.raise_()
        self.chairHBridgeGroup = QGroupBox(self.chairFoldPage)
        self.chairHBridgeGroup.setObjectName(u"chairHBridgeGroup")
        self.chairHBridgeGroup.setGeometry(QRect(564, 390, 238, 233))
        self.chairHBridgeGroup.setFont(font6)
        self.chairHBridgeGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.chairLeftBridgeDuty = QSlider(self.chairHBridgeGroup)
        self.chairLeftBridgeDuty.setObjectName(u"chairLeftBridgeDuty")
        self.chairLeftBridgeDuty.setGeometry(QRect(30, 46, 22, 170))
        self.chairLeftBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.chairLeftBridgeDuty.setMaximum(980)
        self.chairLeftBridgeDuty.setPageStep(100)
        self.chairLeftBridgeDuty.setValue(0)
        self.chairLeftBridgeDuty.setSliderPosition(0)
        self.chairLeftBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.chairLeftBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.chairRightBridgeDuty = QSlider(self.chairHBridgeGroup)
        self.chairRightBridgeDuty.setObjectName(u"chairRightBridgeDuty")
        self.chairRightBridgeDuty.setGeometry(QRect(186, 46, 22, 170))
        self.chairRightBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.chairRightBridgeDuty.setMaximum(980)
        self.chairRightBridgeDuty.setPageStep(100)
        self.chairRightBridgeDuty.setValue(0)
        self.chairRightBridgeDuty.setSliderPosition(0)
        self.chairRightBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.chairRightBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.chairLeftBridgeText = QLineEdit(self.chairHBridgeGroup)
        self.chairLeftBridgeText.setObjectName(u"chairLeftBridgeText")
        self.chairLeftBridgeText.setGeometry(QRect(61, 117, 44, 22))
        font13 = QFont()
        font13.setBold(False)
        self.chairLeftBridgeText.setFont(font13)
        self.chairLeftBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.chairRightBridgeText = QLineEdit(self.chairHBridgeGroup)
        self.chairRightBridgeText.setObjectName(u"chairRightBridgeText")
        self.chairRightBridgeText.setGeometry(QRect(130, 117, 43, 22))
        self.chairRightBridgeText.setFont(font13)
        self.chairRightBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.chairRightBridgeText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.chairHoldRightDutyButton = QRadioButton(self.chairHBridgeGroup)
        self.chairHoldRightDutyButton.setObjectName(u"chairHoldRightDutyButton")
        self.chairHoldRightDutyButton.setGeometry(QRect(174, 17, 51, 22))
        self.chairHoldRightDutyButton.setFont(font5)
        self.chairHoldRightDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.chairHoldRightDutyButton.setChecked(False)
        self.chairHoldRightDutyButton.setAutoExclusive(False)
        self.chairHoldLeftDutyButton = QRadioButton(self.chairHBridgeGroup)
        self.chairHoldLeftDutyButton.setObjectName(u"chairHoldLeftDutyButton")
        self.chairHoldLeftDutyButton.setGeometry(QRect(18, 17, 51, 22))
        self.chairHoldLeftDutyButton.setFont(font5)
        self.chairHoldLeftDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.chairHoldLeftDutyButton.setChecked(False)
        self.chairHoldLeftDutyButton.setAutoExclusive(False)
        self.maxChairPWMLabel = QLabel(self.chairHBridgeGroup)
        self.maxChairPWMLabel.setObjectName(u"maxChairPWMLabel")
        self.maxChairPWMLabel.setGeometry(QRect(107, 52, 26, 16))
        self.maxChairPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.maxChairPWM = QLineEdit(self.chairHBridgeGroup)
        self.maxChairPWM.setObjectName(u"maxChairPWM")
        self.maxChairPWM.setGeometry(QRect(93, 70, 52, 22))
        self.maxChairPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.maxChairPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.maxChairPWM.setReadOnly(False)
        self.minChairPWM = QLineEdit(self.chairHBridgeGroup)
        self.minChairPWM.setObjectName(u"minChairPWM")
        self.minChairPWM.setGeometry(QRect(93, 170, 52, 22))
        self.minChairPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.minChairPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minChairPWM.setReadOnly(False)
        self.minChairPWMLabel = QLabel(self.chairHBridgeGroup)
        self.minChairPWMLabel.setObjectName(u"minChairPWMLabel")
        self.minChairPWMLabel.setGeometry(QRect(107, 151, 26, 16))
        self.minChairPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.enableChairBridgeButton = QRadioButton(self.chairHBridgeGroup)
        self.enableChairBridgeButton.setObjectName(u"enableChairBridgeButton")
        self.enableChairBridgeButton.setGeometry(QRect(90, 205, 60, 22))
        self.enableChairBridgeButton.setFont(font5)
        self.enableChairBridgeButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableChairBridgeButton.setChecked(False)
        self.enableChairBridgeButton.setAutoExclusive(False)
        self.chairStateMachineGroup = QGroupBox(self.chairFoldPage)
        self.chairStateMachineGroup.setObjectName(u"chairStateMachineGroup")
        self.chairStateMachineGroup.setGeometry(QRect(564, 230, 238, 144))
        self.chairStateMachineGroup.setFont(font6)
        self.chairStateMachineGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 0px 0px 0px;\n"
"	top: 15px;\n"
"}")
        self.chairStateMachineTable = QTableWidget(self.chairStateMachineGroup)
        if (self.chairStateMachineTable.columnCount() < 2):
            self.chairStateMachineTable.setColumnCount(2)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.chairStateMachineTable.setHorizontalHeaderItem(0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.chairStateMachineTable.setHorizontalHeaderItem(1, __qtablewidgetitem56)
        self.chairStateMachineTable.setObjectName(u"chairStateMachineTable")
        self.chairStateMachineTable.setGeometry(QRect(17, 50, 203, 75))
        self.chairStateMachineTable.setFont(font8)
        self.chairStateMachineTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.chairStateMachineTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.chairStateMachineTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairStateMachineTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.chairStateMachineTable.setAutoScroll(False)
        self.chairStateMachineTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.chairStateMachineTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.chairStateMachineTable.horizontalHeader().setVisible(False)
        self.chairStateMachineTable.horizontalHeader().setMinimumSectionSize(40)
        self.chairStateMachineTable.horizontalHeader().setDefaultSectionSize(100)
        self.chairStateMachineTable.horizontalHeader().setStretchLastSection(False)
        self.chairStateMachineTable.verticalHeader().setVisible(False)
        self.chairStateMachineTable.verticalHeader().setMinimumSectionSize(16)
        self.chairStateMachineTable.verticalHeader().setDefaultSectionSize(18)
        self.chairCalibrationGroup = QGroupBox(self.chairFoldPage)
        self.chairCalibrationGroup.setObjectName(u"chairCalibrationGroup")
        self.chairCalibrationGroup.setGeometry(QRect(16, 552, 191, 123))
        self.chairCalibrationGroup.setFont(font6)
        self.chairCalibrationGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.autoChairCalButton = QRadioButton(self.chairCalibrationGroup)
        self.autoChairCalButton.setObjectName(u"autoChairCalButton")
        self.autoChairCalButton.setGeometry(QRect(29, 90, 63, 22))
        self.autoChairCalButton.setFont(font5)
        self.autoChairCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoChairCalButton.setChecked(False)
        self.autoChairCalButton.setAutoExclusive(True)
        self.manualChairCalButton = QRadioButton(self.chairCalibrationGroup)
        self.manualChairCalButton.setObjectName(u"manualChairCalButton")
        self.manualChairCalButton.setGeometry(QRect(99, 90, 72, 22))
        self.manualChairCalButton.setFont(font5)
        self.manualChairCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualChairCalButton.setChecked(True)
        self.manualChairCalButton.setAutoExclusive(True)
        self.startChairCalButton = QPushButton(self.chairCalibrationGroup)
        self.startChairCalButton.setObjectName(u"startChairCalButton")
        self.startChairCalButton.setGeometry(QRect(10, 50, 49, 27))
        self.startChairCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.acceptChairCalButton = QPushButton(self.chairCalibrationGroup)
        self.acceptChairCalButton.setObjectName(u"acceptChairCalButton")
        self.acceptChairCalButton.setGeometry(QRect(70, 50, 49, 27))
        self.acceptChairCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.rejectChairCalButton = QPushButton(self.chairCalibrationGroup)
        self.rejectChairCalButton.setObjectName(u"rejectChairCalButton")
        self.rejectChairCalButton.setGeometry(QRect(130, 50, 49, 27))
        self.rejectChairCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.chairFoldPage)
        self.footrestPage = QWidget()
        self.footrestPage.setObjectName(u"footrestPage")
        self.footrestDriveControlGroup = QGroupBox(self.footrestPage)
        self.footrestDriveControlGroup.setObjectName(u"footrestDriveControlGroup")
        self.footrestDriveControlGroup.setGeometry(QRect(16, 16, 532, 521))
        self.footrestDriveControlGroup.setFont(font6)
        self.footrestDriveControlGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 170px 0px 0px; /* Added left padding to move it left */\n"
"    top: 15px;\n"
"}")
        self.footrestDriveControlTable = QTableWidget(self.footrestDriveControlGroup)
        if (self.footrestDriveControlTable.columnCount() < 3):
            self.footrestDriveControlTable.setColumnCount(3)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.footrestDriveControlTable.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.footrestDriveControlTable.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.footrestDriveControlTable.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        self.footrestDriveControlTable.setObjectName(u"footrestDriveControlTable")
        self.footrestDriveControlTable.setGeometry(QRect(17, 50, 246, 407))
        self.footrestDriveControlTable.setFont(font8)
        self.footrestDriveControlTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.footrestDriveControlTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.footrestDriveControlTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestDriveControlTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestDriveControlTable.setAutoScroll(False)
        self.footrestDriveControlTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.footrestDriveControlTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.footrestDriveControlTable.horizontalHeader().setMinimumSectionSize(40)
        self.footrestDriveControlTable.horizontalHeader().setDefaultSectionSize(81)
        self.footrestDriveControlTable.horizontalHeader().setStretchLastSection(False)
        self.footrestDriveControlTable.verticalHeader().setVisible(False)
        self.footrestDriveControlTable.verticalHeader().setMinimumSectionSize(16)
        self.footrestDriveControlTable.verticalHeader().setDefaultSectionSize(18)
        self.plotFootrestButton = QPushButton(self.footrestDriveControlGroup)
        self.plotFootrestButton.setObjectName(u"plotFootrestButton")
        self.plotFootrestButton.setGeometry(QRect(117, 472, 69, 33))
        self.plotFootrestButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.footrestPIDPosTable = QTableWidget(self.footrestDriveControlGroup)
        if (self.footrestPIDPosTable.columnCount() < 3):
            self.footrestPIDPosTable.setColumnCount(3)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.footrestPIDPosTable.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.footrestPIDPosTable.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.footrestPIDPosTable.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        self.footrestPIDPosTable.setObjectName(u"footrestPIDPosTable")
        self.footrestPIDPosTable.setGeometry(QRect(277, 50, 238, 97))
        self.footrestPIDPosTable.setFont(font8)
        self.footrestPIDPosTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.footrestPIDPosTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.footrestPIDPosTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.footrestPIDPosTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestPIDPosTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestPIDPosTable.setAutoScroll(False)
        self.footrestPIDPosTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.footrestPIDPosTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.footrestPIDPosTable.horizontalHeader().setMinimumSectionSize(40)
        self.footrestPIDPosTable.horizontalHeader().setDefaultSectionSize(79)
        self.footrestPIDPosTable.horizontalHeader().setStretchLastSection(False)
        self.footrestPIDPosTable.verticalHeader().setVisible(False)
        self.footrestPIDPosTable.verticalHeader().setMinimumSectionSize(16)
        self.footrestPIDPosTable.verticalHeader().setDefaultSectionSize(18)
        self.footrestPIDSpeedTable = QTableWidget(self.footrestDriveControlGroup)
        if (self.footrestPIDSpeedTable.columnCount() < 3):
            self.footrestPIDSpeedTable.setColumnCount(3)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.footrestPIDSpeedTable.setHorizontalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.footrestPIDSpeedTable.setHorizontalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.footrestPIDSpeedTable.setHorizontalHeaderItem(2, __qtablewidgetitem65)
        self.footrestPIDSpeedTable.setObjectName(u"footrestPIDSpeedTable")
        self.footrestPIDSpeedTable.setGeometry(QRect(277, 190, 238, 82))
        self.footrestPIDSpeedTable.setFont(font8)
        self.footrestPIDSpeedTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.footrestPIDSpeedTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.footrestPIDSpeedTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.footrestPIDSpeedTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestPIDSpeedTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestPIDSpeedTable.setAutoScroll(False)
        self.footrestPIDSpeedTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.footrestPIDSpeedTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.footrestPIDSpeedTable.horizontalHeader().setMinimumSectionSize(40)
        self.footrestPIDSpeedTable.horizontalHeader().setDefaultSectionSize(79)
        self.footrestPIDSpeedTable.horizontalHeader().setStretchLastSection(False)
        self.footrestPIDSpeedTable.verticalHeader().setVisible(False)
        self.footrestPIDSpeedTable.verticalHeader().setMinimumSectionSize(16)
        self.footrestPIDSpeedTable.verticalHeader().setDefaultSectionSize(18)
        self.enableFootrestSpeedButton = QRadioButton(self.footrestDriveControlGroup)
        self.enableFootrestSpeedButton.setObjectName(u"enableFootrestSpeedButton")
        self.enableFootrestSpeedButton.setGeometry(QRect(330, 160, 144, 22))
        self.enableFootrestSpeedButton.setFont(font5)
        self.enableFootrestSpeedButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableFootrestSpeedButton.setChecked(False)
        self.enableFootrestSpeedButton.setAutoExclusive(False)
        self.requestFootrestTuningButton = QPushButton(self.footrestDriveControlGroup)
        self.requestFootrestTuningButton.setObjectName(u"requestFootrestTuningButton")
        self.requestFootrestTuningButton.setGeometry(QRect(280, 285, 51, 22))
        self.requestFootrestTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.copyFootrestTuningButton = QPushButton(self.footrestDriveControlGroup)
        self.copyFootrestTuningButton.setObjectName(u"copyFootrestTuningButton")
        self.copyFootrestTuningButton.setGeometry(QRect(340, 285, 51, 22))
        self.copyFootrestTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.alterFootrestTuningButton = QPushButton(self.footrestDriveControlGroup)
        self.alterFootrestTuningButton.setObjectName(u"alterFootrestTuningButton")
        self.alterFootrestTuningButton.setGeometry(QRect(460, 285, 51, 22))
        self.alterFootrestTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.topLine_4 = QFrame(self.footrestDriveControlGroup)
        self.topLine_4.setObjectName(u"topLine_4")
        self.topLine_4.setGeometry(QRect(277, 322, 237, 2))
        self.topLine_4.setFont(font4)
        self.topLine_4.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_4.setFrameShape(QFrame.Shape.HLine)
        self.topLine_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.autoFootrestPlotButton = QRadioButton(self.footrestDriveControlGroup)
        self.footrestPlotModeButtonGroup = QButtonGroup(MainWindow)
        self.footrestPlotModeButtonGroup.setObjectName(u"footrestPlotModeButtonGroup")
        self.footrestPlotModeButtonGroup.addButton(self.autoFootrestPlotButton)
        self.autoFootrestPlotButton.setObjectName(u"autoFootrestPlotButton")
        self.autoFootrestPlotButton.setGeometry(QRect(19, 463, 63, 22))
        self.autoFootrestPlotButton.setFont(font5)
        self.autoFootrestPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoFootrestPlotButton.setChecked(False)
        self.autoFootrestPlotButton.setAutoExclusive(True)
        self.manualFootrestPlotButton = QRadioButton(self.footrestDriveControlGroup)
        self.footrestPlotModeButtonGroup.addButton(self.manualFootrestPlotButton)
        self.manualFootrestPlotButton.setObjectName(u"manualFootrestPlotButton")
        self.manualFootrestPlotButton.setGeometry(QRect(19, 488, 72, 22))
        self.manualFootrestPlotButton.setFont(font5)
        self.manualFootrestPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualFootrestPlotButton.setChecked(True)
        self.manualFootrestPlotButton.setAutoExclusive(True)
        self.openFootrestPlotButton = QPushButton(self.footrestDriveControlGroup)
        self.openFootrestPlotButton.setObjectName(u"openFootrestPlotButton")
        self.openFootrestPlotButton.setGeometry(QRect(194, 472, 69, 33))
        self.openFootrestPlotButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
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
        self.requestFootrestLoggingButton = QPushButton(self.footrestDriveControlGroup)
        self.requestFootrestLoggingButton.setObjectName(u"requestFootrestLoggingButton")
        self.requestFootrestLoggingButton.setGeometry(QRect(17, 17, 79, 22))
        self.requestFootrestLoggingButton.setStyleSheet(u"QPushButton {\n"
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
        self.footrestFolder = QLineEdit(self.footrestDriveControlGroup)
        self.footrestFolder.setObjectName(u"footrestFolder")
        self.footrestFolder.setGeometry(QRect(278, 337, 236, 22))
        self.footrestFolder.setFont(font8)
        self.footrestFolder.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.footrestFolder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footrestFolder.setReadOnly(True)
        self.selectFootrestFolderButton = QPushButton(self.footrestDriveControlGroup)
        self.selectFootrestFolderButton.setObjectName(u"selectFootrestFolderButton")
        self.selectFootrestFolderButton.setGeometry(QRect(340, 370, 111, 22))
        self.selectFootrestFolderButton.setStyleSheet(u"QPushButton {\n"
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
        self.resetFootrestTuningButton = QPushButton(self.footrestDriveControlGroup)
        self.resetFootrestTuningButton.setObjectName(u"resetFootrestTuningButton")
        self.resetFootrestTuningButton.setGeometry(QRect(400, 285, 51, 22))
        self.resetFootrestTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.footrestFoldTuneButton = QRadioButton(self.footrestDriveControlGroup)
        self.footrestTuneButtonGroup = QButtonGroup(MainWindow)
        self.footrestTuneButtonGroup.setObjectName(u"footrestTuneButtonGroup")
        self.footrestTuneButtonGroup.addButton(self.footrestFoldTuneButton)
        self.footrestFoldTuneButton.setObjectName(u"footrestFoldTuneButton")
        self.footrestFoldTuneButton.setGeometry(QRect(300, 20, 50, 22))
        self.footrestFoldTuneButton.setFont(font5)
        self.footrestFoldTuneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.footrestFoldTuneButton.setChecked(True)
        self.footrestFoldTuneButton.setAutoExclusive(True)
        self.footrestUnfoldTuneButton = QRadioButton(self.footrestDriveControlGroup)
        self.footrestTuneButtonGroup.addButton(self.footrestUnfoldTuneButton)
        self.footrestUnfoldTuneButton.setObjectName(u"footrestUnfoldTuneButton")
        self.footrestUnfoldTuneButton.setGeometry(QRect(434, 20, 58, 22))
        self.footrestUnfoldTuneButton.setFont(font5)
        self.footrestUnfoldTuneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.footrestUnfoldTuneButton.setChecked(False)
        self.footrestUnfoldTuneButton.setAutoExclusive(True)
        self.footrestPlottingLabel = QLabel(self.footrestDriveControlGroup)
        self.footrestPlottingLabel.setObjectName(u"footrestPlottingLabel")
        self.footrestPlottingLabel.setGeometry(QRect(316, 486, 78, 16))
        self.footrestPlottingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.footrestHSLabel = QLabel(self.footrestDriveControlGroup)
        self.footrestHSLabel.setObjectName(u"footrestHSLabel")
        self.footrestHSLabel.setGeometry(QRect(297, 434, 97, 17))
        self.footrestHSLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.footrestLoggingLabel = QLabel(self.footrestDriveControlGroup)
        self.footrestLoggingLabel.setObjectName(u"footrestLoggingLabel")
        self.footrestLoggingLabel.setGeometry(QRect(314, 460, 81, 16))
        self.footrestLoggingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.footrestHSState = QLineEdit(self.footrestDriveControlGroup)
        self.footrestHSState.setObjectName(u"footrestHSState")
        self.footrestHSState.setGeometry(QRect(397, 431, 121, 22))
        self.footrestHSState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.footrestHSState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footrestHSState.setReadOnly(True)
        self.footrestLoggingState = QLineEdit(self.footrestDriveControlGroup)
        self.footrestLoggingState.setObjectName(u"footrestLoggingState")
        self.footrestLoggingState.setGeometry(QRect(397, 457, 121, 22))
        self.footrestLoggingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.footrestLoggingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footrestLoggingState.setReadOnly(True)
        self.footrestPlottingState = QLineEdit(self.footrestDriveControlGroup)
        self.footrestPlottingState.setObjectName(u"footrestPlottingState")
        self.footrestPlottingState.setGeometry(QRect(397, 483, 121, 22))
        self.footrestPlottingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.footrestPlottingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footrestPlottingState.setReadOnly(True)
        self.footrestDrivePositionGroup = QGroupBox(self.footrestPage)
        self.footrestDrivePositionGroup.setObjectName(u"footrestDrivePositionGroup")
        self.footrestDrivePositionGroup.setGeometry(QRect(564, 16, 238, 180))
        self.footrestDrivePositionGroup.setFont(font6)
        self.footrestDrivePositionGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.footrestDrivePositionTable = QTableWidget(self.footrestDrivePositionGroup)
        if (self.footrestDrivePositionTable.columnCount() < 2):
            self.footrestDrivePositionTable.setColumnCount(2)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.footrestDrivePositionTable.setHorizontalHeaderItem(0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.footrestDrivePositionTable.setHorizontalHeaderItem(1, __qtablewidgetitem67)
        self.footrestDrivePositionTable.setObjectName(u"footrestDrivePositionTable")
        self.footrestDrivePositionTable.setGeometry(QRect(17, 50, 203, 111))
        self.footrestDrivePositionTable.setFont(font8)
        self.footrestDrivePositionTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.footrestDrivePositionTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.footrestDrivePositionTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestDrivePositionTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestDrivePositionTable.setAutoScroll(False)
        self.footrestDrivePositionTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.footrestDrivePositionTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.footrestDrivePositionTable.horizontalHeader().setVisible(False)
        self.footrestDrivePositionTable.horizontalHeader().setMinimumSectionSize(40)
        self.footrestDrivePositionTable.horizontalHeader().setDefaultSectionSize(100)
        self.footrestDrivePositionTable.horizontalHeader().setStretchLastSection(False)
        self.footrestDrivePositionTable.verticalHeader().setVisible(False)
        self.footrestDrivePositionTable.verticalHeader().setMinimumSectionSize(16)
        self.footrestDrivePositionTable.verticalHeader().setDefaultSectionSize(18)
        self.requestFootrestPositionButton = QPushButton(self.footrestDrivePositionGroup)
        self.requestFootrestPositionButton.setObjectName(u"requestFootrestPositionButton")
        self.requestFootrestPositionButton.setGeometry(QRect(17, 16, 51, 22))
        self.requestFootrestPositionButton.setStyleSheet(u"QPushButton {\n"
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
        self.footrestHBridgeGroup = QGroupBox(self.footrestPage)
        self.footrestHBridgeGroup.setObjectName(u"footrestHBridgeGroup")
        self.footrestHBridgeGroup.setGeometry(QRect(564, 372, 238, 233))
        self.footrestHBridgeGroup.setFont(font6)
        self.footrestHBridgeGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.footrestLeftBridgeDuty = QSlider(self.footrestHBridgeGroup)
        self.footrestLeftBridgeDuty.setObjectName(u"footrestLeftBridgeDuty")
        self.footrestLeftBridgeDuty.setGeometry(QRect(30, 46, 22, 170))
        self.footrestLeftBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.footrestLeftBridgeDuty.setMaximum(980)
        self.footrestLeftBridgeDuty.setPageStep(100)
        self.footrestLeftBridgeDuty.setValue(0)
        self.footrestLeftBridgeDuty.setSliderPosition(0)
        self.footrestLeftBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.footrestLeftBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.footrestRightBridgeDuty = QSlider(self.footrestHBridgeGroup)
        self.footrestRightBridgeDuty.setObjectName(u"footrestRightBridgeDuty")
        self.footrestRightBridgeDuty.setGeometry(QRect(186, 46, 22, 170))
        self.footrestRightBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.footrestRightBridgeDuty.setMaximum(980)
        self.footrestRightBridgeDuty.setPageStep(100)
        self.footrestRightBridgeDuty.setValue(0)
        self.footrestRightBridgeDuty.setSliderPosition(0)
        self.footrestRightBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.footrestRightBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.footrestLeftBridgeText = QLineEdit(self.footrestHBridgeGroup)
        self.footrestLeftBridgeText.setObjectName(u"footrestLeftBridgeText")
        self.footrestLeftBridgeText.setGeometry(QRect(61, 117, 44, 22))
        self.footrestLeftBridgeText.setFont(font13)
        self.footrestLeftBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.footrestRightBridgeText = QLineEdit(self.footrestHBridgeGroup)
        self.footrestRightBridgeText.setObjectName(u"footrestRightBridgeText")
        self.footrestRightBridgeText.setGeometry(QRect(130, 117, 43, 22))
        self.footrestRightBridgeText.setFont(font13)
        self.footrestRightBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.footrestRightBridgeText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.footrestHoldRightDutyButton = QRadioButton(self.footrestHBridgeGroup)
        self.footrestHoldRightDutyButton.setObjectName(u"footrestHoldRightDutyButton")
        self.footrestHoldRightDutyButton.setGeometry(QRect(174, 17, 51, 22))
        self.footrestHoldRightDutyButton.setFont(font5)
        self.footrestHoldRightDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.footrestHoldRightDutyButton.setChecked(False)
        self.footrestHoldRightDutyButton.setAutoExclusive(False)
        self.footrestHoldLeftDutyButton = QRadioButton(self.footrestHBridgeGroup)
        self.footrestHoldLeftDutyButton.setObjectName(u"footrestHoldLeftDutyButton")
        self.footrestHoldLeftDutyButton.setGeometry(QRect(18, 17, 51, 22))
        self.footrestHoldLeftDutyButton.setFont(font5)
        self.footrestHoldLeftDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.footrestHoldLeftDutyButton.setChecked(False)
        self.footrestHoldLeftDutyButton.setAutoExclusive(False)
        self.maxFootrestPWMLabel = QLabel(self.footrestHBridgeGroup)
        self.maxFootrestPWMLabel.setObjectName(u"maxFootrestPWMLabel")
        self.maxFootrestPWMLabel.setGeometry(QRect(107, 52, 26, 16))
        self.maxFootrestPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.maxFootrestPWM = QLineEdit(self.footrestHBridgeGroup)
        self.maxFootrestPWM.setObjectName(u"maxFootrestPWM")
        self.maxFootrestPWM.setGeometry(QRect(93, 70, 52, 22))
        self.maxFootrestPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.maxFootrestPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.maxFootrestPWM.setReadOnly(False)
        self.minFootrestPWM = QLineEdit(self.footrestHBridgeGroup)
        self.minFootrestPWM.setObjectName(u"minFootrestPWM")
        self.minFootrestPWM.setGeometry(QRect(93, 170, 52, 22))
        self.minFootrestPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.minFootrestPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minFootrestPWM.setReadOnly(False)
        self.minFootrestPWMLabel = QLabel(self.footrestHBridgeGroup)
        self.minFootrestPWMLabel.setObjectName(u"minFootrestPWMLabel")
        self.minFootrestPWMLabel.setGeometry(QRect(107, 151, 26, 16))
        self.minFootrestPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.enableFootrestBridgeButton = QRadioButton(self.footrestHBridgeGroup)
        self.enableFootrestBridgeButton.setObjectName(u"enableFootrestBridgeButton")
        self.enableFootrestBridgeButton.setGeometry(QRect(90, 205, 60, 22))
        self.enableFootrestBridgeButton.setFont(font5)
        self.enableFootrestBridgeButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableFootrestBridgeButton.setChecked(False)
        self.enableFootrestBridgeButton.setAutoExclusive(False)
        self.footrestStateMachineGroup = QGroupBox(self.footrestPage)
        self.footrestStateMachineGroup.setObjectName(u"footrestStateMachineGroup")
        self.footrestStateMachineGroup.setGeometry(QRect(564, 212, 238, 140))
        self.footrestStateMachineGroup.setFont(font6)
        self.footrestStateMachineGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 0px 0px 0px;\n"
"	top: 15px;\n"
"}")
        self.footrestStateMachineTable = QTableWidget(self.footrestStateMachineGroup)
        if (self.footrestStateMachineTable.columnCount() < 2):
            self.footrestStateMachineTable.setColumnCount(2)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.footrestStateMachineTable.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.footrestStateMachineTable.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        self.footrestStateMachineTable.setObjectName(u"footrestStateMachineTable")
        self.footrestStateMachineTable.setGeometry(QRect(17, 50, 203, 74))
        self.footrestStateMachineTable.setFont(font8)
        self.footrestStateMachineTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.footrestStateMachineTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.footrestStateMachineTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestStateMachineTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.footrestStateMachineTable.setAutoScroll(False)
        self.footrestStateMachineTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.footrestStateMachineTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.footrestStateMachineTable.horizontalHeader().setVisible(False)
        self.footrestStateMachineTable.horizontalHeader().setMinimumSectionSize(40)
        self.footrestStateMachineTable.horizontalHeader().setDefaultSectionSize(100)
        self.footrestStateMachineTable.horizontalHeader().setStretchLastSection(False)
        self.footrestStateMachineTable.verticalHeader().setVisible(False)
        self.footrestStateMachineTable.verticalHeader().setMinimumSectionSize(16)
        self.footrestStateMachineTable.verticalHeader().setDefaultSectionSize(18)
        self.footrestCalibrationGroup = QGroupBox(self.footrestPage)
        self.footrestCalibrationGroup.setObjectName(u"footrestCalibrationGroup")
        self.footrestCalibrationGroup.setGeometry(QRect(16, 552, 191, 123))
        self.footrestCalibrationGroup.setFont(font6)
        self.footrestCalibrationGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.autoFootrestCalButton = QRadioButton(self.footrestCalibrationGroup)
        self.autoFootrestCalButton.setObjectName(u"autoFootrestCalButton")
        self.autoFootrestCalButton.setGeometry(QRect(29, 90, 63, 22))
        self.autoFootrestCalButton.setFont(font5)
        self.autoFootrestCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoFootrestCalButton.setChecked(False)
        self.autoFootrestCalButton.setAutoExclusive(True)
        self.manualFootrestCalButton = QRadioButton(self.footrestCalibrationGroup)
        self.manualFootrestCalButton.setObjectName(u"manualFootrestCalButton")
        self.manualFootrestCalButton.setGeometry(QRect(99, 90, 72, 22))
        self.manualFootrestCalButton.setFont(font5)
        self.manualFootrestCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualFootrestCalButton.setChecked(True)
        self.manualFootrestCalButton.setAutoExclusive(True)
        self.startFootrestCalButton = QPushButton(self.footrestCalibrationGroup)
        self.startFootrestCalButton.setObjectName(u"startFootrestCalButton")
        self.startFootrestCalButton.setGeometry(QRect(10, 50, 49, 27))
        self.startFootrestCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.acceptFootrestCalButton = QPushButton(self.footrestCalibrationGroup)
        self.acceptFootrestCalButton.setObjectName(u"acceptFootrestCalButton")
        self.acceptFootrestCalButton.setGeometry(QRect(70, 50, 49, 27))
        self.acceptFootrestCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.rejectFootrestCalButton = QPushButton(self.footrestCalibrationGroup)
        self.rejectFootrestCalButton.setObjectName(u"rejectFootrestCalButton")
        self.rejectFootrestCalButton.setGeometry(QRect(130, 50, 49, 27))
        self.rejectFootrestCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.footrestPage)
        self.mainDrivePage = QWidget()
        self.mainDrivePage.setObjectName(u"mainDrivePage")
        self.mainStateMachineGroup = QGroupBox(self.mainDrivePage)
        self.mainStateMachineGroup.setObjectName(u"mainStateMachineGroup")
        self.mainStateMachineGroup.setGeometry(QRect(564, 142, 238, 142))
        self.mainStateMachineGroup.setFont(font6)
        self.mainStateMachineGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 0px 0px 0px;\n"
"	top: 15px;\n"
"}")
        self.mainStateMachineTable = QTableWidget(self.mainStateMachineGroup)
        if (self.mainStateMachineTable.columnCount() < 2):
            self.mainStateMachineTable.setColumnCount(2)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.mainStateMachineTable.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.mainStateMachineTable.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        self.mainStateMachineTable.setObjectName(u"mainStateMachineTable")
        self.mainStateMachineTable.setGeometry(QRect(17, 50, 203, 74))
        self.mainStateMachineTable.setFont(font8)
        self.mainStateMachineTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mainStateMachineTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.mainStateMachineTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainStateMachineTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainStateMachineTable.setAutoScroll(False)
        self.mainStateMachineTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.mainStateMachineTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.mainStateMachineTable.horizontalHeader().setVisible(False)
        self.mainStateMachineTable.horizontalHeader().setMinimumSectionSize(40)
        self.mainStateMachineTable.horizontalHeader().setDefaultSectionSize(100)
        self.mainStateMachineTable.horizontalHeader().setStretchLastSection(False)
        self.mainStateMachineTable.verticalHeader().setVisible(False)
        self.mainStateMachineTable.verticalHeader().setMinimumSectionSize(16)
        self.mainStateMachineTable.verticalHeader().setDefaultSectionSize(18)
        self.mainHBridgeGroup = QGroupBox(self.mainDrivePage)
        self.mainHBridgeGroup.setObjectName(u"mainHBridgeGroup")
        self.mainHBridgeGroup.setGeometry(QRect(564, 303, 238, 233))
        self.mainHBridgeGroup.setFont(font6)
        self.mainHBridgeGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.mainLeftBridgeDuty = QSlider(self.mainHBridgeGroup)
        self.mainLeftBridgeDuty.setObjectName(u"mainLeftBridgeDuty")
        self.mainLeftBridgeDuty.setGeometry(QRect(30, 46, 22, 170))
        self.mainLeftBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.mainLeftBridgeDuty.setMaximum(980)
        self.mainLeftBridgeDuty.setPageStep(100)
        self.mainLeftBridgeDuty.setValue(0)
        self.mainLeftBridgeDuty.setSliderPosition(0)
        self.mainLeftBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.mainLeftBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.mainRightBridgeDuty = QSlider(self.mainHBridgeGroup)
        self.mainRightBridgeDuty.setObjectName(u"mainRightBridgeDuty")
        self.mainRightBridgeDuty.setGeometry(QRect(186, 46, 22, 170))
        self.mainRightBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.mainRightBridgeDuty.setMaximum(980)
        self.mainRightBridgeDuty.setPageStep(100)
        self.mainRightBridgeDuty.setValue(0)
        self.mainRightBridgeDuty.setSliderPosition(0)
        self.mainRightBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.mainRightBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.mainLeftBridgeText = QLineEdit(self.mainHBridgeGroup)
        self.mainLeftBridgeText.setObjectName(u"mainLeftBridgeText")
        self.mainLeftBridgeText.setGeometry(QRect(61, 117, 44, 22))
        self.mainLeftBridgeText.setFont(font13)
        self.mainLeftBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.mainRightBridgeText = QLineEdit(self.mainHBridgeGroup)
        self.mainRightBridgeText.setObjectName(u"mainRightBridgeText")
        self.mainRightBridgeText.setGeometry(QRect(130, 117, 43, 22))
        self.mainRightBridgeText.setFont(font13)
        self.mainRightBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.mainRightBridgeText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.mainHoldRightDutyButton = QRadioButton(self.mainHBridgeGroup)
        self.mainHoldRightDutyButton.setObjectName(u"mainHoldRightDutyButton")
        self.mainHoldRightDutyButton.setGeometry(QRect(174, 17, 51, 22))
        self.mainHoldRightDutyButton.setFont(font5)
        self.mainHoldRightDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.mainHoldRightDutyButton.setChecked(False)
        self.mainHoldRightDutyButton.setAutoExclusive(False)
        self.mainHoldLeftDutyButton = QRadioButton(self.mainHBridgeGroup)
        self.mainHoldLeftDutyButton.setObjectName(u"mainHoldLeftDutyButton")
        self.mainHoldLeftDutyButton.setGeometry(QRect(18, 17, 51, 22))
        self.mainHoldLeftDutyButton.setFont(font5)
        self.mainHoldLeftDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.mainHoldLeftDutyButton.setChecked(False)
        self.mainHoldLeftDutyButton.setAutoExclusive(False)
        self.maxMainPWMLabel = QLabel(self.mainHBridgeGroup)
        self.maxMainPWMLabel.setObjectName(u"maxMainPWMLabel")
        self.maxMainPWMLabel.setGeometry(QRect(107, 52, 26, 16))
        self.maxMainPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.maxMainPWM = QLineEdit(self.mainHBridgeGroup)
        self.maxMainPWM.setObjectName(u"maxMainPWM")
        self.maxMainPWM.setGeometry(QRect(93, 70, 52, 22))
        self.maxMainPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.maxMainPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.maxMainPWM.setReadOnly(False)
        self.minMainPWM = QLineEdit(self.mainHBridgeGroup)
        self.minMainPWM.setObjectName(u"minMainPWM")
        self.minMainPWM.setGeometry(QRect(93, 170, 52, 22))
        self.minMainPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.minMainPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minMainPWM.setReadOnly(False)
        self.minMainPWMLabel = QLabel(self.mainHBridgeGroup)
        self.minMainPWMLabel.setObjectName(u"minMainPWMLabel")
        self.minMainPWMLabel.setGeometry(QRect(107, 151, 26, 16))
        self.minMainPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.enableMainBridgeButton = QRadioButton(self.mainHBridgeGroup)
        self.enableMainBridgeButton.setObjectName(u"enableMainBridgeButton")
        self.enableMainBridgeButton.setGeometry(QRect(90, 205, 60, 22))
        self.enableMainBridgeButton.setFont(font5)
        self.enableMainBridgeButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableMainBridgeButton.setChecked(False)
        self.enableMainBridgeButton.setAutoExclusive(False)
        self.mainDriveControlGroup = QGroupBox(self.mainDrivePage)
        self.mainDriveControlGroup.setObjectName(u"mainDriveControlGroup")
        self.mainDriveControlGroup.setGeometry(QRect(16, 16, 532, 521))
        self.mainDriveControlGroup.setFont(font6)
        self.mainDriveControlGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 170px 0px 0px; /* Added left padding to move it left */\n"
"    top: 15px;\n"
"}")
        self.mainDriveControlTable = QTableWidget(self.mainDriveControlGroup)
        if (self.mainDriveControlTable.columnCount() < 3):
            self.mainDriveControlTable.setColumnCount(3)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.mainDriveControlTable.setHorizontalHeaderItem(0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.mainDriveControlTable.setHorizontalHeaderItem(1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.mainDriveControlTable.setHorizontalHeaderItem(2, __qtablewidgetitem74)
        self.mainDriveControlTable.setObjectName(u"mainDriveControlTable")
        self.mainDriveControlTable.setGeometry(QRect(17, 50, 246, 407))
        self.mainDriveControlTable.setFont(font8)
        self.mainDriveControlTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mainDriveControlTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.mainDriveControlTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainDriveControlTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainDriveControlTable.setAutoScroll(False)
        self.mainDriveControlTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.mainDriveControlTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.mainDriveControlTable.horizontalHeader().setMinimumSectionSize(40)
        self.mainDriveControlTable.horizontalHeader().setDefaultSectionSize(81)
        self.mainDriveControlTable.horizontalHeader().setStretchLastSection(False)
        self.mainDriveControlTable.verticalHeader().setVisible(False)
        self.mainDriveControlTable.verticalHeader().setMinimumSectionSize(16)
        self.mainDriveControlTable.verticalHeader().setDefaultSectionSize(18)
        self.plotMainButton = QPushButton(self.mainDriveControlGroup)
        self.plotMainButton.setObjectName(u"plotMainButton")
        self.plotMainButton.setGeometry(QRect(117, 472, 69, 33))
        self.plotMainButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.mainPIDPosTable = QTableWidget(self.mainDriveControlGroup)
        if (self.mainPIDPosTable.columnCount() < 3):
            self.mainPIDPosTable.setColumnCount(3)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.mainPIDPosTable.setHorizontalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.mainPIDPosTable.setHorizontalHeaderItem(1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.mainPIDPosTable.setHorizontalHeaderItem(2, __qtablewidgetitem77)
        self.mainPIDPosTable.setObjectName(u"mainPIDPosTable")
        self.mainPIDPosTable.setGeometry(QRect(277, 50, 238, 97))
        self.mainPIDPosTable.setFont(font8)
        self.mainPIDPosTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.mainPIDPosTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.mainPIDPosTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.mainPIDPosTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainPIDPosTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainPIDPosTable.setAutoScroll(False)
        self.mainPIDPosTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.mainPIDPosTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.mainPIDPosTable.horizontalHeader().setMinimumSectionSize(40)
        self.mainPIDPosTable.horizontalHeader().setDefaultSectionSize(79)
        self.mainPIDPosTable.horizontalHeader().setStretchLastSection(False)
        self.mainPIDPosTable.verticalHeader().setVisible(False)
        self.mainPIDPosTable.verticalHeader().setMinimumSectionSize(16)
        self.mainPIDPosTable.verticalHeader().setDefaultSectionSize(18)
        self.mainPIDSpeedTable = QTableWidget(self.mainDriveControlGroup)
        if (self.mainPIDSpeedTable.columnCount() < 3):
            self.mainPIDSpeedTable.setColumnCount(3)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.mainPIDSpeedTable.setHorizontalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.mainPIDSpeedTable.setHorizontalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.mainPIDSpeedTable.setHorizontalHeaderItem(2, __qtablewidgetitem80)
        self.mainPIDSpeedTable.setObjectName(u"mainPIDSpeedTable")
        self.mainPIDSpeedTable.setGeometry(QRect(277, 190, 238, 82))
        self.mainPIDSpeedTable.setFont(font8)
        self.mainPIDSpeedTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.mainPIDSpeedTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.mainPIDSpeedTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.mainPIDSpeedTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainPIDSpeedTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainPIDSpeedTable.setAutoScroll(False)
        self.mainPIDSpeedTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.mainPIDSpeedTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.mainPIDSpeedTable.horizontalHeader().setMinimumSectionSize(40)
        self.mainPIDSpeedTable.horizontalHeader().setDefaultSectionSize(79)
        self.mainPIDSpeedTable.horizontalHeader().setStretchLastSection(False)
        self.mainPIDSpeedTable.verticalHeader().setVisible(False)
        self.mainPIDSpeedTable.verticalHeader().setMinimumSectionSize(16)
        self.mainPIDSpeedTable.verticalHeader().setDefaultSectionSize(18)
        self.enableMainSpeedButton = QRadioButton(self.mainDriveControlGroup)
        self.enableMainSpeedButton.setObjectName(u"enableMainSpeedButton")
        self.enableMainSpeedButton.setGeometry(QRect(330, 160, 144, 22))
        self.enableMainSpeedButton.setFont(font5)
        self.enableMainSpeedButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableMainSpeedButton.setChecked(False)
        self.enableMainSpeedButton.setAutoExclusive(False)
        self.requestMainTuningButton = QPushButton(self.mainDriveControlGroup)
        self.requestMainTuningButton.setObjectName(u"requestMainTuningButton")
        self.requestMainTuningButton.setGeometry(QRect(280, 285, 51, 22))
        self.requestMainTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.copyMainTuningButton = QPushButton(self.mainDriveControlGroup)
        self.copyMainTuningButton.setObjectName(u"copyMainTuningButton")
        self.copyMainTuningButton.setGeometry(QRect(340, 285, 51, 22))
        self.copyMainTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.alterMainTuningButton = QPushButton(self.mainDriveControlGroup)
        self.alterMainTuningButton.setObjectName(u"alterMainTuningButton")
        self.alterMainTuningButton.setGeometry(QRect(460, 285, 51, 22))
        self.alterMainTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.topLine_11 = QFrame(self.mainDriveControlGroup)
        self.topLine_11.setObjectName(u"topLine_11")
        self.topLine_11.setGeometry(QRect(277, 322, 237, 2))
        self.topLine_11.setFont(font4)
        self.topLine_11.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_11.setFrameShape(QFrame.Shape.HLine)
        self.topLine_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.autoMainPlotButton = QRadioButton(self.mainDriveControlGroup)
        self.mainPlotModeButtonGroup = QButtonGroup(MainWindow)
        self.mainPlotModeButtonGroup.setObjectName(u"mainPlotModeButtonGroup")
        self.mainPlotModeButtonGroup.addButton(self.autoMainPlotButton)
        self.autoMainPlotButton.setObjectName(u"autoMainPlotButton")
        self.autoMainPlotButton.setGeometry(QRect(19, 463, 63, 22))
        self.autoMainPlotButton.setFont(font5)
        self.autoMainPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoMainPlotButton.setChecked(False)
        self.autoMainPlotButton.setAutoExclusive(True)
        self.manualMainPlotButton = QRadioButton(self.mainDriveControlGroup)
        self.mainPlotModeButtonGroup.addButton(self.manualMainPlotButton)
        self.manualMainPlotButton.setObjectName(u"manualMainPlotButton")
        self.manualMainPlotButton.setGeometry(QRect(19, 488, 72, 22))
        self.manualMainPlotButton.setFont(font5)
        self.manualMainPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualMainPlotButton.setChecked(True)
        self.manualMainPlotButton.setAutoExclusive(True)
        self.openMainPlotButton = QPushButton(self.mainDriveControlGroup)
        self.openMainPlotButton.setObjectName(u"openMainPlotButton")
        self.openMainPlotButton.setGeometry(QRect(194, 472, 69, 33))
        self.openMainPlotButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
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
        self.requestMainLoggingButton = QPushButton(self.mainDriveControlGroup)
        self.requestMainLoggingButton.setObjectName(u"requestMainLoggingButton")
        self.requestMainLoggingButton.setGeometry(QRect(17, 17, 79, 22))
        self.requestMainLoggingButton.setStyleSheet(u"QPushButton {\n"
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
        self.selectMainFolderButton = QPushButton(self.mainDriveControlGroup)
        self.selectMainFolderButton.setObjectName(u"selectMainFolderButton")
        self.selectMainFolderButton.setGeometry(QRect(340, 370, 111, 22))
        self.selectMainFolderButton.setStyleSheet(u"QPushButton {\n"
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
        self.mainFolder = QLineEdit(self.mainDriveControlGroup)
        self.mainFolder.setObjectName(u"mainFolder")
        self.mainFolder.setGeometry(QRect(278, 337, 236, 22))
        self.mainFolder.setFont(font8)
        self.mainFolder.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.mainFolder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainFolder.setReadOnly(True)
        self.resetMainTuningButton = QPushButton(self.mainDriveControlGroup)
        self.resetMainTuningButton.setObjectName(u"resetMainTuningButton")
        self.resetMainTuningButton.setGeometry(QRect(400, 285, 51, 22))
        self.resetMainTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.mainHSLabel = QLabel(self.mainDriveControlGroup)
        self.mainHSLabel.setObjectName(u"mainHSLabel")
        self.mainHSLabel.setGeometry(QRect(297, 434, 97, 17))
        self.mainHSLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.mainPlottingLabel = QLabel(self.mainDriveControlGroup)
        self.mainPlottingLabel.setObjectName(u"mainPlottingLabel")
        self.mainPlottingLabel.setGeometry(QRect(316, 486, 78, 16))
        self.mainPlottingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.mainLoggingState = QLineEdit(self.mainDriveControlGroup)
        self.mainLoggingState.setObjectName(u"mainLoggingState")
        self.mainLoggingState.setGeometry(QRect(397, 457, 121, 22))
        self.mainLoggingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.mainLoggingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLoggingState.setReadOnly(True)
        self.mainHSState = QLineEdit(self.mainDriveControlGroup)
        self.mainHSState.setObjectName(u"mainHSState")
        self.mainHSState.setGeometry(QRect(397, 431, 121, 22))
        self.mainHSState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.mainHSState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainHSState.setReadOnly(True)
        self.mainLoggingLabel = QLabel(self.mainDriveControlGroup)
        self.mainLoggingLabel.setObjectName(u"mainLoggingLabel")
        self.mainLoggingLabel.setGeometry(QRect(314, 460, 81, 16))
        self.mainLoggingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.mainPlottingState = QLineEdit(self.mainDriveControlGroup)
        self.mainPlottingState.setObjectName(u"mainPlottingState")
        self.mainPlottingState.setGeometry(QRect(397, 483, 121, 22))
        self.mainPlottingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.mainPlottingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainPlottingState.setReadOnly(True)
        self.mainDrivePositionGroup = QGroupBox(self.mainDrivePage)
        self.mainDrivePositionGroup.setObjectName(u"mainDrivePositionGroup")
        self.mainDrivePositionGroup.setGeometry(QRect(564, 16, 238, 109))
        self.mainDrivePositionGroup.setFont(font6)
        self.mainDrivePositionGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.mainDrivePositionTable = QTableWidget(self.mainDrivePositionGroup)
        if (self.mainDrivePositionTable.columnCount() < 2):
            self.mainDrivePositionTable.setColumnCount(2)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.mainDrivePositionTable.setHorizontalHeaderItem(0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.mainDrivePositionTable.setHorizontalHeaderItem(1, __qtablewidgetitem82)
        self.mainDrivePositionTable.setObjectName(u"mainDrivePositionTable")
        self.mainDrivePositionTable.setGeometry(QRect(17, 50, 203, 39))
        self.mainDrivePositionTable.setFont(font8)
        self.mainDrivePositionTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mainDrivePositionTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.mainDrivePositionTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainDrivePositionTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainDrivePositionTable.setAutoScroll(False)
        self.mainDrivePositionTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.mainDrivePositionTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.mainDrivePositionTable.horizontalHeader().setVisible(False)
        self.mainDrivePositionTable.horizontalHeader().setMinimumSectionSize(40)
        self.mainDrivePositionTable.horizontalHeader().setDefaultSectionSize(100)
        self.mainDrivePositionTable.horizontalHeader().setStretchLastSection(False)
        self.mainDrivePositionTable.verticalHeader().setVisible(False)
        self.mainDrivePositionTable.verticalHeader().setMinimumSectionSize(16)
        self.mainDrivePositionTable.verticalHeader().setDefaultSectionSize(18)
        self.requestMainPositionButton = QPushButton(self.mainDrivePositionGroup)
        self.requestMainPositionButton.setObjectName(u"requestMainPositionButton")
        self.requestMainPositionButton.setGeometry(QRect(17, 16, 51, 22))
        self.requestMainPositionButton.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget.addWidget(self.mainDrivePage)
        self.swivelPage = QWidget()
        self.swivelPage.setObjectName(u"swivelPage")
        self.swivelDrivePositionGroup = QGroupBox(self.swivelPage)
        self.swivelDrivePositionGroup.setObjectName(u"swivelDrivePositionGroup")
        self.swivelDrivePositionGroup.setGeometry(QRect(564, 16, 238, 199))
        self.swivelDrivePositionGroup.setFont(font6)
        self.swivelDrivePositionGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.swivelDrivePositionTable = QTableWidget(self.swivelDrivePositionGroup)
        if (self.swivelDrivePositionTable.columnCount() < 2):
            self.swivelDrivePositionTable.setColumnCount(2)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.swivelDrivePositionTable.setHorizontalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.swivelDrivePositionTable.setHorizontalHeaderItem(1, __qtablewidgetitem84)
        self.swivelDrivePositionTable.setObjectName(u"swivelDrivePositionTable")
        self.swivelDrivePositionTable.setGeometry(QRect(17, 50, 203, 129))
        self.swivelDrivePositionTable.setFont(font8)
        self.swivelDrivePositionTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.swivelDrivePositionTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.swivelDrivePositionTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelDrivePositionTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelDrivePositionTable.setAutoScroll(False)
        self.swivelDrivePositionTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.swivelDrivePositionTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.swivelDrivePositionTable.horizontalHeader().setVisible(False)
        self.swivelDrivePositionTable.horizontalHeader().setMinimumSectionSize(40)
        self.swivelDrivePositionTable.horizontalHeader().setDefaultSectionSize(100)
        self.swivelDrivePositionTable.horizontalHeader().setStretchLastSection(False)
        self.swivelDrivePositionTable.verticalHeader().setVisible(False)
        self.swivelDrivePositionTable.verticalHeader().setMinimumSectionSize(16)
        self.swivelDrivePositionTable.verticalHeader().setDefaultSectionSize(18)
        self.requestSwivelPositionButton = QPushButton(self.swivelDrivePositionGroup)
        self.requestSwivelPositionButton.setObjectName(u"requestSwivelPositionButton")
        self.requestSwivelPositionButton.setGeometry(QRect(17, 16, 51, 22))
        self.requestSwivelPositionButton.setStyleSheet(u"QPushButton {\n"
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
        self.swivelCalibrationGroup = QGroupBox(self.swivelPage)
        self.swivelCalibrationGroup.setObjectName(u"swivelCalibrationGroup")
        self.swivelCalibrationGroup.setGeometry(QRect(16, 552, 191, 123))
        self.swivelCalibrationGroup.setFont(font6)
        self.swivelCalibrationGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.autoSwivelCalButton = QRadioButton(self.swivelCalibrationGroup)
        self.autoSwivelCalButton.setObjectName(u"autoSwivelCalButton")
        self.autoSwivelCalButton.setGeometry(QRect(29, 90, 63, 22))
        self.autoSwivelCalButton.setFont(font5)
        self.autoSwivelCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoSwivelCalButton.setChecked(False)
        self.autoSwivelCalButton.setAutoExclusive(True)
        self.manualSwivelCalButton = QRadioButton(self.swivelCalibrationGroup)
        self.manualSwivelCalButton.setObjectName(u"manualSwivelCalButton")
        self.manualSwivelCalButton.setGeometry(QRect(99, 90, 72, 22))
        self.manualSwivelCalButton.setFont(font5)
        self.manualSwivelCalButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualSwivelCalButton.setChecked(True)
        self.manualSwivelCalButton.setAutoExclusive(True)
        self.startSwivelCalButton = QPushButton(self.swivelCalibrationGroup)
        self.startSwivelCalButton.setObjectName(u"startSwivelCalButton")
        self.startSwivelCalButton.setGeometry(QRect(10, 50, 49, 27))
        self.startSwivelCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.acceptSwivelCalButton = QPushButton(self.swivelCalibrationGroup)
        self.acceptSwivelCalButton.setObjectName(u"acceptSwivelCalButton")
        self.acceptSwivelCalButton.setGeometry(QRect(70, 50, 49, 27))
        self.acceptSwivelCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.rejectSwivelCalButton = QPushButton(self.swivelCalibrationGroup)
        self.rejectSwivelCalButton.setObjectName(u"rejectSwivelCalButton")
        self.rejectSwivelCalButton.setGeometry(QRect(130, 50, 49, 27))
        self.rejectSwivelCalButton.setStyleSheet(u"QPushButton {\n"
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
        self.swivelDriveControlGroup = QGroupBox(self.swivelPage)
        self.swivelDriveControlGroup.setObjectName(u"swivelDriveControlGroup")
        self.swivelDriveControlGroup.setGeometry(QRect(16, 16, 532, 521))
        self.swivelDriveControlGroup.setFont(font6)
        self.swivelDriveControlGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 170px 0px 0px; /* Added left padding to move it left */\n"
"    top: 15px;\n"
"}")
        self.swivelDriveControlTable = QTableWidget(self.swivelDriveControlGroup)
        if (self.swivelDriveControlTable.columnCount() < 3):
            self.swivelDriveControlTable.setColumnCount(3)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.swivelDriveControlTable.setHorizontalHeaderItem(0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.swivelDriveControlTable.setHorizontalHeaderItem(1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.swivelDriveControlTable.setHorizontalHeaderItem(2, __qtablewidgetitem87)
        self.swivelDriveControlTable.setObjectName(u"swivelDriveControlTable")
        self.swivelDriveControlTable.setGeometry(QRect(17, 50, 246, 407))
        self.swivelDriveControlTable.setFont(font8)
        self.swivelDriveControlTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.swivelDriveControlTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.swivelDriveControlTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelDriveControlTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelDriveControlTable.setAutoScroll(False)
        self.swivelDriveControlTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.swivelDriveControlTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.swivelDriveControlTable.horizontalHeader().setMinimumSectionSize(40)
        self.swivelDriveControlTable.horizontalHeader().setDefaultSectionSize(81)
        self.swivelDriveControlTable.horizontalHeader().setStretchLastSection(False)
        self.swivelDriveControlTable.verticalHeader().setVisible(False)
        self.swivelDriveControlTable.verticalHeader().setMinimumSectionSize(16)
        self.swivelDriveControlTable.verticalHeader().setDefaultSectionSize(18)
        self.plotSwivelButton = QPushButton(self.swivelDriveControlGroup)
        self.plotSwivelButton.setObjectName(u"plotSwivelButton")
        self.plotSwivelButton.setGeometry(QRect(117, 472, 69, 33))
        self.plotSwivelButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
"}")
        self.swivelPIDPosTable = QTableWidget(self.swivelDriveControlGroup)
        if (self.swivelPIDPosTable.columnCount() < 3):
            self.swivelPIDPosTable.setColumnCount(3)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.swivelPIDPosTable.setHorizontalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.swivelPIDPosTable.setHorizontalHeaderItem(1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.swivelPIDPosTable.setHorizontalHeaderItem(2, __qtablewidgetitem90)
        self.swivelPIDPosTable.setObjectName(u"swivelPIDPosTable")
        self.swivelPIDPosTable.setGeometry(QRect(277, 50, 238, 97))
        self.swivelPIDPosTable.setFont(font8)
        self.swivelPIDPosTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.swivelPIDPosTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.swivelPIDPosTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.swivelPIDPosTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelPIDPosTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelPIDPosTable.setAutoScroll(False)
        self.swivelPIDPosTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.swivelPIDPosTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.swivelPIDPosTable.horizontalHeader().setMinimumSectionSize(40)
        self.swivelPIDPosTable.horizontalHeader().setDefaultSectionSize(79)
        self.swivelPIDPosTable.horizontalHeader().setStretchLastSection(False)
        self.swivelPIDPosTable.verticalHeader().setVisible(False)
        self.swivelPIDPosTable.verticalHeader().setMinimumSectionSize(16)
        self.swivelPIDPosTable.verticalHeader().setDefaultSectionSize(18)
        self.swivelPIDSpeedTable = QTableWidget(self.swivelDriveControlGroup)
        if (self.swivelPIDSpeedTable.columnCount() < 3):
            self.swivelPIDSpeedTable.setColumnCount(3)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.swivelPIDSpeedTable.setHorizontalHeaderItem(0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.swivelPIDSpeedTable.setHorizontalHeaderItem(1, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.swivelPIDSpeedTable.setHorizontalHeaderItem(2, __qtablewidgetitem93)
        self.swivelPIDSpeedTable.setObjectName(u"swivelPIDSpeedTable")
        self.swivelPIDSpeedTable.setGeometry(QRect(277, 190, 238, 82))
        self.swivelPIDSpeedTable.setFont(font8)
        self.swivelPIDSpeedTable.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.swivelPIDSpeedTable.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.swivelPIDSpeedTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.swivelPIDSpeedTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelPIDSpeedTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelPIDSpeedTable.setAutoScroll(False)
        self.swivelPIDSpeedTable.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked)
        self.swivelPIDSpeedTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.swivelPIDSpeedTable.horizontalHeader().setMinimumSectionSize(40)
        self.swivelPIDSpeedTable.horizontalHeader().setDefaultSectionSize(79)
        self.swivelPIDSpeedTable.horizontalHeader().setStretchLastSection(False)
        self.swivelPIDSpeedTable.verticalHeader().setVisible(False)
        self.swivelPIDSpeedTable.verticalHeader().setMinimumSectionSize(16)
        self.swivelPIDSpeedTable.verticalHeader().setDefaultSectionSize(18)
        self.enableSwivelSpeedButton = QRadioButton(self.swivelDriveControlGroup)
        self.enableSwivelSpeedButton.setObjectName(u"enableSwivelSpeedButton")
        self.enableSwivelSpeedButton.setGeometry(QRect(330, 160, 144, 22))
        self.enableSwivelSpeedButton.setFont(font5)
        self.enableSwivelSpeedButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableSwivelSpeedButton.setChecked(False)
        self.enableSwivelSpeedButton.setAutoExclusive(False)
        self.requestSwivelTuningButton = QPushButton(self.swivelDriveControlGroup)
        self.requestSwivelTuningButton.setObjectName(u"requestSwivelTuningButton")
        self.requestSwivelTuningButton.setGeometry(QRect(280, 285, 51, 22))
        self.requestSwivelTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.copySwivelTuningButton = QPushButton(self.swivelDriveControlGroup)
        self.copySwivelTuningButton.setObjectName(u"copySwivelTuningButton")
        self.copySwivelTuningButton.setGeometry(QRect(340, 285, 51, 22))
        self.copySwivelTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.alterSwivelTuningButton = QPushButton(self.swivelDriveControlGroup)
        self.alterSwivelTuningButton.setObjectName(u"alterSwivelTuningButton")
        self.alterSwivelTuningButton.setGeometry(QRect(460, 285, 51, 22))
        self.alterSwivelTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.topLine_6 = QFrame(self.swivelDriveControlGroup)
        self.topLine_6.setObjectName(u"topLine_6")
        self.topLine_6.setGeometry(QRect(277, 322, 237, 2))
        self.topLine_6.setFont(font4)
        self.topLine_6.setStyleSheet(u"QFrame {\n"
"    background-color: #000000; /* Solid black line */\n"
"    max-height: 2px;          /* Restrict height to 1px */\n"
"    min-height: 2px;          /* Ensure it stays 1px tall */\n"
"    border: none;             /* Remove any borders */\n"
"}")
        self.topLine_6.setFrameShape(QFrame.Shape.HLine)
        self.topLine_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.autoSwivelPlotButton = QRadioButton(self.swivelDriveControlGroup)
        self.swivelPlotModeButtonGroup = QButtonGroup(MainWindow)
        self.swivelPlotModeButtonGroup.setObjectName(u"swivelPlotModeButtonGroup")
        self.swivelPlotModeButtonGroup.addButton(self.autoSwivelPlotButton)
        self.autoSwivelPlotButton.setObjectName(u"autoSwivelPlotButton")
        self.autoSwivelPlotButton.setGeometry(QRect(19, 463, 63, 22))
        self.autoSwivelPlotButton.setFont(font5)
        self.autoSwivelPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.autoSwivelPlotButton.setChecked(False)
        self.autoSwivelPlotButton.setAutoExclusive(True)
        self.manualSwivelPlotButton = QRadioButton(self.swivelDriveControlGroup)
        self.swivelPlotModeButtonGroup.addButton(self.manualSwivelPlotButton)
        self.manualSwivelPlotButton.setObjectName(u"manualSwivelPlotButton")
        self.manualSwivelPlotButton.setGeometry(QRect(19, 488, 72, 22))
        self.manualSwivelPlotButton.setFont(font5)
        self.manualSwivelPlotButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.manualSwivelPlotButton.setChecked(True)
        self.manualSwivelPlotButton.setAutoExclusive(True)
        self.openSwivelPlotButton = QPushButton(self.swivelDriveControlGroup)
        self.openSwivelPlotButton.setObjectName(u"openSwivelPlotButton")
        self.openSwivelPlotButton.setGeometry(QRect(194, 472, 69, 33))
        self.openSwivelPlotButton.setStyleSheet(u"QPushButton {\n"
"    color: #000000; /* Text color */\n"
"    border: 2px solid #000000; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"	background-color: #FFA2A7;\n"
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
        self.requestSwivelLoggingButton = QPushButton(self.swivelDriveControlGroup)
        self.requestSwivelLoggingButton.setObjectName(u"requestSwivelLoggingButton")
        self.requestSwivelLoggingButton.setGeometry(QRect(17, 17, 79, 22))
        self.requestSwivelLoggingButton.setStyleSheet(u"QPushButton {\n"
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
        self.selectSwivelFolderButton = QPushButton(self.swivelDriveControlGroup)
        self.selectSwivelFolderButton.setObjectName(u"selectSwivelFolderButton")
        self.selectSwivelFolderButton.setGeometry(QRect(340, 370, 111, 22))
        self.selectSwivelFolderButton.setStyleSheet(u"QPushButton {\n"
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
        self.swivelFolder = QLineEdit(self.swivelDriveControlGroup)
        self.swivelFolder.setObjectName(u"swivelFolder")
        self.swivelFolder.setGeometry(QRect(278, 337, 236, 22))
        self.swivelFolder.setFont(font8)
        self.swivelFolder.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.swivelFolder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.swivelFolder.setReadOnly(True)
        self.resetSwivelTuningButton = QPushButton(self.swivelDriveControlGroup)
        self.resetSwivelTuningButton.setObjectName(u"resetSwivelTuningButton")
        self.resetSwivelTuningButton.setGeometry(QRect(400, 285, 51, 22))
        self.resetSwivelTuningButton.setStyleSheet(u"QPushButton {\n"
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
        self.swivelLeftTuneButton = QRadioButton(self.swivelDriveControlGroup)
        self.swivelTuneButtonGroup = QButtonGroup(MainWindow)
        self.swivelTuneButtonGroup.setObjectName(u"swivelTuneButtonGroup")
        self.swivelTuneButtonGroup.addButton(self.swivelLeftTuneButton)
        self.swivelLeftTuneButton.setObjectName(u"swivelLeftTuneButton")
        self.swivelLeftTuneButton.setGeometry(QRect(300, 20, 50, 22))
        self.swivelLeftTuneButton.setFont(font5)
        self.swivelLeftTuneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.swivelLeftTuneButton.setChecked(True)
        self.swivelLeftTuneButton.setAutoExclusive(True)
        self.swivelRightTuneButton = QRadioButton(self.swivelDriveControlGroup)
        self.swivelTuneButtonGroup.addButton(self.swivelRightTuneButton)
        self.swivelRightTuneButton.setObjectName(u"swivelRightTuneButton")
        self.swivelRightTuneButton.setGeometry(QRect(434, 20, 58, 22))
        self.swivelRightTuneButton.setFont(font5)
        self.swivelRightTuneButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.swivelRightTuneButton.setChecked(False)
        self.swivelRightTuneButton.setAutoExclusive(True)
        self.swivelHSLabel = QLabel(self.swivelDriveControlGroup)
        self.swivelHSLabel.setObjectName(u"swivelHSLabel")
        self.swivelHSLabel.setGeometry(QRect(297, 434, 97, 17))
        self.swivelHSLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.swivelPlottingLabel = QLabel(self.swivelDriveControlGroup)
        self.swivelPlottingLabel.setObjectName(u"swivelPlottingLabel")
        self.swivelPlottingLabel.setGeometry(QRect(316, 486, 78, 16))
        self.swivelPlottingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.swivelLoggingState = QLineEdit(self.swivelDriveControlGroup)
        self.swivelLoggingState.setObjectName(u"swivelLoggingState")
        self.swivelLoggingState.setGeometry(QRect(397, 457, 121, 22))
        self.swivelLoggingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.swivelLoggingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.swivelLoggingState.setReadOnly(True)
        self.swivelHSState = QLineEdit(self.swivelDriveControlGroup)
        self.swivelHSState.setObjectName(u"swivelHSState")
        self.swivelHSState.setGeometry(QRect(397, 431, 121, 22))
        self.swivelHSState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.swivelHSState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.swivelHSState.setReadOnly(True)
        self.swivelLoggingLabel = QLabel(self.swivelDriveControlGroup)
        self.swivelLoggingLabel.setObjectName(u"swivelLoggingLabel")
        self.swivelLoggingLabel.setGeometry(QRect(314, 460, 81, 16))
        self.swivelLoggingLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.swivelPlottingState = QLineEdit(self.swivelDriveControlGroup)
        self.swivelPlottingState.setObjectName(u"swivelPlottingState")
        self.swivelPlottingState.setGeometry(QRect(397, 483, 121, 22))
        self.swivelPlottingState.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.swivelPlottingState.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.swivelPlottingState.setReadOnly(True)
        self.swivelHBridgeGroup = QGroupBox(self.swivelPage)
        self.swivelHBridgeGroup.setObjectName(u"swivelHBridgeGroup")
        self.swivelHBridgeGroup.setGeometry(QRect(564, 390, 238, 233))
        self.swivelHBridgeGroup.setFont(font6)
        self.swivelHBridgeGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 10px;\n"
"	top: 15px;\n"
"}")
        self.swivelLeftBridgeDuty = QSlider(self.swivelHBridgeGroup)
        self.swivelLeftBridgeDuty.setObjectName(u"swivelLeftBridgeDuty")
        self.swivelLeftBridgeDuty.setGeometry(QRect(30, 46, 22, 170))
        self.swivelLeftBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.swivelLeftBridgeDuty.setMaximum(980)
        self.swivelLeftBridgeDuty.setPageStep(100)
        self.swivelLeftBridgeDuty.setValue(0)
        self.swivelLeftBridgeDuty.setSliderPosition(0)
        self.swivelLeftBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.swivelLeftBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.swivelRightBridgeDuty = QSlider(self.swivelHBridgeGroup)
        self.swivelRightBridgeDuty.setObjectName(u"swivelRightBridgeDuty")
        self.swivelRightBridgeDuty.setGeometry(QRect(186, 46, 22, 170))
        self.swivelRightBridgeDuty.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: black;\n"
"    width: 4px;  /* Width of the groove */\n"
"    margin: 0 8px;  /* Keep horizontal spacing */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #F03F3F;  /* Red handle */\n"
"	border: 1px solid black;\n"
"    border-radius: 4px;\n"
"    height: 12px;\n"
"    width: 20px;  /* Increased width for a wider handle */\n"
"    margin: 0 -8px;  /* Adjusted to center the wider handle */\n"
"}")
        self.swivelRightBridgeDuty.setMaximum(980)
        self.swivelRightBridgeDuty.setPageStep(100)
        self.swivelRightBridgeDuty.setValue(0)
        self.swivelRightBridgeDuty.setSliderPosition(0)
        self.swivelRightBridgeDuty.setOrientation(Qt.Orientation.Vertical)
        self.swivelRightBridgeDuty.setTickPosition(QSlider.TickPosition.NoTicks)
        self.swivelLeftBridgeText = QLineEdit(self.swivelHBridgeGroup)
        self.swivelLeftBridgeText.setObjectName(u"swivelLeftBridgeText")
        self.swivelLeftBridgeText.setGeometry(QRect(61, 117, 44, 22))
        self.swivelLeftBridgeText.setFont(font13)
        self.swivelLeftBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.swivelRightBridgeText = QLineEdit(self.swivelHBridgeGroup)
        self.swivelRightBridgeText.setObjectName(u"swivelRightBridgeText")
        self.swivelRightBridgeText.setGeometry(QRect(130, 117, 43, 22))
        self.swivelRightBridgeText.setFont(font13)
        self.swivelRightBridgeText.setStyleSheet(u"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: none;\n"
"}")
        self.swivelRightBridgeText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.swivelHoldRightDutyButton = QRadioButton(self.swivelHBridgeGroup)
        self.swivelHoldRightDutyButton.setObjectName(u"swivelHoldRightDutyButton")
        self.swivelHoldRightDutyButton.setGeometry(QRect(174, 17, 51, 22))
        self.swivelHoldRightDutyButton.setFont(font5)
        self.swivelHoldRightDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.swivelHoldRightDutyButton.setChecked(False)
        self.swivelHoldRightDutyButton.setAutoExclusive(False)
        self.swivelHoldLeftDutyButton = QRadioButton(self.swivelHBridgeGroup)
        self.swivelHoldLeftDutyButton.setObjectName(u"swivelHoldLeftDutyButton")
        self.swivelHoldLeftDutyButton.setGeometry(QRect(18, 17, 51, 22))
        self.swivelHoldLeftDutyButton.setFont(font5)
        self.swivelHoldLeftDutyButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.swivelHoldLeftDutyButton.setChecked(False)
        self.swivelHoldLeftDutyButton.setAutoExclusive(False)
        self.maxSwivelPWMLabel = QLabel(self.swivelHBridgeGroup)
        self.maxSwivelPWMLabel.setObjectName(u"maxSwivelPWMLabel")
        self.maxSwivelPWMLabel.setGeometry(QRect(107, 52, 26, 16))
        self.maxSwivelPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.maxSwivelPWM = QLineEdit(self.swivelHBridgeGroup)
        self.maxSwivelPWM.setObjectName(u"maxSwivelPWM")
        self.maxSwivelPWM.setGeometry(QRect(93, 70, 52, 22))
        self.maxSwivelPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.maxSwivelPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.maxSwivelPWM.setReadOnly(False)
        self.minSwivelPWM = QLineEdit(self.swivelHBridgeGroup)
        self.minSwivelPWM.setObjectName(u"minSwivelPWM")
        self.minSwivelPWM.setGeometry(QRect(93, 170, 52, 22))
        self.minSwivelPWM.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.minSwivelPWM.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minSwivelPWM.setReadOnly(False)
        self.minSwivelPWMLabel = QLabel(self.swivelHBridgeGroup)
        self.minSwivelPWMLabel.setObjectName(u"minSwivelPWMLabel")
        self.minSwivelPWMLabel.setGeometry(QRect(107, 151, 26, 16))
        self.minSwivelPWMLabel.setStyleSheet(u"background: transparent;\n"
"color: black;")
        self.enableSwivelBridgeButton = QRadioButton(self.swivelHBridgeGroup)
        self.enableSwivelBridgeButton.setObjectName(u"enableSwivelBridgeButton")
        self.enableSwivelBridgeButton.setGeometry(QRect(90, 205, 60, 22))
        self.enableSwivelBridgeButton.setFont(font5)
        self.enableSwivelBridgeButton.setStyleSheet(u"QRadioButton {\n"
"    color: #000000; /* Text color */\n"
"	background-color: transparent;\n"
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
        self.enableSwivelBridgeButton.setChecked(False)
        self.enableSwivelBridgeButton.setAutoExclusive(False)
        self.swivelStateMachineGroup = QGroupBox(self.swivelPage)
        self.swivelStateMachineGroup.setObjectName(u"swivelStateMachineGroup")
        self.swivelStateMachineGroup.setGeometry(QRect(564, 230, 238, 144))
        self.swivelStateMachineGroup.setFont(font6)
        self.swivelStateMachineGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #57CAFF;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 0px 0px 0px;\n"
"	top: 15px;\n"
"}")
        self.swivelStateMachineTable = QTableWidget(self.swivelStateMachineGroup)
        if (self.swivelStateMachineTable.columnCount() < 2):
            self.swivelStateMachineTable.setColumnCount(2)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.swivelStateMachineTable.setHorizontalHeaderItem(0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.swivelStateMachineTable.setHorizontalHeaderItem(1, __qtablewidgetitem95)
        self.swivelStateMachineTable.setObjectName(u"swivelStateMachineTable")
        self.swivelStateMachineTable.setGeometry(QRect(17, 50, 203, 75))
        self.swivelStateMachineTable.setFont(font8)
        self.swivelStateMachineTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.swivelStateMachineTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F6FF68;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"	color: black;\n"
"}")
        self.swivelStateMachineTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelStateMachineTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.swivelStateMachineTable.setAutoScroll(False)
        self.swivelStateMachineTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.swivelStateMachineTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.swivelStateMachineTable.horizontalHeader().setVisible(False)
        self.swivelStateMachineTable.horizontalHeader().setMinimumSectionSize(40)
        self.swivelStateMachineTable.horizontalHeader().setDefaultSectionSize(100)
        self.swivelStateMachineTable.horizontalHeader().setStretchLastSection(False)
        self.swivelStateMachineTable.verticalHeader().setVisible(False)
        self.swivelStateMachineTable.verticalHeader().setMinimumSectionSize(16)
        self.swivelStateMachineTable.verticalHeader().setDefaultSectionSize(18)
        self.stackedWidget.addWidget(self.swivelPage)
        self.x06Page = QWidget()
        self.x06Page.setObjectName(u"x06Page")
        self.enableX06MessagesButton = QRadioButton(self.x06Page)
        self.enableX06MessagesButton.setObjectName(u"enableX06MessagesButton")
        self.enableX06MessagesButton.setGeometry(QRect(14, 13, 139, 22))
        self.enableX06MessagesButton.setFont(font5)
        self.enableX06MessagesButton.setStyleSheet(u"QRadioButton {\n"
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
        self.enableX06MessagesButton.setChecked(False)
        self.enableX06MessagesButton.setAutoExclusive(False)
        self.stackedWidget.addWidget(self.x06Page)
        self.consoleTab = QTabWidget(self.centralwidget)
        self.consoleTab.setObjectName(u"consoleTab")
        self.consoleTab.setGeometry(QRect(1219, 11, 636, 986))
        font14 = QFont()
        font14.setBold(True)
        font14.setItalic(True)
        self.consoleTab.setFont(font14)
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
        self.clearPrimaryConsoleButton.setGeometry(QRect(540, 870, 51, 22))
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
        self.savePrimaryConsoleButton.setGeometry(QRect(540, 900, 51, 22))
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
"    min-height: 20px; /* Minimum height of the handle */\n"
"}\n"
""
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
"    background: none; /* No background for the add-page and sub-page */\n"
"    border: none; /* Remove any border */\n"
"}"
                        "\n"
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
"    background: none; /* Consistent background for hidin"
                        "g */\n"
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
        self.saveSecondaryConsoleButton.setGeometry(QRect(540, 900, 51, 22))
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
        self.clearSecondaryConsoleButton.setGeometry(QRect(540, 870, 51, 22))
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
"    min-height: 20px; /* Minimum height of the handle */\n"
"}\n"
""
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
"    background: none; /* No background for the add-page and sub-page */\n"
"    border: none; /* Remove any border */\n"
"}"
                        "\n"
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
"    background: none; /* Consistent background for hidin"
                        "g */\n"
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
"    min-height: 20px; /* Minimum height of the handle */\n"
"}\n"
""
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
"    background: none; /* No background for the add-page and sub-page */\n"
"    border: none; /* Remove any border */\n"
"}"
                        "\n"
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
"    background: none; /* Consistent background for hidin"
                        "g */\n"
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
        self.clearTertiaryConsoleButton.setGeometry(QRect(540, 870, 51, 22))
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
        self.saveTertiaryConsoleButton.setGeometry(QRect(540, 900, 51, 22))
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
        self.hexDisplayGroup = QGroupBox(self.sysFrame)
        self.hexDisplayGroup.setObjectName(u"hexDisplayGroup")
        self.hexDisplayGroup.setGeometry(QRect(553, 12, 256, 96))
        font15 = QFont()
        font15.setPointSize(10)
        font15.setBold(True)
        self.hexDisplayGroup.setFont(font15)
        self.hexDisplayGroup.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid black; /* Border for the group box */\n"
"    border-radius: 5px; /* Rounded corners for the border */\n"
"	background-color: #000000;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"	color: black;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0px 0px 0px 0px;\n"
"	top: 5px;\n"
"}")
        self.hexDigitE = QLCDNumber(self.hexDisplayGroup)
        self.hexDigitE.setObjectName(u"hexDigitE")
        self.hexDigitE.setGeometry(QRect(13, 0, 43, 95))
        self.hexDigitE.setStyleSheet(u"QLCDNumber {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: red;\n"
"}")
        self.hexDigitE.setDigitCount(1)
        self.hexDigitE.setMode(QLCDNumber.Mode.Hex)
        self.hexDigitE.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.hexDigitE.setProperty(u"intValue", 14)
        self.hexDigit0 = QLCDNumber(self.hexDisplayGroup)
        self.hexDigit0.setObjectName(u"hexDigit0")
        self.hexDigit0.setGeometry(QRect(60, 0, 43, 95))
        self.hexDigit0.setStyleSheet(u"QLCDNumber {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: red;\n"
"}")
        self.hexDigit0.setDigitCount(1)
        self.hexDigit0.setMode(QLCDNumber.Mode.Hex)
        self.hexDigit0.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.hexDigit0.setProperty(u"value", 0.000000000000000)
        self.hexDigit0.setProperty(u"intValue", 0)
        self.hexDigit1 = QLCDNumber(self.hexDisplayGroup)
        self.hexDigit1.setObjectName(u"hexDigit1")
        self.hexDigit1.setGeometry(QRect(100, 0, 43, 95))
        self.hexDigit1.setStyleSheet(u"QLCDNumber {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: red;\n"
"}")
        self.hexDigit1.setSmallDecimalPoint(False)
        self.hexDigit1.setDigitCount(1)
        self.hexDigit1.setMode(QLCDNumber.Mode.Hex)
        self.hexDigit1.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.hexDigit1.setProperty(u"value", 0.000000000000000)
        self.hexDigit1.setProperty(u"intValue", 0)
        self.hexDigit2 = QLCDNumber(self.hexDisplayGroup)
        self.hexDigit2.setObjectName(u"hexDigit2")
        self.hexDigit2.setGeometry(QRect(160, 0, 43, 95))
        self.hexDigit2.setStyleSheet(u"QLCDNumber {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: red;\n"
"}")
        self.hexDigit2.setDigitCount(1)
        self.hexDigit2.setMode(QLCDNumber.Mode.Hex)
        self.hexDigit2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.hexDigit2.setProperty(u"value", 0.000000000000000)
        self.hexDigit2.setProperty(u"intValue", 0)
        self.hexDigit3 = QLCDNumber(self.hexDisplayGroup)
        self.hexDigit3.setObjectName(u"hexDigit3")
        self.hexDigit3.setGeometry(QRect(200, 0, 43, 95))
        self.hexDigit3.setStyleSheet(u"QLCDNumber {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: red;\n"
"}")
        self.hexDigit3.setDigitCount(1)
        self.hexDigit3.setMode(QLCDNumber.Mode.Hex)
        self.hexDigit3.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.hexDigit3.setProperty(u"value", 0.000000000000000)
        self.hexDigit3.setProperty(u"intValue", 0)
        self.decimalPoint = QLabel(self.hexDisplayGroup)
        self.decimalPoint.setObjectName(u"decimalPoint")
        self.decimalPoint.setGeometry(QRect(142, 10, 16, 69))
        font16 = QFont()
        font16.setPointSize(60)
        self.decimalPoint.setFont(font16)
        self.decimalPoint.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: red;\n"
"}")
        self.eCodeLineEdit = QLineEdit(self.sysFrame)
        self.eCodeLineEdit.setObjectName(u"eCodeLineEdit")
        self.eCodeLineEdit.setGeometry(QRect(553, 117, 256, 22))
        self.eCodeLineEdit.setFont(font8)
        self.eCodeLineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: #FFE200;\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.eCodeLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.miscTable = QTableWidget(self.sysFrame)
        if (self.miscTable.columnCount() < 2):
            self.miscTable.setColumnCount(2)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.miscTable.setHorizontalHeaderItem(0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.miscTable.setHorizontalHeaderItem(1, __qtablewidgetitem97)
        self.miscTable.setObjectName(u"miscTable")
        self.miscTable.setGeometry(QRect(15, 14, 241, 94))
        self.miscTable.setFont(font8)
        self.miscTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.miscTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #6FDD8E;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.miscTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.miscTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.miscTable.setAutoScroll(False)
        self.miscTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.miscTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.miscTable.horizontalHeader().setVisible(False)
        self.miscTable.horizontalHeader().setMinimumSectionSize(80)
        self.miscTable.horizontalHeader().setDefaultSectionSize(120)
        self.miscTable.horizontalHeader().setStretchLastSection(False)
        self.miscTable.verticalHeader().setVisible(False)
        self.miscTable.verticalHeader().setMinimumSectionSize(16)
        self.miscTable.verticalHeader().setDefaultSectionSize(18)
        self.opModeBox = QComboBox(self.sysFrame)
        self.opModeBox.setObjectName(u"opModeBox")
        self.opModeBox.setGeometry(QRect(15, 117, 152, 21))
        self.opModeBox.setFont(font8)
        self.opModeBox.setStyleSheet(u"QComboBox{\n"
"    color: #000000; /* Text color */\n"
"    background-color: #FFFFFF; /* Background color */\n"
"    border: 1px solid black; /* Thin black solid border */\n"
"    border-radius: 5px; /* Optional: rounded corners */\n"
"    padding: 5px; /* Adds space around the text */\n"
"    padding-top: 3px; /* Adjusts the padding at the top */\n"
"    padding-bottom: 3px; /* Adjusts the padding at the bottom */\n"
"    line-height: 20px; /* Ensures proper vertical alignment of text */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: #000000; /* Text color for drop-down items */\n"
"	background-color: #FFFFFF; /* Background color for drop-down items */\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: none;\n"
"}")
        self.setOpModeButton = QPushButton(self.sysFrame)
        self.setOpModeButton.setObjectName(u"setOpModeButton")
        self.setOpModeButton.setGeometry(QRect(178, 117, 78, 21))
        self.setOpModeButton.setFont(font13)
        self.setOpModeButton.setStyleSheet(u"QPushButton {\n"
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
        self.clearFaultButton = QPushButton(self.sysFrame)
        self.clearFaultButton.setObjectName(u"clearFaultButton")
        self.clearFaultButton.setGeometry(QRect(335, 100, 54, 26))
        self.clearFaultButton.setFont(font3)
        self.clearFaultButton.setStyleSheet(u"QPushButton {\n"
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
        self.assertTable = QTableWidget(self.sysFrame)
        if (self.assertTable.columnCount() < 2):
            self.assertTable.setColumnCount(2)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.assertTable.setHorizontalHeaderItem(0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.assertTable.setHorizontalHeaderItem(1, __qtablewidgetitem99)
        self.assertTable.setObjectName(u"assertTable")
        self.assertTable.setGeometry(QRect(270, 14, 241, 74))
        self.assertTable.setFont(font8)
        self.assertTable.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.assertTable.setStyleSheet(u"QTableWidget {\n"
"    border: 2px solid black;\n"
"	background: #E6E2BE;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #6FDD8E;\n"
"    border: none;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 2px solid black;\n"
"    color: black;\n"
"}")
        self.assertTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.assertTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.assertTable.setAutoScroll(False)
        self.assertTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.assertTable.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.assertTable.horizontalHeader().setVisible(False)
        self.assertTable.horizontalHeader().setMinimumSectionSize(10)
        self.assertTable.horizontalHeader().setDefaultSectionSize(120)
        self.assertTable.horizontalHeader().setStretchLastSection(False)
        self.assertTable.verticalHeader().setVisible(False)
        self.assertTable.verticalHeader().setMinimumSectionSize(16)
        self.assertTable.verticalHeader().setDefaultSectionSize(18)
        self.clearAssertButton = QPushButton(self.sysFrame)
        self.clearAssertButton.setObjectName(u"clearAssertButton")
        self.clearAssertButton.setGeometry(QRect(394, 100, 54, 26))
        self.clearAssertButton.setFont(font3)
        self.clearAssertButton.setStyleSheet(u"QPushButton {\n"
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.consoleTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metrics", None))
        self.ADCIOPageButton.setText(QCoreApplication.translate("MainWindow", u"ADC/IO", None))
        self.swivelPageButton.setText(QCoreApplication.translate("MainWindow", u"Swivel\n"
"Drive", None))
        self.configurationPageButton.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.railMappingPageButton.setText(QCoreApplication.translate("MainWindow", u"Rail \n"
" Map", None))
        self.metricsVersionText.setText(QCoreApplication.translate("MainWindow", u"VX.X.X", None))
        self.carriageLeftCallButton.setText(QCoreApplication.translate("MainWindow", u"Carriage\n"
"Left", None))
        self.footrestUnfoldCallButton.setText(QCoreApplication.translate("MainWindow", u"Footrest\n"
"Unfold", None))
        self.swivelLeftCallButton.setText(QCoreApplication.translate("MainWindow", u"Swivel\n"
"Left", None))
        self.chairFoldCallButton.setText(QCoreApplication.translate("MainWindow", u"Chair\n"
"Fold", None))
        self.swivelRightCallButton.setText(QCoreApplication.translate("MainWindow", u"Swivel\n"
"Right", None))
        self.chairPartFoldCallButton.setText(QCoreApplication.translate("MainWindow", u"Chair\n"
"Partial\n"
"Fold", None))
        self.footrestFoldCallButton.setText(QCoreApplication.translate("MainWindow", u"Footrest\n"
"Fold", None))
        self.carriageRightCallButton.setText(QCoreApplication.translate("MainWindow", u"Carriage\n"
"Right", None))
        self.swivelCentreCallButton.setText(QCoreApplication.translate("MainWindow", u"Swivel\n"
"Centre", None))
        self.chairUnfoldCallButton.setText(QCoreApplication.translate("MainWindow", u"Chair\n"
"Unfold", None))
        self.localLeftCallButton.setText(QCoreApplication.translate("MainWindow", u"Local\n"
"Left", None))
        self.localRightCallButton.setText(QCoreApplication.translate("MainWindow", u"Local\n"
"Right", None))
        self.remoteUpCallButton.setText(QCoreApplication.translate("MainWindow", u"Remote\n"
"Up", None))
        self.remoteDownCallButton.setText(QCoreApplication.translate("MainWindow", u"Remote\n"
"Down", None))
        self.repeatCallButton.setText(QCoreApplication.translate("MainWindow", u"Click to repeat a call", None))
        self.carriageDownCallButton.setText(QCoreApplication.translate("MainWindow", u"Carriage\n"
"Down", None))
        self.carriageUpCallButton.setText(QCoreApplication.translate("MainWindow", u"Carriage\n"
"Up", None))
        self.noCallButton.setText(QCoreApplication.translate("MainWindow", u"No\n"
"Call", None))
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
        self.chairFoldPageButton.setText(QCoreApplication.translate("MainWindow", u"Chair\n"
"Drive", None))
        self.footrestPageButton.setText(QCoreApplication.translate("MainWindow", u"Footrest\n"
"Drive", None))
        self.mainDrivePageButton.setText(QCoreApplication.translate("MainWindow", u"Main\n"
"Drive", None))
        self.systemPageButton.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.keyWiringPageButton.setText(QCoreApplication.translate("MainWindow", u"Key \n"
" Wiring", None))
        self.debuggingPageButton.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.callAndDemandPageButton.setText(QCoreApplication.translate("MainWindow", u"Call\n"
"Demand", None))
        self.enableDemoModeButton.setText(QCoreApplication.translate("MainWindow", u"Enable Demo Mode", None))
        self.x06PageButton.setText(QCoreApplication.translate("MainWindow", u"X06", None))
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
        self.callDetectionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Call Detection", None))
        ___qtablewidgetitem13 = self.callDetectionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem14 = self.callDetectionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.demandProcessorGroup.setTitle(QCoreApplication.translate("MainWindow", u"Demand Processor", None))
        ___qtablewidgetitem15 = self.demandProcessorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem16 = self.demandProcessorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.testColourLog.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        ___qtablewidgetitem17 = self.testTable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem18 = self.testTable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.bgDefButton.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.configBox.setTitle(QCoreApplication.translate("MainWindow", u"Stored Configuration", None))
        ___qtablewidgetitem19 = self.configTable.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem20 = self.configTable.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Record", None));
        ___qtablewidgetitem21 = self.configTable.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem22 = self.configTable.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        self.loadConfigButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.alterConfigButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.restoreConfigButton.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.resetConfigButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.confirmRestoreButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.saveConfigButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.injectConfigButton.setText(QCoreApplication.translate("MainWindow", u"Inject", None))
        self.sdCardBox.setTitle(QCoreApplication.translate("MainWindow", u"SD Card", None))
        self.eraseSDCardButton.setText(QCoreApplication.translate("MainWindow", u"Erase", None))
        self.sdCardTextEdit.setText(QCoreApplication.translate("MainWindow", u"SD Card Files Present", None))
        self.confirmEraseButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.debugGroup1.setTitle(QCoreApplication.translate("MainWindow", u"Debug Table 1", None))
        ___qtablewidgetitem23 = self.debugTable1.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem24 = self.debugTable1.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.debugGroup2.setTitle(QCoreApplication.translate("MainWindow", u"Debug Table 2", None))
        ___qtablewidgetitem25 = self.debugTable2.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem26 = self.debugTable2.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.debugGroup3.setTitle(QCoreApplication.translate("MainWindow", u"Debug Table 3", None))
        ___qtablewidgetitem27 = self.debugTable3.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem28 = self.debugTable3.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.debugGroup4.setTitle(QCoreApplication.translate("MainWindow", u"Debug Table 4", None))
        ___qtablewidgetitem29 = self.debugTable4.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem30 = self.debugTable4.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.debugGroup6.setTitle(QCoreApplication.translate("MainWindow", u"Debug Table 6", None))
        ___qtablewidgetitem31 = self.debugTable6.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem32 = self.debugTable6.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.debugGroup5.setTitle(QCoreApplication.translate("MainWindow", u"Debug Table 5", None))
        ___qtablewidgetitem33 = self.debugTable5.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem34 = self.debugTable5.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.rightStopLED.setText("")
        self.rightSafetyLED.setText("")
        self.callDownLabel.setText(QCoreApplication.translate("MainWindow", u"Call Down", None))
        self.leftFootrestLED.setText("")
        self.leftSkateLED.setText("")
        self.leftSafetyLED.setText("")
        self.handing4Label.setText(QCoreApplication.translate("MainWindow", u"Handing 4", None))
        self.leftSkateLabel.setText(QCoreApplication.translate("MainWindow", u"Left Skate", None))
        self.osgReturnLED.setText("")
        self.osgReturnLabel.setText(QCoreApplication.translate("MainWindow", u"OSG \n"
"Return", None))
        self.callUpLED.setText("")
        self.handing2LED.setText("")
        self.bistableReturnLabel.setText(QCoreApplication.translate("MainWindow", u"Bistable \n"
"Return", None))
        self.ultimateLabel.setText(QCoreApplication.translate("MainWindow", u"Ultimate", None))
        self.bottomFootrestLED.setText("")
        self.rightFootrestLED.setText("")
        self.ultimateLED.setText("")
        self.relayCoilMonitorLabel.setText(QCoreApplication.translate("MainWindow", u"Relay Coil Monitor", None))
        self.leftSafetyLabel.setText(QCoreApplication.translate("MainWindow", u"Left Safety", None))
        self.callUpLabel.setText(QCoreApplication.translate("MainWindow", u"Call Up", None))
        self.rightSafetyLabel.setText(QCoreApplication.translate("MainWindow", u"Right Safety", None))
        self.swivelOverrideLabel.setText(QCoreApplication.translate("MainWindow", u"Swivel \n"
"Override", None))
        self.leftFootrestLabel.setText(QCoreApplication.translate("MainWindow", u"Left Footrest", None))
        self.bistableReturnLED.setText("")
        self.handing4LED.setText("")
        self.bistableFeedLabel.setText(QCoreApplication.translate("MainWindow", u"Bistable \n"
"Feed", None))
        self.rightSkateLED.setText("")
        self.rightStopLabel.setText(QCoreApplication.translate("MainWindow", u"Right Stop", None))
        self.bistableFeedLED.setText("")
        self.handing2Label.setText(QCoreApplication.translate("MainWindow", u"Handing 2", None))
        self.callDownLED.setText("")
        self.leftStopLED.setText("")
        self.leftStopLabel.setText(QCoreApplication.translate("MainWindow", u"Left Stop", None))
        self.bottomFootrestLabel.setText(QCoreApplication.translate("MainWindow", u"Bottom \n"
" Footrest", None))
        self.rightSkateLabel.setText(QCoreApplication.translate("MainWindow", u"Right Skate", None))
        self.rightFootrestLabel.setText(QCoreApplication.translate("MainWindow", u"Right Footrest", None))
        self.relayCoilMonitorLED.setText("")
        self.swivelOverrideLED.setText("")
        self.handingLink4.setText("")
        self.handingLinkLabel3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.handingLinkLabel2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.handingLink3.setText("")
        self.handingLinkLabel5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.handingLinkLabel4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.handingLink5.setText("")
        self.handingLinkLabel1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.handingLink1.setText("")
        self.handingLink4_2.setText("")
        self.handingLinkLabel3_2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.handingLinkLabel2_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.handingLink3_2.setText("")
        self.handingLinkLabel5_2.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.handingLinkLabel4_2.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.handingLink5_2.setText("")
        self.handingLink2_2.setText("")
        self.handingLinkJoin.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For LH Stairlift, link 2-3 and 4-5.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For RH Stairlift, link 1-2 and 3-4.</p></body></html>", None))
        self.railMapBox.setTitle(QCoreApplication.translate("MainWindow", u"Rail Mapping", None))
        ___qtablewidgetitem35 = self.mapPointsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem36 = self.mapPointsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem37 = self.mapPointsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        self.mainMapModeGroup.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.modeRemoteDButton.setText(QCoreApplication.translate("MainWindow", u"Remote Control D", None))
        self.modePartialUnfoldButton.setText(QCoreApplication.translate("MainWindow", u"Partial Unfold Zone", None))
        self.modeHalfSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Half Speed Zone", None))
        self.modeRemoteBButton.setText(QCoreApplication.translate("MainWindow", u"Remote Control B", None))
        self.modeRemoteCButton.setText(QCoreApplication.translate("MainWindow", u"Remote Control C", None))
        self.modeSwivelRightButton.setText(QCoreApplication.translate("MainWindow", u"Swivel Right Enabled", None))
        self.modeRemoteAButton.setText(QCoreApplication.translate("MainWindow", u"Remote Control A", None))
        self.modeUnpackButton.setText(QCoreApplication.translate("MainWindow", u"Unpack on Arrival", None))
        self.modeFullSwivelButton.setText(QCoreApplication.translate("MainWindow", u"Full Swivel Angle", None))
        self.modeParkingPointButton.setText(QCoreApplication.translate("MainWindow", u"Parking", None))
        self.modeSwivelLeftButton.setText(QCoreApplication.translate("MainWindow", u"Swivel Left Enabled", None))
        self.modeBoardingPointButton.setText(QCoreApplication.translate("MainWindow", u"Boarding", None))
        self.updatePointButton.setText(QCoreApplication.translate("MainWindow", u"Update Point", None))
        self.modeEnabledButton.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.zoneWidthText.setText("")
        self.zoneWidthLabel.setText(QCoreApplication.translate("MainWindow", u"Zone Width (mm)", None))
        self.newPointPositionText.setText("")
        self.pointPositionLabel.setText(QCoreApplication.translate("MainWindow", u"Point Position", None))
        self.copyPositionButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.mainCurrentPointGroup.setTitle(QCoreApplication.translate("MainWindow", u"Current Point", None))
        self.leftStopButton.setText(QCoreApplication.translate("MainWindow", u"Left Stop", None))
        self.middleStopButton.setText(QCoreApplication.translate("MainWindow", u"Middle Stop", None))
        self.rightStopButton.setText(QCoreApplication.translate("MainWindow", u"Right Stop", None))
        self.parkPointButton.setText(QCoreApplication.translate("MainWindow", u"Park Point", None))
        self.partialUnfoldLeftButton.setText(QCoreApplication.translate("MainWindow", u"Partial Unfold to Left", None))
        self.halfSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Half Speed Zone", None))
        self.partialUnfoldRightButton.setText(QCoreApplication.translate("MainWindow", u"Partial Unfold to Right", None))
        self.partialUnfoldZoneButton.setText(QCoreApplication.translate("MainWindow", u"Partial Unfold Zone", None))
        self.swivelFullAngleButton.setText(QCoreApplication.translate("MainWindow", u"Swivel Full Angle", None))
        self.swivelLeftButton.setText(QCoreApplication.translate("MainWindow", u"Swivel Left Allowed", None))
        self.unpackArrivalButton.setText(QCoreApplication.translate("MainWindow", u"Unpack on Arrival", None))
        self.swivelRightButton.setText(QCoreApplication.translate("MainWindow", u"Swivel Right Allowed", None))
        self.mainCalibrationGroup.setTitle(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.autoMainCalButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualMainCalButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.startMainCalButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.acceptMainCalButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.rejectMainCalButton.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
        self.mainNewPositionText.setText("")
        self.setPositionButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.zeroPositionButton.setText(QCoreApplication.translate("MainWindow", u"Zero", None))
        ___qtablewidgetitem38 = self.mapDataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem39 = self.mapDataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.saveMapFileButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.injectMapButton.setText(QCoreApplication.translate("MainWindow", u"Inject", None))
        self.mainPointGroup_2.setTitle(QCoreApplication.translate("MainWindow", u"Map Control", None))
        self.wipeMapButton.setText(QCoreApplication.translate("MainWindow", u"Wipe \n"
" Map", None))
        self.deleteMapPoint.setText(QCoreApplication.translate("MainWindow", u"Delete \n"
" Point", None))
        self.saveMapButton.setText(QCoreApplication.translate("MainWindow", u"Save \n"
" Map", None))
        self.disableModeButton.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.editModeButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.confirmWipeMapButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.findModeButton.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.confirmDeletePointButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.loadMapButton.setText(QCoreApplication.translate("MainWindow", u"Load \n"
" Map", None))
        self.restrictModeButton.setText(QCoreApplication.translate("MainWindow", u"Restrict", None))
        self.mainPointGroup.setTitle(QCoreApplication.translate("MainWindow", u"Add Points", None))
        self.boardingPointButton.setText(QCoreApplication.translate("MainWindow", u"Boarding \n"
" Point", None))
        self.partFoldPointButton.setText(QCoreApplication.translate("MainWindow", u"Partial \n"
" Unfold", None))
        self.parkingPointButton.setText(QCoreApplication.translate("MainWindow", u"Parking \n"
" Point", None))
        self.halfSpeedPointButton.setText(QCoreApplication.translate("MainWindow", u"Half \n"
" Speed", None))
        self.positionToSpecifyText.setText("")
        self.specifyPositionButton.setText(QCoreApplication.translate("MainWindow", u"Specify Position", None))
        self.mainLocatingGroup.setTitle(QCoreApplication.translate("MainWindow", u"Position Locating", None))
        self.findLeftPosButton.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.findBothPosButton.setText(QCoreApplication.translate("MainWindow", u"Both", None))
        self.findRightPosButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.locateBoardingButton.setText(QCoreApplication.translate("MainWindow", u"Boarding \n"
" Point", None))
        self.locateParkingButton.setText(QCoreApplication.translate("MainWindow", u"Parking \n"
" Point", None))
        self.locateRemoteAButton.setText(QCoreApplication.translate("MainWindow", u"Remote\n"
"A", None))
        self.locateRemoteBButton.setText(QCoreApplication.translate("MainWindow", u"Remote\n"
"B", None))
        self.locateRemoteCButton.setText(QCoreApplication.translate("MainWindow", u"Remote\n"
"C", None))
        self.locateRemoteDButton.setText(QCoreApplication.translate("MainWindow", u"Remote\n"
"D", None))
        self.locateNextRailButton.setText(QCoreApplication.translate("MainWindow", u"Next\n"
"Rail", None))
        self.clearMapTableButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.sysVersionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Version", None))
        self.requestSystemVersionButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        ___qtablewidgetitem40 = self.sysVerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem41 = self.sysVerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.timeGroup.setTitle(QCoreApplication.translate("MainWindow", u"RTC", None))
        self.setRTCButton.setText(QCoreApplication.translate("MainWindow", u"Set RTC", None))
        ___qtablewidgetitem42 = self.timeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem43 = self.timeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.chairDrivePositionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        ___qtablewidgetitem44 = self.chairDrivePositionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem45 = self.chairDrivePositionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.requestChairPositionButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.chairDriveControlGroup.setTitle(QCoreApplication.translate("MainWindow", u"Drive Control", None))
        self.plotChairButton.setText(QCoreApplication.translate("MainWindow", u"Start Plot", None))
        ___qtablewidgetitem46 = self.chairPIDPosTable.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem47 = self.chairPIDPosTable.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem48 = self.chairPIDPosTable.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        ___qtablewidgetitem49 = self.chairPIDSpeedTable.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem50 = self.chairPIDSpeedTable.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem51 = self.chairPIDSpeedTable.horizontalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        self.enableChairSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Enable Speed Control", None))
        self.requestChairTuningButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.copyChairTuningButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.alterChairTuningButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.autoChairPlotButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualChairPlotButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.openChairPlotButton.setText(QCoreApplication.translate("MainWindow", u"Open Plot", None))
        ___qtablewidgetitem52 = self.chairDriveControlTable.horizontalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem53 = self.chairDriveControlTable.horizontalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem54 = self.chairDriveControlTable.horizontalHeaderItem(2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.requestChairLoggingButton.setText(QCoreApplication.translate("MainWindow", u"HS Request", None))
        self.chairFolder.setText(QCoreApplication.translate("MainWindow", u"No Folder Selected", None))
        self.selectChairFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.resetChairTuningButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.chairFoldTuneButton.setText(QCoreApplication.translate("MainWindow", u"Fold", None))
        self.chairPartFoldTuneButton.setText(QCoreApplication.translate("MainWindow", u"Part Fold", None))
        self.chairUnfoldTuneButton.setText(QCoreApplication.translate("MainWindow", u"Unfold", None))
        self.chairPlottingLabel.setText(QCoreApplication.translate("MainWindow", u"Plotting State:", None))
        self.chairHSLabel.setText(QCoreApplication.translate("MainWindow", u"High Speed State:", None))
        self.chairLoggingLabel.setText(QCoreApplication.translate("MainWindow", u"Logging State:", None))
        self.chairHSState.setText(QCoreApplication.translate("MainWindow", u"HS Logging Disabled", None))
        self.chairLoggingState.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.chairPlottingState.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.chairHBridgeGroup.setTitle(QCoreApplication.translate("MainWindow", u"H Bridge", None))
        self.chairLeftBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.chairRightBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.chairHoldRightDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.chairHoldLeftDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.maxChairPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.maxChairPWM.setText(QCoreApplication.translate("MainWindow", u"980", None))
        self.minChairPWM.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.minChairPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.enableChairBridgeButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.chairStateMachineGroup.setTitle(QCoreApplication.translate("MainWindow", u"State Machine", None))
        ___qtablewidgetitem55 = self.chairStateMachineTable.horizontalHeaderItem(0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem56 = self.chairStateMachineTable.horizontalHeaderItem(1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.chairCalibrationGroup.setTitle(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.autoChairCalButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualChairCalButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.startChairCalButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.acceptChairCalButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.rejectChairCalButton.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
        self.footrestDriveControlGroup.setTitle(QCoreApplication.translate("MainWindow", u"Drive Control", None))
        ___qtablewidgetitem57 = self.footrestDriveControlTable.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem58 = self.footrestDriveControlTable.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem59 = self.footrestDriveControlTable.horizontalHeaderItem(2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.plotFootrestButton.setText(QCoreApplication.translate("MainWindow", u"Start Plot", None))
        ___qtablewidgetitem60 = self.footrestPIDPosTable.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem61 = self.footrestPIDPosTable.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem62 = self.footrestPIDPosTable.horizontalHeaderItem(2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        ___qtablewidgetitem63 = self.footrestPIDSpeedTable.horizontalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem64 = self.footrestPIDSpeedTable.horizontalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem65 = self.footrestPIDSpeedTable.horizontalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        self.enableFootrestSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Enable Speed Control", None))
        self.requestFootrestTuningButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.copyFootrestTuningButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.alterFootrestTuningButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.autoFootrestPlotButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualFootrestPlotButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.openFootrestPlotButton.setText(QCoreApplication.translate("MainWindow", u"Open Plot", None))
        self.requestFootrestLoggingButton.setText(QCoreApplication.translate("MainWindow", u"HS Request", None))
        self.footrestFolder.setText(QCoreApplication.translate("MainWindow", u"No Folder Selected", None))
        self.selectFootrestFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.resetFootrestTuningButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.footrestFoldTuneButton.setText(QCoreApplication.translate("MainWindow", u"Fold", None))
        self.footrestUnfoldTuneButton.setText(QCoreApplication.translate("MainWindow", u"Unfold", None))
        self.footrestPlottingLabel.setText(QCoreApplication.translate("MainWindow", u"Plotting State:", None))
        self.footrestHSLabel.setText(QCoreApplication.translate("MainWindow", u"High Speed State:", None))
        self.footrestLoggingLabel.setText(QCoreApplication.translate("MainWindow", u"Logging State:", None))
        self.footrestHSState.setText(QCoreApplication.translate("MainWindow", u"HS Logging Disabled", None))
        self.footrestLoggingState.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.footrestPlottingState.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.footrestDrivePositionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        ___qtablewidgetitem66 = self.footrestDrivePositionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem67 = self.footrestDrivePositionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.requestFootrestPositionButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.footrestHBridgeGroup.setTitle(QCoreApplication.translate("MainWindow", u"H Bridge", None))
        self.footrestLeftBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.footrestRightBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.footrestHoldRightDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.footrestHoldLeftDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.maxFootrestPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.maxFootrestPWM.setText(QCoreApplication.translate("MainWindow", u"980", None))
        self.minFootrestPWM.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.minFootrestPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.enableFootrestBridgeButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.footrestStateMachineGroup.setTitle(QCoreApplication.translate("MainWindow", u"State Machine", None))
        ___qtablewidgetitem68 = self.footrestStateMachineTable.horizontalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem69 = self.footrestStateMachineTable.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.footrestCalibrationGroup.setTitle(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.autoFootrestCalButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualFootrestCalButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.startFootrestCalButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.acceptFootrestCalButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.rejectFootrestCalButton.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
        self.mainStateMachineGroup.setTitle(QCoreApplication.translate("MainWindow", u"State Machine", None))
        ___qtablewidgetitem70 = self.mainStateMachineTable.horizontalHeaderItem(0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem71 = self.mainStateMachineTable.horizontalHeaderItem(1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.mainHBridgeGroup.setTitle(QCoreApplication.translate("MainWindow", u"H Bridge", None))
        self.mainLeftBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.mainRightBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.mainHoldRightDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.mainHoldLeftDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.maxMainPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.maxMainPWM.setText(QCoreApplication.translate("MainWindow", u"980", None))
        self.minMainPWM.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.minMainPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.enableMainBridgeButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.mainDriveControlGroup.setTitle(QCoreApplication.translate("MainWindow", u"Drive Control", None))
        ___qtablewidgetitem72 = self.mainDriveControlTable.horizontalHeaderItem(0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem73 = self.mainDriveControlTable.horizontalHeaderItem(1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem74 = self.mainDriveControlTable.horizontalHeaderItem(2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.plotMainButton.setText(QCoreApplication.translate("MainWindow", u"Start Plot", None))
        ___qtablewidgetitem75 = self.mainPIDPosTable.horizontalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem76 = self.mainPIDPosTable.horizontalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem77 = self.mainPIDPosTable.horizontalHeaderItem(2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        ___qtablewidgetitem78 = self.mainPIDSpeedTable.horizontalHeaderItem(0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem79 = self.mainPIDSpeedTable.horizontalHeaderItem(1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem80 = self.mainPIDSpeedTable.horizontalHeaderItem(2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        self.enableMainSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Enable Speed Control", None))
        self.requestMainTuningButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.copyMainTuningButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.alterMainTuningButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.autoMainPlotButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualMainPlotButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.openMainPlotButton.setText(QCoreApplication.translate("MainWindow", u"Open Plot", None))
        self.requestMainLoggingButton.setText(QCoreApplication.translate("MainWindow", u"HS Request", None))
        self.selectMainFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.mainFolder.setText(QCoreApplication.translate("MainWindow", u"No Folder Selected", None))
        self.resetMainTuningButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.mainHSLabel.setText(QCoreApplication.translate("MainWindow", u"High Speed State:", None))
        self.mainPlottingLabel.setText(QCoreApplication.translate("MainWindow", u"Plotting State:", None))
        self.mainLoggingState.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.mainHSState.setText(QCoreApplication.translate("MainWindow", u"HS Logging Disabled", None))
        self.mainLoggingLabel.setText(QCoreApplication.translate("MainWindow", u"Logging State:", None))
        self.mainPlottingState.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.mainDrivePositionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        ___qtablewidgetitem81 = self.mainDrivePositionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem82 = self.mainDrivePositionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.requestMainPositionButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.swivelDrivePositionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        ___qtablewidgetitem83 = self.swivelDrivePositionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem84 = self.swivelDrivePositionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.requestSwivelPositionButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.swivelCalibrationGroup.setTitle(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.autoSwivelCalButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualSwivelCalButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.startSwivelCalButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.acceptSwivelCalButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.rejectSwivelCalButton.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
        self.swivelDriveControlGroup.setTitle(QCoreApplication.translate("MainWindow", u"Drive Control", None))
        ___qtablewidgetitem85 = self.swivelDriveControlTable.horizontalHeaderItem(0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem86 = self.swivelDriveControlTable.horizontalHeaderItem(1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem87 = self.swivelDriveControlTable.horizontalHeaderItem(2)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.plotSwivelButton.setText(QCoreApplication.translate("MainWindow", u"Start Plot", None))
        ___qtablewidgetitem88 = self.swivelPIDPosTable.horizontalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem89 = self.swivelPIDPosTable.horizontalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem90 = self.swivelPIDPosTable.horizontalHeaderItem(2)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        ___qtablewidgetitem91 = self.swivelPIDSpeedTable.horizontalHeaderItem(0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Term", None));
        ___qtablewidgetitem92 = self.swivelPIDSpeedTable.horizontalHeaderItem(1)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem93 = self.swivelPIDSpeedTable.horizontalHeaderItem(2)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Alter", None));
        self.enableSwivelSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Enable Speed Control", None))
        self.requestSwivelTuningButton.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.copySwivelTuningButton.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.alterSwivelTuningButton.setText(QCoreApplication.translate("MainWindow", u"Alter", None))
        self.autoSwivelPlotButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.manualSwivelPlotButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.openSwivelPlotButton.setText(QCoreApplication.translate("MainWindow", u"Open Plot", None))
        self.requestSwivelLoggingButton.setText(QCoreApplication.translate("MainWindow", u"HS Request", None))
        self.selectSwivelFolderButton.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.swivelFolder.setText(QCoreApplication.translate("MainWindow", u"No Folder Selected", None))
        self.resetSwivelTuningButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.swivelLeftTuneButton.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.swivelRightTuneButton.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.swivelHSLabel.setText(QCoreApplication.translate("MainWindow", u"High Speed State:", None))
        self.swivelPlottingLabel.setText(QCoreApplication.translate("MainWindow", u"Plotting State:", None))
        self.swivelLoggingState.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.swivelHSState.setText(QCoreApplication.translate("MainWindow", u"HS Logging Disabled", None))
        self.swivelLoggingLabel.setText(QCoreApplication.translate("MainWindow", u"Logging State:", None))
        self.swivelPlottingState.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.swivelHBridgeGroup.setTitle(QCoreApplication.translate("MainWindow", u"H Bridge", None))
        self.swivelLeftBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.swivelRightBridgeText.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.swivelHoldRightDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.swivelHoldLeftDutyButton.setText(QCoreApplication.translate("MainWindow", u"Hold", None))
        self.maxSwivelPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.maxSwivelPWM.setText(QCoreApplication.translate("MainWindow", u"980", None))
        self.minSwivelPWM.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.minSwivelPWMLabel.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.enableSwivelBridgeButton.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.swivelStateMachineGroup.setTitle(QCoreApplication.translate("MainWindow", u"State Machine", None))
        ___qtablewidgetitem94 = self.swivelStateMachineTable.horizontalHeaderItem(0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem95 = self.swivelStateMachineTable.horizontalHeaderItem(1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.enableX06MessagesButton.setText(QCoreApplication.translate("MainWindow", u"Enable X06 Messages", None))
        self.clearPrimaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.savePrimaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.consoleTab.setTabText(self.consoleTab.indexOf(self.primaryTab), QCoreApplication.translate("MainWindow", u"X04", None))
        self.saveSecondaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.clearSecondaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.consoleTab.setTabText(self.consoleTab.indexOf(self.secondaryTab), QCoreApplication.translate("MainWindow", u"X01", None))
        self.clearTertiaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.saveTertiaryConsoleButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.consoleTab.setTabText(self.consoleTab.indexOf(self.tertiaryTab), QCoreApplication.translate("MainWindow", u"Debug", None))
        self.hexDisplayGroup.setTitle("")
        self.decimalPoint.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.eCodeLineEdit.setText(QCoreApplication.translate("MainWindow", u"NO ERROR", None))
        ___qtablewidgetitem96 = self.miscTable.horizontalHeaderItem(0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem97 = self.miscTable.horizontalHeaderItem(1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.setOpModeButton.setText(QCoreApplication.translate("MainWindow", u"Set Mode", None))
        self.clearFaultButton.setText(QCoreApplication.translate("MainWindow", u"Clear \n"
" Fault", None))
        ___qtablewidgetitem98 = self.assertTable.horizontalHeaderItem(0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem99 = self.assertTable.horizontalHeaderItem(1)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.clearAssertButton.setText(QCoreApplication.translate("MainWindow", u"Clear\n"
"Assert", None))
    # retranslateUi

