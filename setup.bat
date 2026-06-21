@echo off
cd /d "%~dp0"
setlocal enabledelayedexpansion

echo.
echo ===== Mailer Setup & Installation =====
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python version:
python --version

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo.
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo.
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

REM Verify Flask installation
echo.
echo Verifying Flask installation...
python -c "import flask; print('Flask version:', flask.__version__)"
if errorlevel 1 (
    echo ERROR: Flask verification failed
    pause
    exit /b 1
)

REM Verify pytest installation
echo.
echo Verifying pytest installation...
python -c "import pytest; print('pytest version:', pytest.__version__)"
if errorlevel 1 (
    echo WARNING: pytest not installed, but continuing...
)

echo.
echo ===== Installation Complete =====
echo.
echo Virtual environment: venv\
echo.
echo Next steps:
echo 1. Run setup tests: python -m pytest tests\
echo 2. Start the application: run.bat
echo.
echo For manual commands:
echo   - Activate venv: venv\Scripts\activate.bat
echo   - Install packages: pip install PACKAGE_NAME
echo.

pause
endlocal
