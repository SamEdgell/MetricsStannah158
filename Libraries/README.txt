Create virtual environment:
py -V:3.13 -m venv venv_313

Locate all libraries installed in this environment and print to file:
pip freeze > required_libraries.txt

Download all required libraries to this environment:
pip install -r Libraries\required_libraries.txt

