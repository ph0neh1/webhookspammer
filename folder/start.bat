@echo off
title cr.ghost
color 03
echo Discord Webhook Spammer created by Ph0neh1
echo Make sure you are running Python 3.8 or higher and Python is added to your PATH
echo.
echo https://github.com/ph0neh1/webhookspammer
echo.
pause
goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :NOPYTHON)
python -V | find "Python"    >NUL 2>NUL && (goto :HASPYTHON)

:NOPYTHON
cls
echo Python is not installed on your Windows system or not added to your PATH
pause
exit

:HASPYTHON
cls
color 0a
echo The following modules will be installed with pip3
echo Any module that is already installed will be skipped
echo.
echo Discord Module
echo Requests Module
echo.
pause
cls
echo Installing Discord Module
pip3 install Discord
echo Installing Request Module
pip3 install requests
cls
python main.py