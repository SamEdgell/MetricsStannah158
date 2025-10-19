# Standard libraries.
import os
import shutil
import sys
from pathlib import Path

# Third party libraries.
import PyInstaller.__main__


try:
    print(f"Building executable...")

    # Ensure build directory is clean before building.
    dist_path = Path("./dist")
    if dist_path.exists():
        print("Cleaning existing dist directory...")
        shutil.rmtree(dist_path)

    build_path = Path("./build")
    if build_path.exists():
        print("Cleaning existing build directory...")
        shutil.rmtree(build_path)

    spec_path = Path("./Metrics.spec")
    if spec_path.exists():
        print("Cleaning existing .spec file...")
        spec_path.unlink()

    separator = os.pathsep

    # --- Define build parameters ---

    # List of data folders compulsory to include in the build.
    data_folders = [
        'General',      # Contains version.txt which is required.
        'Images',       # Contains application icons which are required.
        'PIDLogs',
        'Snapshots',
        'UI',           # Contains main_window.ui files which are required.
        'Utilities'     # Contains utility scripts which are required.
    ]

    # List of hidden imports compulsory to include in the build.
    hidden_imports = [
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'qasync'
    ]

    # List of arguments for PyInstaller.
    args = [
        'metrics.py',
        '--name=Metrics',
        '--clean',              # Clean PyInstaller cache and remove temporary files before building.
        '--console',            # Terminal window required.
        '--noconfirm',          # Overwrites previous build artifacts without asking.
        '--onefile',            # Create a one-file bundled executable.
    ]

    for folder in data_folders:
        args.append(f'--add-data={folder}{separator}{folder}')

    for module in hidden_imports:
        args.append(f'--hidden-import={module}')

    # --- Execute PyInstaller with the defined arguments ---
    PyInstaller.__main__.run(args)

    print("Build completed.")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)