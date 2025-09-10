from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainterPath, QRegion
from PySide6.QtWidgets import QLabel, QStyle, QStyledItemDelegate
from UI.ui_styling import Colours


class Painter(QStyledItemDelegate):
    """
    Custom delegate for table widgets, inheriting from QStyledItemDelegate.
    Enables custom painting of table cells (background, borders, text) and customizes the editor widget for a consistent and polished appearance.
    """

    def paint(self, painter, option, index):
        """
        Paints the specified cell with a custom border.

        Args:
            painter:    The painter object used for drawing.
            option:     The style options for the item.
            index:      The index of the cell being painted.
        """
        # Remove selection highlighting so the background remains unchanged.
        option.state &= ~QStyle.State_Selected

        # Save painter state.
        painter.save()

        # Retrieve background and text colour.
        bg = index.data(Qt.BackgroundRole) or Colours.DEFAULT
        fg = index.data(Qt.ForegroundRole) or Colours.BLACK

        # If fg is a QBrush, use its colour.
        if isinstance(fg, QtGui.QBrush):
            fg = fg.color()

        # Fill the entire cell area with the background colour.
        painter.fillRect(option.rect, bg)

        # Set up a pen for drawing borders.
        border_pen = QtGui.QPen(Colours.GRIDLINES, 1)
        painter.setPen(border_pen)

        # Get model dimensions.
        last_row = index.model().rowCount() - 1
        last_col = index.model().columnCount() - 1

        # Draw bottom border (only for cells that are not in the last row).
        if index.row() < last_row:
            bottom_line = option.rect.adjusted(0, option.rect.height() - 1, 0, 0)
            painter.drawLine(bottom_line.left(), bottom_line.top(), bottom_line.right(), bottom_line.top())

        # Draw right border (only for cells that are not in the last column).
        if index.column() < last_col:
            right_line = option.rect.adjusted(option.rect.width() - 1, 0, 0, 0)
            painter.drawLine(right_line.right(), right_line.top(), right_line.right(), right_line.bottom())

        # Draw the text.
        text = index.data(Qt.DisplayRole)
        if text:
            # Retrieve text alignment (default to center if not provided).
            alignment = index.data(Qt.TextAlignmentRole) or Qt.AlignCenter

            # Create a padded rectangle (2px left/right padding).
            padded_rect = option.rect.adjusted(2, 0, -2, 0)

            # Set the pen with the foreground colour.
            painter.setPen(QtGui.QPen(fg))
            painter.drawText(padded_rect, alignment, text)

        # Restore painter state.
        painter.restore()


    def createEditor(self, parent, option, index):
        """
        Creates and returns an editor widget for the item at the given index.
        This is needed to keep the styling of a cell the same when double-clicking to alter values.

        Args:
            parent: The parent widget.
            option: The style options for the item.
            index:  The index of the cell.
        """
        # Get the default editor.
        editor = super().createEditor(parent, option, index)

        # Remove any automatic background change while editing.
        # The transparent background will let the table's background show through.
        editor.setStyleSheet("background-color: transparent; border: none; color: black;")

        # If the editor is a QLineEdit, remove its frame. This gets rid of the underline when double clicking a cell.
        if hasattr(editor, "setFrame"):
            editor.setFrame(False)

        return editor


class ScalableLabel(QLabel):
    """
    Custom label widget inheriting from QLabel.
    ScalableLabel automatically rescales any displayed image to fit within the label's frame, preserving the aspect ratio. It also applies a rounded rectangle mask for a polished appearance.
    Inherits all QLabel functionality, allowing it to be used anywhere a QLabel would be used, but with enhanced image scaling and masking behaviour.
    """

    def __init__(self, parent=None, scale_mode=Qt.KeepAspectRatioByExpanding):
        """
        Initialises the scalable label.

        Args:
            parent:     The parent widget.
            scale_mode: The scaling mode to use when resizing the image.
        """
        super().__init__(parent)  # Initialises the QLabel base class, passing the parent widget if provided.
        self.original_pixmap = None
        self.scale_mode = scale_mode


    def setPixmap(self, pixmap):
        """
        Takes an input image and displays a scaled version within the label.

        Args:
            pixmap: The input image.
        """
        self.original_pixmap = pixmap
        # Scale to fill the label fully, preserving aspect ratio but expanding if necessary.
        scaled = pixmap.scaled(self.size(), self.scale_mode, Qt.SmoothTransformation)
        super().setPixmap(scaled)
        # Apply a rounded rectangle mask to match the frame's style.
        self.applyRoundedMask()


    def resizeEvent(self, event):
        """
        Handles resizing of the label and rescales the image accordingly.

        Args:
            event: The event containing data about the resize action.
        """
        if self.original_pixmap:
            # Scale the image to fill the label, preserving aspect ratio and expanding if necessary.
            scaled = self.original_pixmap.scaled(self.size(), self.scale_mode, Qt.SmoothTransformation)
            super().setPixmap(scaled)
        # Apply a rounded rectangle mask to match the frame's style.
        self.applyRoundedMask()
        super().resizeEvent(event)


    def applyRoundedMask(self):
        """
        Forces the image to be displayed as a rounded rectangle by applying a mask to the label.
        """
        # Create a rounded rectangle mask with a 10-pixel radius (The same border radius as the image frame).
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 10, 10)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)