#!/bin/bash

echo "Setting up virtual environment and installing dependencies..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install Python 3.x."
    exit 1
fi

# Check if venv exists and create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        exit 1
    fi
fi

# Activate virtual environment and install requirements
echo "Activating virtual environment and installing requirements..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    exit 1
fi

echo "Dependencies installed successfully!"
echo "You can now run the script using: ./venv/bin/python your_script_name.py"
# Deactivate venv if desired, or let the user do it manually
# deactivate