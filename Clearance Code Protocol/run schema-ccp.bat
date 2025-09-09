:StartCode
@echo off
title SCHEMA Clearance Code Protocol
python schema-ccp.py
echo.
CHOICE /C YN /M "Run code again?"
echo.
IF ERRORLEVEL 2 GOTO :EOF
IF ERRORLEVEL 1 GOTO StartCode