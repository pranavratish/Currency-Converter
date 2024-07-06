#!/bin/bash
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies
pip3 install -r ../requirements.txt

# Run the app
python3 src/main.py

# Deactivate the virtual env
deactivate