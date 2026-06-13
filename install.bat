:: This batch file checks for Python, Python 3 and PyGame, and then runs the game if it can. It won't install Python or anything else, only use for checking.

:: This script is designed for Windows users. For Linux/macOS, use the setup.yml Ansible playbook.

:: This bat file will preforme the following steps:
:: 1. Check if Python 3 is installed
:: 2. If Python 3 is not found, it will then try Python and if that doesn't work it will prompt the user to install it
:: 3. If Python is found, it will check for PyGame and install it if necessary
:: 4. And least but not last it will launch the game

:: How to run (terminal):
:: .\install.bat

@echo off
:: Check for Python 3 Installation
python3 --version 2>NUL
if errorlevel 1 goto tryPython

:: if python3 works, go straight to install
set PYTHON=python3
goto install

:tryPython
:: Try python instead
python --version 2>NUL
if errorlevel 1 goto errorNoPython
set PYTHON=python

:install
:: Install PyGame
echo Installing PyGame...
pip install pygame

:: Launch the game
echo Starting game...
%PYTHON% game.py
goto:eof

:errorNoPython
echo.
echo Error: Python 3 not installed
echo Please download it from https://www.python.org/downloads/
pause