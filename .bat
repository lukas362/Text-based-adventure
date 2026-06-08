:: This batch file checks for Python, Python 3 and PyGame, installs them if necessary, and then runs the game. It won't install Python.

:: This script is designed for Windows users. For Linux/macOS, use the setup.yml Ansible playbook.

:: How to run (terminal):
:: install_and_run.bat

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