# Standard library imports.
import os
import sys


def resource_path(relative_path):
    """
    Get the absolute path to a resource, works for development and for PyInstaller.

    Args:
        relative_path:  The relative path to the resource file.
    Returns:
        The absolute path to the resource file.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS.
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)