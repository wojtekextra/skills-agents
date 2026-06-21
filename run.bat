@echo off
cd /d "%~dp0"
setlocal enabledelayedexpansion

echo.
echo ===== Mailer Application Launcher =====
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ and add it to system PATH
    pause
    exit /b 1
)

REM Activate virtual environment if available
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo WARNING: Virtual environment not found
    echo Please run: python -m venv venv
    echo.
)

REM Set environment variables
set FLASK_APP=mailer
set FLASK_ENV=development

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Flask is not installed
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

echo Starting Flask server...
echo Application will be available at: http://127.0.0.1:5000
echo Press Ctrl+C to stop the server
echo.

REM Start Flask server in a new window and open browser
start cmd /k python -m flask run

REM Wait a moment for server to start
timeout /t 3 /nobreak

REM Open browser
start http://127.0.0.1:5000

echo.
echo Browser should open automatically. If not, visit: http://127.0.0.1:5000
echo.

endlocal
