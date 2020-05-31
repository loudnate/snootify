#!/usr/bin/env sh

# Create the virtual environment (will succeed silently if exists)
python3 -m venv /usr/local/snoopi

# Activate the environment. (will also succeed silently if already activated)
source /usr/local/snoopi/bin/activate

# install the package and its dependencies
python3 setup.py install
