# Standard library imports.
import datetime


class Logger:
    """
    Class for logging data to a specified file.
    Provides methods to write data, manage log file creation, set log folders, and ensure data is properly flushed and closed.
    """

    def __init__(self, filename_base):
        """
        Initialises the Logger class.

        Args:
            filename_base: The base name for the log file.
        """
        self.file = None
        self.name_base = filename_base
        self.columns = ""
        self.ext = ".csv"
        self.folder = None
        self.filename = ""


    def close(self):
        """
        Closes the log file if it is open. Ensures any buffered data is written and the file is properly closed.
        """
        if self.file:
            try:
                self.file.flush()
                self.file.close()
            except Exception as e:
                print(f"Error while closing the log file: {e}")
            finally:
                self.file = None


    def flush(self):
        """
        Ensures any buffered data is written to the log file.
        """
        if self.file:
            try:
                self.file.flush()
            except Exception as e:
                print(f"Error whilst flushing the log file: {e}")


    def getFilename(self):
        """
        Get the filename of the current log file.

        Returns:
            The filename of the current log file.
        """
        return self.filename


    def setFolder(self, folder):
        """
        Sets the folder for the current log file.

        Args:
            folder: The folder location to set.
        """
        self.folder = folder


    def getFolder(self):
        """
        Gets the folder location for this logger.

        Returns:
            The folder location.
        """
        return self.folder


    def write(self, data):
        """
        Writes the given data to the log file.

        Args:
            data: The data to write to the log file.
        """
        if self.file is None:
            # This is a new file, so set it up.
            if not self.folder:
                print("Error: Log folder is not set.")
                return
            self.filename = f"{self.folder}/{self.name_base}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}{self.ext}"
            self.file = open(self.filename, "w")
            self.file.write(f"{self.columns}\n")
            self.file.flush()
        try:
            self.file.write(f"{data}\n")
        except Exception as e:
            print(f"Error whilst writing to the log file: {e}")