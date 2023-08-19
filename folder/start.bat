@echo off
title checkmate
color 03
echo Python 3.8 and higher required.
echo Make sure Python is in your PATH
pause
goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :NOPYTHON)
python -V | find "Python"    >NUL 2>NUL && (goto :HASPYTHON)

:NOPYTHON
cls
echo Python is not installed or is not in your PATH
pause
exit

:HASPYTHON
cls
color 0a
echo The following modules will be installed with pip/pip3
echo.
echo Discord Module
echo Requests Module
echo.
pause
cls
echo Installing Discord Module
python -m pip install discord
echo Installing Request Module
pip3 install requests
cls
python main.py