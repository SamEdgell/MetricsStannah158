# Standard library imports.
import multiprocessing
import os

# Third party imports.
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QFileDialog, QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_drive_control import DriveControlDir
from Enums.enum_high_speed import HighSpeedSources
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from Enums.enum_pid import PID
from Enums.enum_system_drives import SystemDrive
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours
from Utilities.logger import Logger
from Utilities.messages import unpackMessagePartial, unpackMessagePayload
from Utilities.plotter import createPlot


class UIPID:
    """
    Class for handling all aspects of PID data.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        # Chair attributes - PID.
        self.main_window.ui.requestChairLoggingButton.clicked.connect(lambda:    self.requestHSLogging("Chair"))
        self.main_window.ui.autoChairPlotButton.clicked.connect(lambda:          self.updatePlotMode("Chair", True))
        self.main_window.ui.manualChairPlotButton.clicked.connect(lambda:        self.updatePlotMode("Chair", False))
        self.main_window.ui.plotChairButton.clicked.connect(lambda:              self.plotData("Chair"))
        self.main_window.ui.openChairPlotButton.clicked.connect(lambda:          self.openPlot("Chair"))
        self.main_window.ui.selectChairFolderButton.clicked.connect(lambda:      self.selectPIDFolder("Chair"))

        self.main_window.ui.plotChairButton.setEnabled(False)    # Button is disabled by default until a folder is created.
        self.main_window.ui.openChairPlotButton.setEnabled(False)    # Button is disabled by default until a plot is created.

        # Chair attributes - Tuning.
        self.main_window.ui.chairFoldTuneButton.clicked.connect(lambda:          self.updateTuningDirection("Chair"))
        self.main_window.ui.chairPartFoldTuneButton.clicked.connect(lambda:      self.updateTuningDirection("Chair"))
        self.main_window.ui.chairUnfoldTuneButton.clicked.connect(lambda:        self.updateTuningDirection("Chair"))
        self.main_window.ui.alterChairTuningButton.clicked.connect(lambda:       self.alterTuningData("Chair"))
        self.main_window.ui.copyChairTuningButton.clicked.connect(lambda:        self.copyTuningData("Chair"))
        self.main_window.ui.requestChairTuningButton.clicked.connect(lambda:     self.requestTuningData("Chair"))
        self.main_window.ui.resetChairTuningButton.clicked.connect(lambda:       self.resetAlteredData("Chair"))

        delegateChairDriveControl = Painter()
        delegateChairPosTune = Painter()
        delegateChairSpeedTune = Painter()
        self.main_window.ui.chairDriveControlTable.setItemDelegate(delegateChairDriveControl)
        self.main_window.ui.chairPIDPosTable.setItemDelegate(delegateChairPosTune)
        self.main_window.ui.chairPIDSpeedTable.setItemDelegate(delegateChairSpeedTune)

        self.chairHSLogging = False
        self.autoChairPlot = False
        self.manualChairPlot = True

        self.chairCurrentLogFile = None         # Last current log file created.
        self.chairPlottingActive = False        # Flag to indicate if the plot is active.
        self.chairPlottingFileClosed = True     # Flag to indicate if the plot file is closed (To prevent multiple closures).

        self.chairLogger = Logger("CH_PIDData")
        self.chairLogger.columns = "driveId:0, tickMs:0, currentPosition, targetPosition, currentSpeed, targetSpeed, error:4, integral:2, derivative:0, speedError:4, speedIntegral:2, sppedDerivative:0, kpTerm:3, kiTerm:3, kdTerm:3, kffTerm:3, kPSpeedTerm:3, kISpeedTerm:3, kDSpeedTerm:3, output:3, current:3"


        # Footrest attributes - PID.
        self.main_window.ui.requestFootrestLoggingButton.clicked.connect(lambda: self.requestHSLogging("Footrest"))
        self.main_window.ui.autoFootrestPlotButton.clicked.connect(lambda:       self.updatePlotMode("Footrest", True))
        self.main_window.ui.manualFootrestPlotButton.clicked.connect(lambda:     self.updatePlotMode("Footrest", False))
        self.main_window.ui.plotFootrestButton.clicked.connect(lambda:           self.plotData("Footrest"))
        self.main_window.ui.openFootrestPlotButton.clicked.connect(lambda:       self.openPlot("Footrest"))
        self.main_window.ui.selectFootrestFolderButton.clicked.connect(lambda:   self.selectPIDFolder("Footrest"))

        self.main_window.ui.plotFootrestButton.setEnabled(False)    # Button is disabled by default until a folder is created.
        self.main_window.ui.openFootrestPlotButton.setEnabled(False)    # Button is disabled by default until a plot is created.

        # Footrest attributes - Tuning.
        self.main_window.ui.footrestFoldTuneButton.clicked.connect(lambda:       self.updateTuningDirection("Footrest"))
        self.main_window.ui.footrestUnfoldTuneButton.clicked.connect(lambda:     self.updateTuningDirection("Footrest"))
        self.main_window.ui.alterFootrestTuningButton.clicked.connect(lambda:    self.alterTuningData("Footrest"))
        self.main_window.ui.copyFootrestTuningButton.clicked.connect(lambda:     self.copyTuningData("Footrest"))
        self.main_window.ui.requestFootrestTuningButton.clicked.connect(lambda:  self.requestTuningData("Footrest"))
        self.main_window.ui.resetFootrestTuningButton.clicked.connect(lambda:    self.resetAlteredData("Footrest"))

        delegateFootrestDriveControl = Painter()
        delegateFootrestPosTune = Painter()
        delegateFootrestSpeedTune = Painter()
        self.main_window.ui.footrestDriveControlTable.setItemDelegate(delegateFootrestDriveControl)
        self.main_window.ui.footrestPIDPosTable.setItemDelegate(delegateFootrestPosTune)
        self.main_window.ui.footrestPIDSpeedTable.setItemDelegate(delegateFootrestSpeedTune)

        self.footrestHSLogging = False
        self.autoFootrestPlot = False
        self.manualFootrestPlot = True

        self.footrestCurrentLogFile = None      # Last current log file created.
        self.footrestPlottingActive = False     # Flag to indicate if the plot is active.
        self.footrestPlottingFileClosed = True  # Flag to indicate if the plot file is closed (To prevent multiple closures).

        self.footrestLogger = Logger("FR_PIDData")
        self.footrestLogger.columns = "driveId:0, tickMs:0, currentPosition, targetPosition, currentSpeed, targetSpeed, error:4, integral:2, derivative:0, speedError:4, speedIntegral:2, sppedDerivative:0, kpTerm:3, kiTerm:3, kdTerm:3, kffTerm:3, kPSpeedTerm:3, kISpeedTerm:3, kDSpeedTerm:3, output:3, current:3"


        # Main attributes - PID.
        self.main_window.ui.requestMainLoggingButton.clicked.connect(lambda:     self.requestHSLogging("Main"))
        self.main_window.ui.autoMainPlotButton.clicked.connect(lambda:           self.updatePlotMode("Main", True))
        self.main_window.ui.manualMainPlotButton.clicked.connect(lambda:         self.updatePlotMode("Main", False))
        self.main_window.ui.plotMainButton.clicked.connect(lambda:               self.plotData("Main"))
        self.main_window.ui.openMainPlotButton.clicked.connect(lambda:           self.openPlot("Main"))
        self.main_window.ui.selectMainFolderButton.clicked.connect(lambda:       self.selectPIDFolder("Main"))

        self.main_window.ui.plotMainButton.setEnabled(False)    # Button is disabled by default until a folder is created.
        self.main_window.ui.openMainPlotButton.setEnabled(False)    # Button is disabled by default until a plot is created.

        # Main attributes - Tuning.
        self.main_window.ui.enableMainSpeedButton.toggled.connect(lambda:       self.updateTuningDirection("Main"))
        self.main_window.ui.alterMainTuningButton.clicked.connect(lambda:       self.alterTuningData("Main"))
        self.main_window.ui.copyMainTuningButton.clicked.connect(lambda:        self.copyTuningData("Main"))
        self.main_window.ui.requestMainTuningButton.clicked.connect(lambda:     self.requestTuningData("Main"))
        self.main_window.ui.resetMainTuningButton.clicked.connect(lambda:       self.resetAlteredData("Main"))

        delegateMainDriveControl = Painter()
        delegateMainPosTune = Painter()
        delegateMainSpeedTune = Painter()
        self.main_window.ui.mainDriveControlTable.setItemDelegate(delegateMainDriveControl)
        self.main_window.ui.mainPIDPosTable.setItemDelegate(delegateMainPosTune)
        self.main_window.ui.mainPIDSpeedTable.setItemDelegate(delegateMainSpeedTune)

        self.mainHSLogging = False
        self.autoMainPlot = False
        self.manualMainPlot = True

        self.mainCurrentLogFile = None        # Last current log file created.
        self.mainPlottingActive = False       # Flag to indicate if the plot is active.
        self.mainPlottingFileClosed = True    # Flag to indicate if the plot file is closed (To prevent multiple closures).

        self.mainLogger = Logger("MD_PIDData")
        self.mainLogger.columns = "driveId:0, tickMs:0, currentPosition, targetPosition, currentSpeed:2, targetSpeed:2, error:4, integral:2, derivative:0, speedError:4, speedIntegral:2, sppedDerivative:0, kpTerm:3, kiTerm:3, kdTerm:3, kffTerm:3, kPSpeedTerm:3, kISpeedTerm:3, kDSpeedTerm:3, output:3, current:3, gx:0, gy:0, gz:0"


        # Swivel attributes - PID.
        self.main_window.ui.requestSwivelLoggingButton.clicked.connect(lambda:   self.requestHSLogging("Swivel"))
        self.main_window.ui.autoSwivelPlotButton.clicked.connect(lambda:         self.updatePlotMode("Swivel", True))
        self.main_window.ui.manualSwivelPlotButton.clicked.connect(lambda:       self.updatePlotMode("Swivel", False))
        self.main_window.ui.plotSwivelButton.clicked.connect(lambda:             self.plotData("Swivel"))
        self.main_window.ui.openSwivelPlotButton.clicked.connect(lambda:         self.openPlot("Swivel"))
        self.main_window.ui.selectSwivelFolderButton.clicked.connect(lambda:     self.selectPIDFolder("Swivel"))

        self.main_window.ui.plotSwivelButton.setEnabled(False)    # Button is disabled by default until a folder is created.
        self.main_window.ui.openSwivelPlotButton.setEnabled(False)    # Button is disabled by default until a plot is created.

        # Swivel attributes - Tuning.
        self.main_window.ui.swivelLeftTuneButton.clicked.connect(lambda:         self.updateTuningDirection("Swivel"))
        self.main_window.ui.swivelRightTuneButton.clicked.connect(lambda:        self.updateTuningDirection("Swivel"))
        self.main_window.ui.alterSwivelTuningButton.clicked.connect(lambda:      self.alterTuningData("Swivel"))
        self.main_window.ui.copySwivelTuningButton.clicked.connect(lambda:       self.copyTuningData("Swivel"))
        self.main_window.ui.requestSwivelTuningButton.clicked.connect(lambda:    self.requestTuningData("Swivel"))
        self.main_window.ui.resetSwivelTuningButton.clicked.connect(lambda:      self.resetAlteredData("Swivel"))

        delegateSwivelDriveControl = Painter()
        delegateSwivelPosTune = Painter()
        delegateSwivelSpeedTune = Painter()
        self.main_window.ui.swivelDriveControlTable.setItemDelegate(delegateSwivelDriveControl)
        self.main_window.ui.swivelPIDPosTable.setItemDelegate(delegateSwivelPosTune)
        self.main_window.ui.swivelPIDSpeedTable.setItemDelegate(delegateSwivelSpeedTune)

        self.swivelHSLogging = False
        self.autoSwivelPlot = False
        self.manualSwivelPlot = True

        self.swivelCurrentLogFile = None        # Last current log file created.
        self.swivelPlottingActive = False       # Flag to indicate if the plot is active.
        self.swivelPlottingFileClosed = True    # Flag to indicate if the plot file is closed (To prevent multiple closures).

        self.swivelLogger = Logger("SW_PIDData")
        self.swivelLogger.columns = "driveId:0, tickMs:0, currentPosition, targetPosition, currentSpeed, targetSpeed, error:4, integral:2, derivative:0, speedError:4, speedIntegral:2, sppedDerivative:0, kpTerm:3, kiTerm:3, kdTerm:3, kffTerm:3, kPSpeedTerm:3, kISpeedTerm:3, kDSpeedTerm:3, output:3, current:3"

        self.plotting_processes = {}  # To store {drive: (process, state_widget)}
        self.plotting_timer = QTimer()
        self.plotting_timer.timeout.connect(self.check_plotting_status)
        self.plotting_timer.setInterval(1000)

        self.setStyleSheetUIPID()
        self.populateControlTables()
        self.populateTuningTables()


    #----------------------------------------------- UI Styling -----------------------------------------------


    def setStyleSheetUIPID(self):
        """
        Sets the style sheet for the UIPID tables.
        Only doing additional stuff to items here that would not work in QTCreator.
        """
        tables = [
            self.main_window.ui.chairDriveControlTable,
            self.main_window.ui.footrestDriveControlTable,
            self.main_window.ui.mainDriveControlTable,
            self.main_window.ui.swivelDriveControlTable,
            self.main_window.ui.chairPIDPosTable,
            self.main_window.ui.footrestPIDPosTable,
            self.main_window.ui.mainPIDPosTable,
            self.main_window.ui.swivelPIDPosTable,
            self.main_window.ui.chairPIDSpeedTable,
            self.main_window.ui.footrestPIDSpeedTable,
            self.main_window.ui.mainPIDSpeedTable,
            self.main_window.ui.swivelPIDSpeedTable
        ]

        for table in tables:
            header = table.horizontalHeader()
            if table in [self.main_window.ui.chairDriveControlTable, self.main_window.ui.footrestDriveControlTable,
                         self.main_window.ui.mainDriveControlTable, self.main_window.ui.swivelDriveControlTable]:
                header.setSectionResizeMode(0, QHeaderView.Fixed)
                header.setSectionResizeMode(1, QHeaderView.Stretch)
                header.setSectionResizeMode(2, QHeaderView.Stretch)
                header.setFixedHeight(20)

                table.setColumnWidth(0, 45)

            if table in [self.main_window.ui.chairPIDPosTable, self.main_window.ui.footrestPIDPosTable,
                         self.main_window.ui.mainPIDPosTable, self.main_window.ui.swivelPIDPosTable,
                         self.main_window.ui.chairPIDSpeedTable, self.main_window.ui.footrestPIDSpeedTable,
                         self.main_window.ui.mainPIDSpeedTable, self.main_window.ui.swivelPIDSpeedTable]:
                header.setSectionResizeMode(0, QHeaderView.Fixed)
                header.setSectionResizeMode(1, QHeaderView.Fixed)
                header.setSectionResizeMode(2, QHeaderView.Fixed)
                header.setFixedHeight(20)

                table.setColumnWidth(0, 79)
                table.setColumnWidth(1, 79)
                table.setColumnWidth(2, 79)

            # Disable the built-in grid, will customise with the delegate class.
            table.setShowGrid(False)

            # Refine the style sheet. Focusing really on the header.
            table.setStyleSheet(f"""
            QTableWidget {{
                border: 2px solid {Colours.BLACK.name()};           /* Border of the table */
                background: {Colours.BEIGE.name()};                 /* Background colour of table */
            }}
            QHeaderView::section {{
                background-color: {Colours.ICTERINE.name()};        /* Background colour of the header */
                border: none;                                       /* Border of the header */
                border-right: 1px solid {Colours.BLACK.name()};     /* Right border of the header. Splits columns visually */
                border-bottom: 2px solid {Colours.BLACK.name()};    /* Bottom border of the header */
                color: {Colours.BLACK.name()};                      /* Text colour of the header */
                font-weight: normal;                                /* Font weight of the header text */
            }}
            QHeaderView::section:last {{
                border-right: none;                                 /* Remove the right border from the last header section. This is because of an overlap with the table widget border */
            }}
            """)


    def populateControlTables(self):
        """
        Populates the PID table with ID and name.
        """
        tables = [
            self.main_window.ui.chairDriveControlTable,
            self.main_window.ui.footrestDriveControlTable,
            self.main_window.ui.mainDriveControlTable,
            self.main_window.ui.swivelDriveControlTable
        ]

        for table in tables:
            table.setRowCount(len(PID))
            row = 0

            # Setup each row.
            for index, var in enumerate(PID):
                # Column 0 is not editable.
                column0 = QTableWidgetItem(f"{index}")
                column0.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, 0, column0)

                # Column 1 is not editable.
                column1 = QTableWidgetItem(var.name)
                column1.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, 1, column1)

                # Column 2 is not editable.
                column2 = QTableWidgetItem("")
                column2.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, 2, column2)

                row += 1

            # Force additional settings to rows/columns after populated.
            for row in range(table.rowCount()):
                table.setRowHeight(row, 18)

                # Row colours.
                table.item(row, 0).setBackground(Colours.BEIGE)
                table.item(row, 1).setBackground(Colours.BEIGE)
                table.item(row, 2).setBackground(Colours.BEIGE)

                table.item(row, 0).setForeground(Colours.GARNET)
                table.item(row, 1).setForeground(Colours.BLACK)
                table.item(row, 2).setForeground(Colours.BLACK)

                # Column alignment.
                for col in range(table.columnCount()):
                    alignment = Qt.AlignLeft if col == 1 else Qt.AlignHCenter
                    alignment |= Qt.AlignVCenter
                    table.item(row, col).setTextAlignment(alignment)

        # Resize the table to the content.
        self.resizeControlTableToContent()


    def resizeControlTableToContent(self):
        """
        Resizes the control table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons to positions based on the new table size.
        """
        tables = [
            self.main_window.ui.chairDriveControlTable,
            self.main_window.ui.footrestDriveControlTable,
            self.main_window.ui.mainDriveControlTable,
            self.main_window.ui.swivelDriveControlTable
        ]

        for table in tables:
            if table == self.main_window.ui.chairDriveControlTable:
                auto_button = self.main_window.ui.autoChairPlotButton
                manual_button = self.main_window.ui.manualChairPlotButton
                plot_button = self.main_window.ui.plotChairButton
                open_plot_button = self.main_window.ui.openChairPlotButton
            elif table == self.main_window.ui.footrestDriveControlTable:
                auto_button = self.main_window.ui.autoFootrestPlotButton
                manual_button = self.main_window.ui.manualFootrestPlotButton
                plot_button = self.main_window.ui.plotFootrestButton
                open_plot_button = self.main_window.ui.openFootrestPlotButton
            elif table == self.main_window.ui.mainDriveControlTable:
                auto_button = self.main_window.ui.autoMainPlotButton
                manual_button = self.main_window.ui.manualMainPlotButton
                plot_button = self.main_window.ui.plotMainButton
                open_plot_button = self.main_window.ui.openMainPlotButton
            elif table == self.main_window.ui.swivelDriveControlTable:
                auto_button = self.main_window.ui.autoSwivelPlotButton
                manual_button = self.main_window.ui.manualSwivelPlotButton
                plot_button = self.main_window.ui.plotSwivelButton
                open_plot_button = self.main_window.ui.openSwivelPlotButton

            # Table height.
            table_row_count = table.rowCount()
            table_row_height = table.rowHeight(0)
            table_header_height = table.horizontalHeader().height()
            table_frame_width = table.frameWidth()
            total_table_height = table_header_height + (table_row_count * table_row_height) + (2 * table_frame_width)
            table.setFixedHeight(total_table_height)

            # Define gaps.
            pixel_gap = 10
            radio_gap = 5
            button_gap = 18

            radio_height = auto_button.height()

            # Calculate positions for the radio buttons.
            auto_radio_button_top = table.y() + total_table_height + pixel_gap
            auto_radio_button_bottom = auto_radio_button_top + radio_height
            manual_radio_button_top = auto_radio_button_bottom + radio_gap
            manual_radio_button_bottom = manual_radio_button_top + radio_height

            # Calculate positions for the plot buttons.
            button_position_top = table.y() + total_table_height + button_gap

            # Move buttons to their respective positions.
            auto_button.move(auto_button.x(), auto_radio_button_top)
            manual_button.move(manual_button.x(), manual_radio_button_top)
            plot_button.move(plot_button.x(), button_position_top)
            open_plot_button.move(open_plot_button.x(), button_position_top)

            # Total group height is the sum of the table height, radio button heights, and gaps.
            group_box_height = manual_radio_button_bottom + pixel_gap

            # Set the new group box height.
            table.parent().setFixedHeight(group_box_height)


    def populateTuningTables(self):
        """
        Populates the tuning tables with the ID and name
        """
        tables = [
            self.main_window.ui.chairPIDPosTable,
            self.main_window.ui.footrestPIDPosTable,
            self.main_window.ui.mainPIDPosTable,
            self.main_window.ui.swivelPIDPosTable,
            self.main_window.ui.chairPIDSpeedTable,
            self.main_window.ui.footrestPIDSpeedTable,
            self.main_window.ui.mainPIDSpeedTable,
            self.main_window.ui.swivelPIDSpeedTable
        ]

        for table in tables:
            if table in [self.main_window.ui.chairPIDPosTable, self.main_window.ui.footrestPIDPosTable,
                         self.main_window.ui.mainPIDPosTable, self.main_window.ui.swivelPIDPosTable]:
                terms = ["P", "I", "D", "FF"]
            else:
                terms = ["P", "I", "D"]

            table.setRowCount(len(terms))
            row = 0

            # Setup each row.
            for _, term in enumerate(terms):
                # Column 0 is not editable.
                column0 = QTableWidgetItem(term)
                column0.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, 0, column0)

                # Column 1 is not editable.
                column1 = QTableWidgetItem("")
                column1.setFlags(Qt.ItemIsEnabled)
                table.setItem(row, 1, column1)

                # Column 2 is editable.
                column2 = QTableWidgetItem("")
                column2.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                table.setItem(row, 2, column2)

                row += 1

            # Force additional settings to rows/columns after populated.
            for row in range(table.rowCount()):
                table.setRowHeight(row, 18)

                # Row colours.
                table.item(row, 0).setBackground(Colours.BEIGE)
                table.item(row, 1).setBackground(Colours.BEIGE)
                table.item(row, 2).setBackground(Colours.BEIGE)

                table.item(row, 0).setForeground(Colours.GARNET)
                table.item(row, 1).setForeground(Colours.BLACK)
                table.item(row, 2).setForeground(Colours.BLACK)

                # Column alignment.
                for col in range(table.columnCount()):
                    alignment = Qt.AlignHCenter | Qt.AlignVCenter
                    table.item(row, col).setTextAlignment(alignment)

        # Resize the tables to the content.
        self.resizeTuningTablesToContent()


    def resizeTuningTablesToContent(self):
        """
        Resizes the tuning table size (in UI file) to the total number of rows. Moves the bottom frame to positions based on the new table size.
        """
        tables = [
            self.main_window.ui.chairPIDPosTable,
            self.main_window.ui.footrestPIDPosTable,
            self.main_window.ui.mainPIDPosTable,
            self.main_window.ui.swivelPIDPosTable,
            self.main_window.ui.chairPIDSpeedTable,
            self.main_window.ui.footrestPIDSpeedTable,
            self.main_window.ui.mainPIDSpeedTable,
            self.main_window.ui.swivelPIDSpeedTable
        ]

        for table in tables:
            # Table height
            table_row_count = table.rowCount()
            table_row_height = table.rowHeight(0)
            table_header_height = table.horizontalHeader().height()
            table_frame_width = table.frameWidth()
            table_total_height = table_header_height + (table_row_count * table_row_height) + (2 * table_frame_width)
            table.setFixedHeight(table_total_height)


    #----------------------------------------------- PID -----------------------------------------------


    def requestHSLogging(self, drive):
        """
        Sends the request to enable/disable logging for the selected drive. Updates the UI to reflect the change providing the port is connected.

        @param drive: The drive to enable/disable logging for.
        """
        try:
            drive_lower_case = drive.lower() # Convert text to lower case
            drive_logging = getattr(self, f"{drive_lower_case}HSLogging")
            enable = True if not drive_logging else False

            if drive == "Chair":
                high_speed_source = HighSpeedSources.CHAIR_FOLD_CTRL_DATA.value
                src_dest = SrcDest.SRC_DEST_X01
            elif drive == "Footrest":
                high_speed_source = HighSpeedSources.FOOTREST_CTRL_DATA.value
                src_dest = SrcDest.SRC_DEST_X04
            elif drive == "Main":
                high_speed_source = HighSpeedSources.MAIN_MOTOR_DATA.value
                src_dest = SrcDest.SRC_DEST_X04
            elif drive == "Swivel":
                high_speed_source = HighSpeedSources.SWIVEL_CTRL_DATA.value
                src_dest = SrcDest.SRC_DEST_X01
            else:
                return

            if self.main_window.ui_comms.sendMessage(MessageID.HS_LOGGING_ENABLE, "BB", [high_speed_source, enable], src_dest, MsgMode.SET):
                setattr(self, f"{drive_lower_case}HSLogging", enable)
                self.updateLoggingText(drive_lower_case, enable)

        except Exception as e:
            print(f"E1: {__file__}: {e}")


    def updateDriveControlTable(self, msg):
        """
        Handles new drive control data for a specific drive.

        @param msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not out. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.OUT:
                # Only interested in the drive ID first to see how much we need to unpack the full payload to.
                _, drive_id = unpackMessagePartial("B", msg)

                if SystemDrive(drive_id[0]) in [SystemDrive.SYS_DRIVE_CHAIR_FOLD, SystemDrive.SYS_DRIVE_FOOTREST, SystemDrive.SYS_DRIVE_SWIVEL]:
                    control_data = unpackMessagePayload("BI10i9h", msg)
                else:
                    control_data = unpackMessagePayload("BI10i12h", msg)

                gui_data = control_data

                if control_data[0] == SystemDrive.SYS_DRIVE_CHAIR_FOLD.value:
                    drive = "chair"
                elif control_data[0] == SystemDrive.SYS_DRIVE_FOOTREST.value:
                    drive = "footrest"
                elif control_data[0] == SystemDrive.SYS_DRIVE_MAIN_DRIVE.value:
                    drive = "main"
                    gui_data = gui_data[:-3] # Remove gx, gy, gz from the GUI data but is kept when logging to CSV.
                elif control_data[0] == SystemDrive.SYS_DRIVE_SWIVEL.value:
                    drive = "swivel"
                else:
                    return

                # Get the table for the drive.
                drive_control_table = getattr(self.main_window.ui, f"{drive}DriveControlTable", None)

                # Populate table with new data.
                for index, val in enumerate(gui_data):
                    item = drive_control_table.item(index, 2)
                    item.setText(f"{val}")

                # Only write if plotting is currently active for this drive.
                drive_plotting_active = getattr(self, f"{drive}PlottingActive", None)
                if drive_plotting_active:
                    self.writeCSV(drive, control_data)

        except Exception as e:
            print(f"E2: {__file__}: {e}")


    def selectPIDFolder(self, drive):
        """
        Selects the folder for the PID data for the selected drive. If the folder does not exist, it will be created.

        @param drive: The drive to select the tuning folder for.
        """
        drive_lower_case = drive.lower() # Convert to lower case
        default_folder = f"PIDLogs/{drive}"

        if not os.path.exists(default_folder):
            print(f"Default folder {default_folder} does not exist. Creating it.")
            os.makedirs(default_folder)

        folder = QFileDialog.getExistingDirectory(None, f"Select {drive} Tuning Folder", default_folder)
        if folder:
            folder_mapping = {
                "Chair": ("chairFolder", "plotChairButton"),
                "Footrest": ("footrestFolder", "plotFootrestButton"),
                "Main": ("mainFolder", "plotMainButton"),
                "Swivel": ("swivelFolder", "plotSwivelButton")
            }

            if drive in folder_mapping:
                text_folder_attr, plot_button_attr = folder_mapping[drive]
                text_folder = getattr(self.main_window.ui, text_folder_attr)
                plot_button = getattr(self.main_window.ui, plot_button_attr)

                text_folder.setText(folder)

                # Update the logger class with the new folder location for the drive
                drive_logger = getattr(self, f"{drive_lower_case}Logger", None)
                drive_logger.setFolder(folder)
                print(f"New {drive} folder: {folder}")

                manual_plot = getattr(self, f"manual{drive}Plot", None)
                if manual_plot:
                    # Only enable and update the button if we are in manual plot mode.
                    plot_button.setEnabled(True)
                    plot_button.setStyleSheet(f"""
                                                QPushButton {{
                                                    color: {Colours.BLACK.name()};
                                                    border: 2px solid {Colours.BLACK.name()};
                                                    border-radius: 10px;
                                                    background-color: {Colours.PALE_GREEN.name()};
                                                }}
                                                QPushButton:hover {{
                                                    border: 2px solid {Colours.BLACK.name()};
                                                    border-radius: 1px;
                                                    background-color: {Colours.PALE_GREEN.name()};
                                                }}
                                                QPushButton:pressed {{
                                                    border: 2px solid {Colours.BLACK.name()};
                                                    border-radius: 1px;
                                                    background-color: {Colours.PALE_GREEN.name()};
                                                }}
                                                """)
        else:
            print(f"{drive} folder selection error.")
            return


    def updatePlotMode(self, drive, auto):
        """
        Switches between auto or manual plot mode. The plot button is disabled in auto mode.
        When manual mode has been selected, if a folder is not chosen, the button will remain disabled, else it will be enabled.

        @param drive: The drive to handle the plot mode for.
        @param auto: True if in auto mode, False if in manual mode.
        """
        button = getattr(self.main_window.ui, f"plot{drive}Button")

        if auto:
            setattr(self, f"auto{drive}PlotButton", True)
            setattr(self, f"manual{drive}PlotButton", False)

            # Switched to auto mode, so disable the plot button, set the text to "Sel Auto" and set colour to red.
            button.setStyleSheet(f"""
                                QPushButton {{
                                    color: {Colours.BLACK.name()}; /* Text color */
                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                    border-radius: 10px; /* Rounded corners */
                                    background-color: {Colours.LIGHT_PINK.name()};
                                }}
                                QPushButton:hover {{
                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                    border-radius: 1px; /* Rounded corners */
                                }}
                                QPushButton:pressed {{
                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                    border-radius: 1px; /* Rounded corners */
                                }}
                                """)
            button.setText("Sel Manual")
            button.setEnabled(False)
        else:
            setattr(self, f"auto{drive}Plot", False)
            setattr(self, f"manual{drive}Plot", True)

            logger = getattr(self, f"{drive.lower()}Logger")
            logger_folder = logger.getFolder()

            if logger_folder is not None:
                # Switched to manual mode and a folder has been selected, so enable the button, set the text to "Start Plot" and set colour to green.
                button.setEnabled(True)
                button.setStyleSheet(f"""
                                    QPushButton {{
                                        color: {Colours.BLACK.name()}; /* Text color */
                                        border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                        border-radius: 10px; /* Rounded corners */
                                        background-color: {Colours.LIGHT_GREEN.name()};
                                    }}
                                    QPushButton:hover {{
                                        border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                        border-radius: 1px; /* Rounded corners */
                                    }}
                                    QPushButton:pressed {{
                                        border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                        border-radius: 1px; /* Rounded corners */
                                    }}
                                    """)
                button.setText("Start Plot")
            else:
                # Switched to manual mode but no folder has been selected, so disable the button, set the text to "Start Plot" and set colour to red.
                button.setEnabled(False)
                button.setStyleSheet(f"""
                                    QPushButton {{
                                        color: {Colours.BLACK.name()}; /* Text color */
                                        border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                        border-radius: 10px; /* Rounded corners */
                                        background-color: {Colours.LIGHT_PINK.name()};
                                    }}
                                    QPushButton:hover {{
                                        border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                        border-radius: 1px; /* Rounded corners */
                                    }}
                                    QPushButton:pressed {{
                                        border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                        border-radius: 1px; /* Rounded corners */
                                    }}
                                    """)
                button.setText("Start Plot")


    def plotData(self, drive):
        """
        Plots the data for the selected drive. A folder must have been selected for this button to activate.

        @param drive: The drive to plot the data for.
        """
        drive_lower_case = drive.lower() # Convert to lower case
        manual_drive_plot = getattr(self, f"manual{drive}Plot")
        plot_drive_button = getattr(self.main_window.ui, f"plot{drive}Button")
        drive_plotting_active = getattr(self, f"{drive_lower_case}PlottingActive", None)

        if drive_plotting_active:
            # Stop plotting for drive.
            setattr(self, f"{drive_lower_case}PlottingActive", False)

            # Close any open CSV file for the drive.
            self.closeCSV(drive_lower_case)

            # Update the plot state text box.
            self.updatePlottingText(drive_lower_case, False)

            if manual_drive_plot:
                plot_drive_button.setText("Start Plot")
                plot_drive_button.setStyleSheet(f"""
                                                QPushButton {{
                                                    color: {Colours.BLACK.name()}; /* Text color */
                                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                    border-radius: 10px; /* Rounded corners */
                                                    background-color: {Colours.PALE_GREEN.name()};
                                                }}
                                                QPushButton:hover {{
                                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                    border-radius: 1px; /* Rounded corners */
                                                }}
                                                QPushButton:pressed {{
                                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                    border-radius: 1px; /* Rounded corners */
                                                }}
                                            """)
        else:
            # Start plotting for drive.
            drive_logger = getattr(self, f"{drive_lower_case}Logger", None)

            if drive_logger:
                if drive_logger.file is not None:
                    # Close the logger if a file is currently open. This ensures that the next call to drive_logger.write() will trigger the creation of a brand new file.
                    print(f"Logger for {drive} indicates file {drive_logger.getFilename()} was open. Closing it to ensure new file on next plot.")
                    drive_logger.close()

            setattr(self, f"{drive_lower_case}PlottingActive", True)
            setattr(self, f"{drive_lower_case}PlottingFileClosed", True) # File is considered closed until something has been written to it.
            setattr(self, f"{drive_lower_case}CurrentLogFile", None) # Clear any old file log names.

            # Update the plot state text box.
            self.updatePlottingText(drive_lower_case, True)

            if manual_drive_plot:
                plot_drive_button.setText("Stop Plot")
                plot_drive_button.setStyleSheet(f"""
                                                QPushButton {{
                                                    color: {Colours.BLACK.name()}; /* Text color */
                                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                    border-radius: 10px; /* Rounded corners */
                                                    background-color: {Colours.LIGHT_PINK.name()};
                                                }}
                                                QPushButton:hover {{
                                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                    border-radius: 1px; /* Rounded corners */
                                                }}
                                                QPushButton:pressed {{
                                                    border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                    border-radius: 1px; /* Rounded corners */
                                                }}
                                                """)

            # Enable the open plot button.
            open_plot_button = getattr(self.main_window.ui, f"open{drive}PlotButton")
            open_plot_button.setEnabled(True)
            open_plot_button.setStyleSheet(f"""
                                            QPushButton {{
                                                color: {Colours.BLACK.name()}; /* Text color */
                                                border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                border-radius: 10px; /* Rounded corners */
                                                background-color: {Colours.WHITE_SMOKE.name()};
                                            }}
                                            QPushButton:hover {{
                                                border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                border-radius: 1px; /* Rounded corners */
                                                background-color: {Colours.PALE_GREEN.name()};
                                            }}
                                            QPushButton:pressed {{
                                                border: 2px solid {Colours.BLACK.name()}; /* Border color */
                                                border-radius: 1px; /* Rounded corners */
                                                background-color: {Colours.PALE_GREEN.name()};
                                            }}
                                            """)


    def openPlot(self, drive):
        """
        Opens the most recent plotted file for the selected drive.

        @param drive: The drive to open the plotted file for.
        """
        drive_current_log_file = getattr(self, f"{drive.lower()}CurrentLogFile", None)
        drive_plotting_state = getattr(self.main_window.ui, f"{drive.lower()}PlottingState", None)

        if drive_current_log_file is not None:
            try:
                # If a process for this drive is already being monitored, clean it up first.
                if drive in self.plotting_processes:
                    old_process, _ = self.plotting_processes[drive]
                    if old_process.is_alive():
                        old_process.terminate()
                    del self.plotting_processes[drive]

                plot_process = multiprocessing.Process(target=createPlot, args=(drive_current_log_file,))
                plot_process.daemon = True
                plot_process.start()

                self.plotting_processes[drive] = (plot_process, drive_plotting_state)

                drive_plotting_state.setText("Opening")
                drive_plotting_state.setStyleSheet(f"""
                                                    QLineEdit {{
                                                        background-color: {Colours.PALE_GREEN.name()};
                                                        border: 1px solid black;
                                                        border-radius: 3px;
                                                    }}
                                                    """
)
                # File is now opened, run the timer to periodically check when user closes it.
                if not self.plotting_timer.isActive():
                    self.plotting_timer.start()

            except Exception as e:
                print(f"E3: {__file__} - {drive} - {e}")
                drive_plotting_state.setText("Error")
                drive_plotting_state.setStyleSheet(f"""
                                                    QLineEdit {{
                                                        background-color: {Colours.LIGHT_PINK.name()};
                                                        border: 1px solid black;
                                                        border-radius: 3px;
                                                    }}
                                                    """)
        else:
            drive_plotting_state.setText(f"Plot Not Found")
            drive_plotting_state.setStyleSheet(f"""
                                                QLineEdit {{
                                                    background-color: {Colours.LIGHT_PINK.name()};
                                                    border: 1px solid black;
                                                    border-radius: 3px;
                                                }}
                                                """)


    def check_plotting_status(self):
        """
        Called when a plotted file is opened. Checks if the open file is now closed and updates the text edit.
        """
        # Check if any processes are actively open, if not, stop the timer and exit.
        if not self.plotting_processes:
            self.plotting_timer.stop()
            return

        for drive, (process, state_widget) in list(self.plotting_processes.items()):
            if not process.is_alive():
                # Process has finished, update the text edit and delete the process.
                state_widget.setText("Closed")
                state_widget.setStyleSheet(f"""
                                        QLineEdit {{
                                            background-color: {Colours.CANARY_YELLOW.name()};
                                            border: 1px solid black;
                                            border-radius: 3px;
                                        }}
                                        """)
                del self.plotting_processes[drive]


    def writeCSV(self, drive, data):
        """
        Writes PID data to CSV file for specified drive.

        @param drive: The drive to write the data for. (Must be lower case)
        @param data: The data to write to the CSV file.
        """
        drive_capitalised = drive.capitalize()
        drive_logger = getattr(self, f"{drive}Logger", None)
        drive_plotting_active = getattr(self, f"{drive}PlottingActive", False)

        if drive_plotting_active:
            row = ', '.join(map(str, data))
            drive_logger.write(row)

            filename = drive_logger.getFilename()

            if filename: # Should always be true if write succeeded
                current_filename = getattr(self, f"{drive}CurrentLogFile", None)
                if filename != current_filename:
                    setattr(self, f"{drive}CurrentLogFile", filename)
                    print(f"Started logging {drive_capitalised} data to new file: {filename}")

                if getattr(self, f"{drive}PlottingFileClosed", True):
                    # Since a write occurred and we have a filename, the file is now currently "open"
                    setattr(self, f"{drive}PlottingFileClosed", False)
            else:
                print(f"Warning: Logger for {drive_capitalised} wrote data but has no filename.")


    def closeCSV(self, drive):
        """
        Closes the CSV file for the specified drive.

        @param drive: The drive to close the CSV file for. (must be lower case)
        """
        drive_capitalised = drive.capitalize()
        drive_logger = getattr(self, f"{drive}Logger", None)

        # Attempt to get filename before closing, or use stored if logger already closed.
        filename = drive_logger.getFilename() or getattr(self, f'{drive}CurrentLogFile', None)

        try:
            drive_logger.close()
            setattr(self, f"{drive}PlottingFileClosed", True)

            if filename: # If there was a file concept (either open in logger or stored)
                print(f"Stopped logging {drive_capitalised} data to file: {filename}")
            else:
                print(f"{drive_capitalised} plot file session ended (file might not have been created or already closed).")

        except Exception as e:
            print(f"E4: {__file__} - {drive} - {e}")


    def updateLoggingText(self, drive, state):
        """
        Updates the text of the high speed logging line edit for the selected drive.

        @param drive: The drive to set the logging state for.
        @param state: The state to set the line edit to. True for enabled, False for disabled.
        """
        logging_state = getattr(self.main_window.ui, f"{drive}HSState")

        if state:
            logging_state.setText("HS Logging Enabled")
            logging_state.setStyleSheet(f"""
                                        QLineEdit {{
                                            background-color: {Colours.PALE_GREEN.name()};
                                            border: 1px solid black;
                                            border-radius: 3px;
                                        }}
                                        """)
        else:
            logging_state.setText("HS Logging Disabled")
            logging_state.setStyleSheet(f"""
                                        QLineEdit {{
                                            background-color: {Colours.CANARY_YELLOW.name()};
                                            border: 1px solid black;
                                            border-radius: 3px;
                                        }}
                                        """)

    def updatePlottingText(self, drive, state):
        """
        Updates the text of the plotting line edit for the selected drive.

        @param drive: The drive to set the plotting state for.
        @param state: The state to set the line edit to. True for enabled, False for disabled.
        """
        plot_state = getattr(self.main_window.ui, f"{drive}LoggingState")

        if state:
            plot_state.setText("Active")
            plot_state.setStyleSheet(f"""
                                    QLineEdit {{
                                        background-color: {Colours.PALE_GREEN.name()};
                                        border: 1px solid black;
                                        border-radius: 3px;
                                    }}
                                    """)
        else:
            plot_state.setText("Inactive")
            plot_state.setStyleSheet(f"""
                                    QLineEdit {{
                                        background-color: {Colours.CANARY_YELLOW.name()};
                                        border: 1px solid black;
                                        border-radius: 3px;
                                    }}
                                    """)


    #----------------------------------------------- Tuning -----------------------------------------------


    def updateTuningDirection(self, drive):
        """
        Radio button has changed for tuning direction data. Request new tuning parameters for the new direction.

        @param drive: The drive to request the tuning data for.
        """
        if drive == "Chair":
            self.requestTuningData("Chair")
        elif drive == "Footrest":
            self.requestTuningData("Footrest")
        elif drive == "Main":
            self.requestTuningData("Main")
        elif drive == "Swivel":
            self.requestTuningData("Swivel")
        else:
            return


    def updateTuningTable(self, msg):
        """
        Handles new tuning data for a specific drive.

        @param msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                tuning_data = unpackMessagePayload("BB7iB", msg)

                drive_id = tuning_data[0]
                drive_terms = tuning_data[2:9]
                speed_enabled = tuning_data[9]

                if drive_id == SystemDrive.SYS_DRIVE_CHAIR_FOLD.value:
                    drive_name = "chair"
                elif drive_id == SystemDrive.SYS_DRIVE_FOOTREST.value:
                    drive_name = "footrest"
                elif drive_id == SystemDrive.SYS_DRIVE_MAIN_DRIVE.value:
                    drive_name = "main"
                elif drive_id == SystemDrive.SYS_DRIVE_SWIVEL.value:
                    drive_name = "swivel"
                else:
                    return

                # Get the table for the drive.
                pos_table = getattr(self.main_window.ui, f"{drive_name}PIDPosTable", None)
                speed_table = getattr(self.main_window.ui, f"{drive_name}PIDSpeedTable", None)

                if pos_table is not None and speed_table is not None:
                    # Update the position table with new data.
                    for index, val in enumerate(drive_terms[0:4]):
                        item = pos_table.item(index, 1)
                        item.setText(f"{val}")

                    # Update the speed table with new data.
                    for index, val in enumerate(drive_terms[4:7]):
                        item = speed_table.item(index, 1)
                        item.setText(f"{val}")

                    # Update speed enable button is speed control is enabled.
                    speed_button = getattr(self.main_window.ui, f"enable{drive_name.capitalize()}SpeedButton", None)
                    if speed_enabled:
                        speed_button.setChecked(True)
                        speed_button.setText("Speed Control Enabled")
                    else:
                        speed_button.setChecked(False)
                        speed_button.setText("Enable Speed Control")

        except Exception as e:
            print(f"E5 {__file__}: {e}")


    def requestTuningData(self, drive):
        """
        Requests the tuning data for the selected drive and direction based on the radio buttons.

        @param drive: The drive to request the tuning data for.
        """
        try:
            if drive == "Chair":
                drive_id = SystemDrive.SYS_DRIVE_CHAIR_FOLD.value
                src_dest = SrcDest.SRC_DEST_X01

                if self.main_window.ui.chairFoldTuneButton.isChecked():
                    direction = DriveControlDir.LEFT.value
                elif self.main_window.ui.chairPartFoldTuneButton.isChecked():
                    direction = DriveControlDir.HOLD.value
                else:
                    direction = DriveControlDir.RIGHT.value

            elif drive == "Footrest":
                drive_id = SystemDrive.SYS_DRIVE_FOOTREST.value
                src_dest = SrcDest.SRC_DEST_X04

                if self.main_window.ui.footrestFoldTuneButton.isChecked():
                    direction = DriveControlDir.LEFT.value
                elif self.main_window.ui.footrestUnfoldTuneButton.isChecked():
                    direction = DriveControlDir.RIGHT.value

            elif drive == "Main":
                drive_id = SystemDrive.SYS_DRIVE_MAIN_DRIVE.value
                src_dest = SrcDest.SRC_DEST_X04
                direction = DriveControlDir.LEFT.value

            elif drive == "Swivel":
                drive_id = SystemDrive.SYS_DRIVE_SWIVEL.value
                src_dest = SrcDest.SRC_DEST_X01

                if self.main_window.ui.swivelLeftTuneButton.isChecked():
                    direction = DriveControlDir.LEFT.value
                elif self.main_window.ui.swivelRightTuneButton.isChecked():
                    direction = DriveControlDir.RIGHT.value

            else:
                return

            pid_conf = (0, 0, 0, 0, 0, 0, 0, 0)
            self.main_window.ui_comms.sendMessage(MessageID.GENERIC_DRIVE_TUNING_DATA, "BBiiiiiiiB", [drive_id, direction, *pid_conf], src_dest, MsgMode.GET)

        except Exception as e:
            print(f"E6: {__file__} - {e}")


    def copyTuningData(self, drive):
        """
        Copies the current tuning data to the alter column for easier tuning.

        @param drive: The drive to copy the tuning data for.
        """
        drive_lower_case = drive.lower()
        pos_table = getattr(self.main_window.ui, f"{drive_lower_case}PIDPosTable")
        speed_table = getattr(self.main_window.ui, f"{drive_lower_case}PIDSpeedTable")

        for table in [pos_table, speed_table]:
            for row in range(table.rowCount()):
                item = table.item(row, 2)
                item.setText(f"{table.item(row, 1).text()}")
                item.setTextAlignment(Qt.AlignCenter)
                item.setForeground(Colours.BLACK)
                item.setBackground(Colours.BEIGE)


    def resetAlteredData(self, drive):
        """
        Clears the current altered data in the tuning table.

        @param drive: The drive to clear the altered data for.
        """
        drive_lower_case = drive.lower()
        pos_table = getattr(self.main_window.ui, f"{drive_lower_case}PIDPosTable")
        speed_table = getattr(self.main_window.ui, f"{drive_lower_case}PIDSpeedTable")

        for table in [pos_table, speed_table]:
            for row in range(table.rowCount()):
                item = table.item(row, 2)
                item.setText("")
                item.setTextAlignment(Qt.AlignCenter)
                item.setForeground(Colours.BLACK)
                item.setBackground(Colours.BEIGE)


    def alterTuningData(self, drive):
        """
        Alters the tuning data for the selected drive.

        @param drive: The drive to alter the tuning data for.
        """
        try:
            if drive == "Chair":
                drive_id = SystemDrive.SYS_DRIVE_CHAIR_FOLD.value
                pos_table = self.main_window.ui.chairPIDPosTable
                speed_table = self.main_window.ui.chairPIDSpeedTable
                dest = SrcDest.SRC_DEST_X01
                if self.main_window.ui.chairFoldTuneButton.isChecked():
                    direction = DriveControlDir.LEFT.value
                elif self.main_window.ui.chairPartFoldTuneButton.isChecked():
                    direction = DriveControlDir.HOLD.value
                else:
                    direction = DriveControlDir.RIGHT.value
                speed_enable = self.main_window.ui.enableChairSpeedButton.isChecked()
            elif drive == "Footrest":
                drive_id = SystemDrive.SYS_DRIVE_FOOTREST.value
                pos_table = self.main_window.ui.footrestPIDPosTable
                speed_table = self.main_window.ui.footrestPIDSpeedTable
                dest = SrcDest.SRC_DEST_X04
                direction = DriveControlDir.LEFT.value if self.main_window.ui.footrestFoldTuneButton.isChecked() else DriveControlDir.RIGHT.value
                speed_enable = self.main_window.ui.enableFootrestSpeedButton.isChecked()
            elif drive == "Main":
                drive_id = SystemDrive.SYS_DRIVE_MAIN_DRIVE.value
                pos_table = self.main_window.ui.mainPIDPosTable
                speed_table = self.main_window.ui.mainPIDSpeedTable
                dest = SrcDest.SRC_DEST_X04
                direction = DriveControlDir.LEFT.value
                speed_enable = self.main_window.ui.enableMainSpeedButton.isChecked()
            elif drive == "Swivel":
                drive_id = SystemDrive.SYS_DRIVE_SWIVEL.value
                pos_table = self.main_window.ui.swivelPIDPosTable
                speed_table = self.main_window.ui.swivelPIDSpeedTable
                dest = SrcDest.SRC_DEST_X01
                direction = DriveControlDir.LEFT.value if self.main_window.ui.swivelLeftTuneButton.isChecked() else DriveControlDir.RIGHT.value
                speed_enable = self.main_window.ui.enableSwivelSpeedButton.isChecked()
            else:
                return

            # Get the tuning data, try alter column first, if there is an empty row, take data from the current data column.
            kp_data = pos_table.item(0, 2) if pos_table.item(0, 2).text() != "" else pos_table.item(0, 1)
            ki_data = pos_table.item(1, 2) if pos_table.item(1, 2).text() != "" else pos_table.item(1, 1)
            kd_data = pos_table.item(2, 2) if pos_table.item(2, 2).text() != "" else pos_table.item(2, 1)
            kf_data = pos_table.item(3, 2) if pos_table.item(3, 2).text() != "" else pos_table.item(3, 1)
            ksP_data = speed_table.item(0, 2) if speed_table.item(0, 2).text() != "" else speed_table.item(0, 1)
            ksI_data = speed_table.item(1, 2) if speed_table.item(1, 2).text() != "" else speed_table.item(1, 1)
            ksD_data = speed_table.item(2, 2) if speed_table.item(2, 2).text() != "" else speed_table.item(2, 1)

            kP = kp_data.text()
            kI = ki_data.text()
            kD = kd_data.text()
            kF = kf_data.text()
            ksP = ksP_data.text()
            ksI = ksI_data.text()
            ksD = ksD_data.text()

            if all(term != "" for term in [kP, kI, kD, kF, ksP, ksI, ksD]):
                pid_conf = (int(kP), int(kI), int(kD), int(kF), int(ksP), int(ksI), int(ksD), speed_enable)
                self.main_window.ui_comms.sendMessage(MessageID.GENERIC_DRIVE_TUNING_DATA, "BBiiiiiiiB", [drive_id, direction, *pid_conf], dest, MsgMode.SET)
            else:
                print("Not all tuning data is set.")

        except Exception as e:
            print(f"E7: {__file__} - {e}")