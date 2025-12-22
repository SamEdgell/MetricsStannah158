# Standard library imports.
import os

# Third party imports.
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QHeaderView, QTableWidgetItem

# Local application imports.
from Enums.enum_ate import ATERequests
from Enums.enum_diag import DiagRequests
from Enums.enum_msg import MessageID, MsgMode, SrcDest
from Enums.enum_rail_map import MapOperationalMode, RailMap, RailMapModes
from UI.ui_custom_widgets import Painter
from UI.ui_styling import Colours, CSS
from Utilities.messages import unpackMessagePayload


class UIRailMap:
    """
    Class for handling all aspects of the rail map for main drive.
    """
    def __init__(self, main_window):
        # Store reference to the main window to access UI elements.
        self.main_window = main_window

        delegateMap = Painter()
        self.main_window.ui.mapDataTable.setItemDelegate(delegateMap)

        delegateMapPoints = Painter()
        self.main_window.ui.mapPointsTable.setItemDelegate(delegateMapPoints)

        self.main_window.ui.clearMapTableButton.clicked.connect(self.clearMapTable)
        self.main_window.ui.injectMapButton.clicked.connect(self.injectMap)
        self.main_window.ui.saveMapFileButton.clicked.connect(self.saveMap)

        self.main_window.ui.mapPointsTable.cellClicked.connect(self.handleRMMCellClick)
        self.main_window.ui.mainNewPositionText.returnPressed.connect(lambda: self.main_window.ui.mainNewPositionText.clearFocus())
        self.main_window.ui.setPositionButton.clicked.connect(self.setEncoderPosition)
        self.main_window.ui.zeroPositionButton.clicked.connect(lambda:   self.main_window.ui_comms.sendMessage(MessageID.DIAGNOSTIC_REQUEST, "H4i", [DiagRequests.DIAG_REQ_RESET_POSITION.value, 0, 0, 0, 0], SrcDest.SRC_DEST_X04, MsgMode.SET))

        self.main_window.ui.disableModeButton.clicked.connect(lambda:    self.main_window.ui_comms.sendMessage(MessageID.RMM_MAP_MODE, "B", [MapOperationalMode.DISABLED.value], SrcDest.SRC_DEST_X04, MsgMode.SET))
        self.main_window.ui.editModeButton.clicked.connect(lambda:       self.main_window.ui_comms.sendMessage(MessageID.RMM_MAP_MODE, "B", [MapOperationalMode.EDITING.value], SrcDest.SRC_DEST_X04, MsgMode.SET))
        self.main_window.ui.findModeButton.clicked.connect(lambda:       self.main_window.ui_comms.sendMessage(MessageID.RMM_MAP_MODE, "B", [MapOperationalMode.POSITION_FINDING.value], SrcDest.SRC_DEST_X04, MsgMode.SET))
        self.main_window.ui.restrictModeButton.clicked.connect(lambda:   self.main_window.ui_comms.sendMessage(MessageID.RMM_MAP_MODE, "B", [MapOperationalMode.RESTRICTED.value], SrcDest.SRC_DEST_X04, MsgMode.SET))
        self.main_window.ui.deleteMapPoint.clicked.connect(self.deletePoint)
        self.main_window.ui.wipeMapButton.clicked.connect(self.wipeMap)
        self.main_window.ui.loadMapButton.clicked.connect(lambda: self.main_window.ui_comms.sendMessage(MessageID.RMM_REPORT, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ))
        self.main_window.ui.saveMapButton.clicked.connect(lambda: self.main_window.ui_comms.sendMessage(MessageID.RMM_SAVE_MAP, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ))
        self.main_window.ui.locateBoardingButton.clicked.connect(lambda: self.findPosition("Boarding"))
        self.main_window.ui.locateParkingButton.clicked.connect(lambda:  self.findPosition("Parking"))
        self.main_window.ui.locateNextRailButton.clicked.connect(lambda: self.findPosition("NextRail"))
        self.main_window.ui.locateRemoteAButton.clicked.connect(lambda:  self.findPosition("RemoteA"))
        self.main_window.ui.locateRemoteBButton.clicked.connect(lambda:  self.findPosition("RemoteB"))
        self.main_window.ui.locateRemoteCButton.clicked.connect(lambda:  self.findPosition("RemoteC"))
        self.main_window.ui.locateRemoteDButton.clicked.connect(lambda:  self.findPosition("RemoteD"))

        self.main_window.ui.boardingPointButton.clicked.connect(lambda:  self.addPoint("Boarding"))
        self.main_window.ui.parkingPointButton.clicked.connect(lambda:   self.addPoint("Parking"))
        self.main_window.ui.halfSpeedPointButton.clicked.connect(lambda: self.addPoint("HalfSpeed"))
        self.main_window.ui.partFoldPointButton.clicked.connect(lambda:  self.addPoint("PartialUnfold"))

        self.modeOptions = []
        self.railMapPoints = []
        self.modeOptions.append(self.main_window.ui.modeEnabledButton)
        self.modeOptions.append(self.main_window.ui.modeBoardingPointButton)
        self.modeOptions.append(self.main_window.ui.modeParkingPointButton)
        self.modeOptions.append(self.main_window.ui.modeUnpackButton)
        self.modeOptions.append(self.main_window.ui.modeSwivelLeftButton)
        self.modeOptions.append(self.main_window.ui.modeSwivelRightButton)
        self.modeOptions.append(self.main_window.ui.modePartialUnfoldButton)
        self.modeOptions.append(self.main_window.ui.modeHalfSpeedButton)
        self.modeOptions.append(None) # Unused bit 8
        self.modeOptions.append(None) # Unused bit 9
        self.modeOptions.append(self.main_window.ui.modeFullSwivelButton)
        self.modeOptions.append(self.main_window.ui.modeRemoteAButton)
        self.modeOptions.append(self.main_window.ui.modeRemoteBButton)
        self.modeOptions.append(self.main_window.ui.modeRemoteCButton)
        self.modeOptions.append(self.main_window.ui.modeRemoteDButton)
        self.modeOptions.append(None) # Unused bit 15
        self.main_window.ui.copyPositionButton.clicked.connect(self.copyCurrentPosition)
        self.main_window.ui.updatePointButton.clicked.connect(self.updatePoint)

        self.rmmTimer = QtCore.QTimer()
        self.rmmTimer.timeout.connect(self.periodicRMMRequests)
        self.rmmTimer.start(1000)

        self.maxRailMapPoints = 10
        self.highlightedMapPoint = -1

        self.setStyleSheetUIRailMap()
        self.populateMapTables()


    def setStyleSheetUIRailMap(self):
        """
        Sets the style sheet for the UIRailMap tables.
        Only doing additional stuff to items here that would not work in QTCreator.
        """
        tables = [self.main_window.ui.mapDataTable, self.main_window.ui.mapPointsTable]

        for table in tables:
            header = table.horizontalHeader()
            if table == self.main_window.ui.mapDataTable:
                header = table.horizontalHeader()
                header.setSectionResizeMode(0, QHeaderView.Fixed)
                header.setSectionResizeMode(1, QHeaderView.Stretch)
                header.setVisible(False) # Once header is set, remove visibility, this is intended for this table.

                table.setColumnWidth(0, 120)

                # Disable the built-in grid, will customise with the delegate class.
                table.setShowGrid(False)

                # Refine the style sheet.
                table.setStyleSheet(f"""
                QTableWidget {{
                    border: 2px solid {Colours.BLACK.name()};
                    background: {Colours.BEIGE.name()};
                }}
                """)

            elif table == self.main_window.ui.mapPointsTable:
                header.setSectionResizeMode(0, QHeaderView.Fixed)
                header.setSectionResizeMode(1, QHeaderView.Stretch)
                header.setSectionResizeMode(2, QHeaderView.Fixed)
                header.setFixedHeight(20)

                table.setColumnWidth(0, 40)
                table.setColumnWidth(2, 80)

                # Disable the built-in grid, will customise with the delegate class.
                table.setShowGrid(False)

                # Refine the style sheet. Focusing really on the header.
                table.setStyleSheet(f"""
                QTableWidget {{
                    border: 2px solid {Colours.BLACK.name()};               /* Border of the table */
                    background: {Colours.BEIGE.name()};                     /* Background colour of table */
                }}
                QHeaderView::section {{
                    background-color: {Colours.ICTERINE.name()};            /* Background colour of the header */
                    border: none;                                           /* Border of the header */
                    border-right: 1px solid {Colours.BLACK.name()};         /* Right border of the header. Splits columns visually */
                    border-bottom: 2px solid {Colours.BLACK.name()};        /* Bottom border of the header */
                    color: {Colours.BLACK.name()};                          /* Text colour of the header */
                    font-weight: normal;                                    /* Font weight of the header text */
                }}
                QHeaderView::section:last {{
                    border-right: none;                                     /* Remove the right border from the last header section. This is because of an overlap with the table widget border */
                }}
                """)


    def populateMapTables(self):
        """
        Populates the rail map table with the variable ID's.
        """
        tables = [self.main_window.ui.mapDataTable, self.main_window.ui.mapPointsTable]

        for table in tables:
            if table == self.main_window.ui.mapDataTable:
                table.setRowCount(len(RailMap))
                row = 0

                # Setup each row.
                for _, var in enumerate(RailMap):
                    # Column 0 is not editable.
                    column0 = QTableWidgetItem(var.name)
                    column0.setFlags(Qt.ItemIsEnabled)
                    table.setItem(row, 0, column0)

                    # Column 1 is not editable.
                    column1 = QTableWidgetItem("")
                    column1.setFlags(Qt.ItemIsEnabled)
                    table.setItem(row, 1, column1)

                    row += 1

                # Force additional settings to rows/columns after populated.
                for row in range(self.main_window.ui.mapDataTable.rowCount()):
                    table.setRowHeight(row, 18)

                    # Row colours.
                    table.item(row, 0).setBackground(Colours.BEIGE)
                    table.item(row, 1).setBackground(Colours.BEIGE)

                    table.item(row, 0).setForeground(Colours.BLACK)
                    table.item(row, 1).setForeground(Colours.BLACK)

                    # Column alignment.
                    for col in range(table.columnCount()):
                        alignment = Qt.AlignLeft if col == 0 else Qt.AlignHCenter
                        alignment |= Qt.AlignVCenter
                        table.item(row, col).setTextAlignment(alignment)

            elif table == self.main_window.ui.mapPointsTable:
                table.setRowCount(self.maxRailMapPoints)
                row = 0

                # Setup each row.
                for _ in range(self.maxRailMapPoints):
                    # Column 0 is not editable.
                    column0 = QTableWidgetItem("")
                    column0.setFlags(Qt.ItemIsEnabled)
                    table.setItem(row, 0, column0)

                    # Column 1 is not editable.
                    column1 = QTableWidgetItem("")
                    column1.setFlags(Qt.ItemIsEnabled)
                    table.setItem(row, 1, column1)

                    # Column 2 is not editable.
                    column2 = QTableWidgetItem("")
                    column2.setFlags(Qt.ItemIsEnabled)
                    table.setItem(row, 2, column2)

                    table.setRowHidden(row, True)  # Hide the row initially until the map has been loaded with its points.

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
        self.resizeMapTableToContent(self.main_window.ui.mapDataTable)
        self.resizeMapTableToContent(self.main_window.ui.mapPointsTable)


    def resizeMapTableToContent(self, table):
        """
        Resizes the default table size (in UI file) to the total number of rows. Moves the bottom frame and the buttons to positions based on the new table size.
        """
        if table == self.main_window.ui.mapPointsTable:
            tableRowCount = self.maxRailMapPoints
            tableRowHeight = 18
        else:
            tableRowCount = table.rowCount()
            tableRowHeight = table.rowHeight(0)

        tableHeaderHeight = table.horizontalHeader().height()
        tableFrameWidth = table.frameWidth()
        tableTotalHeight = tableHeaderHeight + (tableRowCount * tableRowHeight) + (2 * tableFrameWidth)
        table.setFixedHeight(tableTotalHeight)


    def periodicRMMRequests(self):
        """
        Periodically sends requests for RMM data.
        """
        self.main_window.ui_comms.sendMessage(MessageID.RMM_POSITION_REPORT, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET)
        self.main_window.ui_comms.sendMessage(MessageID.RMM_MAP_MODE, "", [], SrcDest.SRC_DEST_X04, MsgMode.GET)


    def clearMapTable(self):
        """
        Clears the map table and relevant data.
        """
        if self.main_window.ui.mapPointsTable.columnCount() > 0 and self.highlightedMapPoint != -1:
            for i in range(self.main_window.ui.mapPointsTable.columnCount()): # First, clear any highlighted rows of the old map. Must have a map in the first place and a row is selected.
                item = self.main_window.ui.mapPointsTable.item(self.highlightedMapPoint, i)
                item.setBackground(Colours.BEIGE)

        # Hide all rows in table
        for i in range(self.maxRailMapPoints):
            self.main_window.ui.mapPointsTable.setRowHidden(i, True)

        self.railMapPoints.clear()
        self.highlightedMapPoint = -1
        self.clearModePane()


    def injectMap(self):
        """
        Injects a map file into the map points table.
        """
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Inject Map", "MapFiles", "Map Files (*.map)")

        self.main_window.ui_console.logDebugConsole(f"Injecting {file_path}")

        if file_path:
            # Read file and apply values to each point
            with open(file_path, 'r') as f:
                # Clear the map first.
                self.clearMapTable()

                for i, line in enumerate(f):
                    if i < self.maxRailMapPoints:
                        line = line.strip()
                        # Skip empty lines.
                        if not line:
                            continue

                        line = line.split(',', 2) # Split the first two commas.

                        if len(line) == 3:
                            pointID = int(line[0].strip())
                            mode = int(line[1].strip())
                            position = int(line[2].strip())

                        self.main_window.ui_console.logDebugConsole(f"{pointID}, {mode}, {position}")

                        if mode & RailMapModes.BOARDING.value and mode & RailMapModes.PARKING.value:
                            convertedPointType = "Boarding/Parking"
                        elif mode & RailMapModes.BOARDING.value:
                            convertedPointType = "Boarding"
                        elif mode & RailMapModes.PARKING.value:
                            convertedPointType = "Parking"
                        elif mode & RailMapModes.HALF_SPEED_ZONE.value:
                            convertedPointType = "Half Speed Zone"
                        elif mode & RailMapModes.PARTIAL_UNFOLD_ZONE.value:
                            convertedPointType = "Partial Unfold Zone"
                        else:
                            convertedPointType = "Unspecified"

                        # Add point to table.
                        self.main_window.ui.mapPointsTable.setRowHidden(i, False)
                        self.main_window.ui.mapPointsTable.item(i, 0).setText(f"{pointID}")
                        self.main_window.ui.mapPointsTable.item(i, 1).setText(f"{convertedPointType}")
                        self.main_window.ui.mapPointsTable.item(i, 2).setText(f"{position}")

                        # Also add point to list.
                        self.railMapPoints.append([mode, position])

            self.main_window.ui_console.logDebugConsole(f"All Points: {self.railMapPoints}")


    def saveMap(self):
        """
        Saves the current points in the table into a map file.
        """
        mapDir = "MapFiles"
        if not os.path.exists(mapDir):
            os.makedirs(mapDir)

        file_path, _ = QFileDialog.getSaveFileName(self.main_window, "Save Map", mapDir, "Map Files (*.map)")

        if file_path:
            self.main_window.ui_console.logDebugConsole(f"Saving map {file_path}")

            # First wipe the current map.
            self.main_window.ui_comms.sendMessage(MessageID.RMM_DELETE_ALL, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ)

            # Create buffer.
            buffer = []
            for i, point in enumerate(self.railMapPoints):
                try:
                    # Appends for each point: ID, mode, position.
                    buffer.append(f"{i},{self.railMapPoints[i][0]},{self.railMapPoints[i][1]}")
                except Exception as e:
                    print(f"E1: {__file__}: {e}")

            # Write buffer to file.
            try:
                with open(file_path, 'w') as f:
                    for line in buffer:
                        f.write(line + "\n")
            except Exception as e:
                print(f"E2: {__file__}: {e}")


    def updateRailMapCurrentPoint(self, msg):
        """
        Handles rail map positions based on the reported data.

        Args:
            msg: The message to unpack.
        """
        # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
        if MsgMode(msg[5]) == MsgMode.GET_ACK:
            payload = unpackMessagePayload("i3B3h12B", msg)

            self.main_window.ui.mapDataTable.item(7, 1).setText(str(payload[0])) # Current position
            self.main_window.ui.mapDataTable.item(1, 1).setText(str(payload[1])) # Num of stops
            self.main_window.ui.mapDataTable.item(2, 1).setText(str(payload[2])) # Left stop index
            self.main_window.ui.mapDataTable.item(3, 1).setText(str(payload[3])) # Right stop index
            self.main_window.ui.mapDataTable.item(4, 1).setText(str(payload[4])) # Gyro X
            self.main_window.ui.mapDataTable.item(5, 1).setText(str(payload[5])) # Gyro Y
            self.main_window.ui.mapDataTable.item(6, 1).setText(str(payload[6])) # Gyro Z

            self.main_window.ui.leftStopButton.setChecked(payload[7])
            self.main_window.ui.rightStopButton.setChecked(payload[8])
            self.main_window.ui.middleStopButton.setChecked(payload[9])

            self.main_window.ui.parkPointButton.setChecked(payload[10])
            self.main_window.ui.halfSpeedButton.setChecked(payload[11])
            self.main_window.ui.partialUnfoldZoneButton.setChecked(payload[12])
            self.main_window.ui.unpackArrivalButton.setChecked(payload[13])

            self.main_window.ui.swivelLeftButton.setChecked(payload[14])
            self.main_window.ui.swivelRightButton.setChecked(payload[15])

            self.main_window.ui.swivelFullAngleButton.setChecked(payload[16])
            self.main_window.ui.partialUnfoldLeftButton.setChecked(payload[17])
            self.main_window.ui.partialUnfoldRightButton.setChecked(payload[18])


    def setEncoderPosition(self):
        """
        Sets new position of encoder based on the value in the text box.
        """
        if self.main_window.ui.mainNewPositionText.text() == "":
            return
        valid = True
        try:
            newPosition = int(self.main_window.ui.mainNewPositionText.text())
        except Exception as e:
            valid = False
            print(f"E3: {__file__}: {e}")

        if valid:
            if self.main_window.ui_config.getATEMode():
                self.main_window.ui_comms.sendMessage(MessageID.ATE_REQUEST, "H4i", [ATERequests.ATE_MAIN_DRIVE_SET_POSITION.value, newPosition, 0, 0, 0], SrcDest.SRC_DEST_X04, MsgMode.SET)
            else:
                self.main_window.ui_comms.sendMessage(MessageID.DIAGNOSTIC_REQUEST, "H4i", [DiagRequests.DIAG_REQ_RESET_POSITION.value, newPosition, 0, 0, 0], SrcDest.SRC_DEST_X04, MsgMode.SET)
            self.main_window.ui.mainNewPositionText.clear()


    def updateRMMMapMode(self, msg):
        """
        Updates the map operational mode.

        Args:
            msg: The message to unpack
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                payload = unpackMessagePayload("B", msg)

                mapMode = payload[0]
                opModeState = "Unknown"
                rowBackgroundColour = Colours.LIGHT_PINK

                if MapOperationalMode(mapMode) == MapOperationalMode.DISABLED:
                    opModeState = "Disabled"
                    rowBackgroundColour = Colours.LIGHT_PINK
                elif MapOperationalMode(mapMode) == MapOperationalMode.EDITING:
                    opModeState = "Editing"
                    rowBackgroundColour = Colours.GOLDEN_YELLOW
                elif MapOperationalMode(mapMode) == MapOperationalMode.POSITION_FINDING:
                    opModeState = "Position Finding"
                    rowBackgroundColour = Colours.PASTEL_PINK
                elif MapOperationalMode(mapMode) == MapOperationalMode.RESTRICTED:
                    opModeState = "Restricted"
                    rowBackgroundColour = Colours.PALE_GREEN

                self.main_window.ui.mapDataTable.item(0, 1).setBackground(rowBackgroundColour)
                self.main_window.ui.mapDataTable.item(0, 1).setText(opModeState)
        except Exception as e:
            print(f"E4: {__file__}: {e}")


    def deletePoint(self):
        """
        Deletes chosen map point.
        """
        if self.main_window.ui.confirmDeletePointButton.isChecked():
            if self.highlightedMapPoint != -1:
                self.main_window.ui_comms.sendMessage(MessageID.RMM_DELETE_POINT, "B", [self.highlightedMapPoint], SrcDest.SRC_DEST_X04, MsgMode.REQ)
            else:
                self.main_window.ui_console.logDebugConsole("No point selected!")


    def wipeMap(self):
        """
        Wipes the whole map.
        """
        if self.main_window.ui.confirmWipeMapButton.isChecked():
            self.main_window.ui_comms.sendMessage(MessageID.RMM_DELETE_ALL, "", [], SrcDest.SRC_DEST_X04, MsgMode.REQ)


    def updateRMMMap(self, msg):
        """
        Updates the map point table with the data.

        Args:
            msg: The message to unpack.
        """
        try:
            # Ignore any messages where the mode is not get ack. Note, this is the 5th element as it's not unpacked yet.
            if MsgMode(msg[5]) == MsgMode.GET_ACK:
                payload = unpackMessagePayload("B Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii Ii", msg)

                numPoints = payload[0]
                points = payload[1:]

                # New map data incoming, reset any old map related data.
                self.clearMapTable()

                if numPoints == 0:
                    self.main_window.ui.mapPointsTable.setRowHidden(0, False)
                    self.main_window.ui.mapPointsTable.item(0, 0).setText(f"Null")
                    self.main_window.ui.mapPointsTable.item(0, 1).setText(f"Empty Map")
                    self.main_window.ui.mapPointsTable.item(0, 2).setText(f"Null")
                    numPoints = 1 # Set to 1 so that when we hide the remaining rows it keeps the empty map row.
                else:
                    for i in range(numPoints):
                        mode = points[i * 2] # Point mode is first element of the pair.
                        position = points[(i * 2) + 1] # Point position is second element of the pair.

                        if mode & RailMapModes.BOARDING.value and mode & RailMapModes.PARKING.value:
                            convertedPointType = "Boarding/Parking"
                        elif mode & RailMapModes.BOARDING.value:
                            convertedPointType = "Boarding"
                        elif mode & RailMapModes.PARKING.value:
                            convertedPointType = "Parking"
                        elif mode & RailMapModes.HALF_SPEED_ZONE.value:
                            convertedPointType = "Half Speed Zone"
                        elif mode & RailMapModes.PARTIAL_UNFOLD_ZONE.value:
                            convertedPointType = "Partial Unfold Zone"
                        else:
                            convertedPointType = "Unspecified"

                        self.railMapPoints.append([mode, position]) # Store point data to buffer. This will allow the GUI to select each point and find out the modes it has set.

                        # Unhide the rows and assign points to the map table.
                        self.main_window.ui.mapPointsTable.setRowHidden(i, False)
                        self.main_window.ui.mapPointsTable.item(i, 0).setText(f"{i}")
                        self.main_window.ui.mapPointsTable.item(i, 1).setText(f"{convertedPointType}")
                        self.main_window.ui.mapPointsTable.item(i, 2).setText(f"{position}")

                # Hide the remaining available rows that have no data.
                for i in range(numPoints, self.maxRailMapPoints):
                    self.main_window.ui.mapPointsTable.setRowHidden(i, True)
                self.main_window.ui_console.logDebugConsole(f"All Points: {self.railMapPoints}")
        except Exception as e:
            print(f"E5: {__file__}: {e}")


    def handleRMMCellClick(self):
        """
        Handles the cell click event for the RMM table. The user has clicked on a cell in the table requesting to select that row for potential editing.
        """
        currentRow = self.main_window.ui.mapPointsTable.currentRow()

        # Current row is already selected, intent must be to deselect.
        if currentRow == self.highlightedMapPoint:
            for i in range(self.main_window.ui.mapPointsTable.columnCount()):
                item = self.main_window.ui.mapPointsTable.item(self.highlightedMapPoint, i)
                item.setBackground(Colours.BEIGE)
            self.highlightedMapPoint = -1
            self.updatePointModes() # Ensure to clear the pane here.
            return

        # Reset the background of the previously highlighted row.
        if self.highlightedMapPoint != -1:
            for i in range(self.main_window.ui.mapPointsTable.columnCount()):
                item = self.main_window.ui.mapPointsTable.item(self.highlightedMapPoint, i)
                item.setBackground(Colours.BEIGE)

        # Highlight the newly selected row.
        for i in range(self.main_window.ui.mapPointsTable.columnCount()):
            item = self.main_window.ui.mapPointsTable.item(currentRow, i)
            item.setBackground(Colours.PALE_GREEN)

        self.highlightedMapPoint = currentRow
        self.updatePointModes()


    def clearModePane(self):
        """
        Clears the mode options pane.
        """
        for i in range(len(self.modeOptions)):
            if self.modeOptions[i] is not None:
                self.modeOptions[i].setChecked(False)
        self.main_window.ui.zoneWidthText.clear()
        self.main_window.ui.newPointPositionText.clear()


    def updatePointModes(self):
        """
        Updates the current mode settings for the chosen point.
        """
        if self.highlightedMapPoint != -1 and self.highlightedMapPoint < len(self.railMapPoints):
            # Update the mode options for the selected point.
            mode = self.railMapPoints[self.highlightedMapPoint][0] # Mode is the 0th element of each row.

            for i in range(len(self.modeOptions)):
                if self.modeOptions[i] is not None:
                    self.modeOptions[i].setChecked(mode & (1 << i))

            zoneWidth = ((mode >> 16) * 127) / 11.15126765
            self.main_window.ui.zoneWidthText.setText(f"{zoneWidth:.2f}")

            self.main_window.ui_console.logDebugConsole(f"Getting Point: {self.highlightedMapPoint} - {mode}")
        else:
            self.clearModePane()


    def updatePoint(self):
        """
        Updates the mode options for selected point.
        """
        if self.highlightedMapPoint != -1:
            mode = 0
            zoneWidth = int(round(float(self.main_window.ui.zoneWidthText.text()) / 11.15126765))

            # Attempt to get position from the user inputted text box, if it is empty, default to original position of this point.
            if self.main_window.ui.newPointPositionText.text():
                position = int(self.main_window.ui.newPointPositionText.text())
            else:
                position = int(self.main_window.ui.mapPointsTable.item(self.highlightedMapPoint, 2).text())

            for i in range(len(self.modeOptions)):
                if self.modeOptions[i] is not None:
                    mode = mode | ((1 << i) if self.modeOptions[i].isChecked() else 0)

            mode = mode | (zoneWidth << 16)

            self.main_window.ui_console.logDebugConsole(f"Saving Point: {self.highlightedMapPoint} - {mode},  {position}")

            self.main_window.ui_comms.sendMessage(MessageID.RMM_UPDATE_POINT, "2BIi", [self.highlightedMapPoint, 0, mode, position], SrcDest.SRC_DEST_X04, MsgMode.SET)
        else:
            self.main_window.ui_console.logDebugConsole("No point selected!")


    def addPoint(self, pointType):
        """
        Adds a new point to the map with the given type.

        Args:
            pointType: The type of point to add.
        """
        if self.main_window.ui.specifyPositionButton.isChecked():
            try:
                position = int(self.main_window.ui.positionToSpecifyText.text())
                msg = MessageID.RMM_NEW_POINT_AT_POS
            except Exception as e:
                print(f"E6: {__file__}: {e}")
                return
        else:
            position = 0
            msg = MessageID.RMM_NEW_POINT

        if pointType == "Boarding":
            mode = RailMapModes.BOARDING.value
        elif pointType == "Parking":
            mode = RailMapModes.PARKING.value
        elif pointType == "HalfSpeed":
            mode = RailMapModes.HALF_SPEED_ZONE.value
        else:
            mode = RailMapModes.PARTIAL_UNFOLD_ZONE.value

        self.main_window.ui_comms.sendMessage(msg, "Ii", [mode, position], SrcDest.SRC_DEST_X04, MsgMode.SET)


    def findPosition(self, pointType):
        """
        Finds the next point in the chosen direction.

        Args:
            pointType: The type of point to find.
        """
        if pointType == "Boarding":
            pointID = 0
        elif pointType == "Parking":
            pointID = 1
        elif pointType == "RemoteA":
            pointID = 2
        elif pointType == "RemoteB":
            pointID = 3
        elif pointType == "RemoteC":
            pointID = 4
        elif pointType == "RemoteD":
            pointID = 5
        else:
            pointID = 6

        if self.main_window.ui.findLeftPosButton.isChecked():
            direction = 0
        elif self.main_window.ui.findRightPosButton.isChecked():
            direction = 1
        else:
            direction = 2

        self.main_window.ui_comms.sendMessage(MessageID.RMM_POSITION_QUERY, "BB", [pointID, direction], SrcDest.SRC_DEST_X04, MsgMode.SET)


    def copyCurrentPosition(self):
        """
        Copies the current encoder position to the new position text box for updating new point mode data.
        """
        self.main_window.ui.newPointPositionText.setText(self.main_window.ui.mapDataTable.item(7, 1).text())


    def handleRMMResponseMessage(self, msg):
        """
        Handles the RMM response from a request sent.

        Args:
            msg: The message to unpack.
        """
        # Get the message ID.
        match(MessageID(msg[0])):
            case MessageID.RMM_DELETE_ALL:
                message = "Rail Map - Delete All"
            case MessageID.RMM_UPDATE_POINT:
                message = "Rail Map - Update Point"
            case MessageID.RMM_NEW_POINT:
                message = "Rail Map - New Point"
            case MessageID.RMM_DELETE_POINT:
                message = "Rail Map - Delete Point"
            case MessageID.RMM_SAVE_MAP:
                message = "Rail Map - Map Saved"
            case MessageID.RMM_NEW_POINT_AT_POS:
                message = "Rail Map - New Point at Position"
            case MessageID.RMM_POSITION_QUERY:
                message = "Rail Map - Position Query"

        # Check for mode type. Note, this is the 5th element as it's not unpacked yet.
        colour = "green"
        match(MsgMode(msg[5])):
            case MsgMode.GET_ACK:
                mode = "GET_ACK received"
            case MsgMode.SET_ACK:
                mode = "SET_ACK received"
            case MsgMode.REQ_ACK:
                mode = "REQ_ACK received"
            case MsgMode.NACK:
                mode = "NACK received"
                colour = "red"

        self.main_window.ui_console.logDebugConsole(f"{message}{CSS.START_STYLE}color: {colour};{CSS.START_STYLE_END} - {mode}{CSS.END_STYLE}")
