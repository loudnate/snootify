#!/usr/bin/env sh

VENV="snootipy"

# Create the virtual environment (will succeed silently if exists)
python3 -m venv "$HOME/$VENV"

# Activate the environment. (will also succeed silently if already activated)
source "$HOME/$VENV/bin/activate"

# run the default command
snootify send
