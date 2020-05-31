#!/usr/bin/env bash

VENV="snootipy"

# Activate the environment. (will also succeed silently if already activated)
source "$HOME/$VENV/bin/activate"

# run the default command
snootify send
