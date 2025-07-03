@echo off
echo Setting up virtual environment and installing dependencies...

REM Check if Python is installed
python --version >NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not found. Please install Python 3.x from python.org and add it to your PATH.
    pause
    exit /b 1
)

REM Check if venv exists and create if not
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    if %ERRORLEVEL% NEQ 0 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM Activate virtual environment and install requirements
echo Activating virtual environment and installing requirements...
call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install dependencies.
    pause
    exit /b 1
)

echo Dependencies installed successfully!
echo You can now run the script using: .\venv\Scripts\python.exe your_script_name.py
pause