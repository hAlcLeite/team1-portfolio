#!/bin/bash

set -e

PROJECT_DIR="$HOME/team1-portfolio"
VENV_DIR="$PROJECT_DIR/python3-virtualenv"

cd "$PROJECT_DIR"

git fetch
git reset origin/main --hard

source "$VENV_DIR/bin/activate"
pip install -r requirements.txt

systemctl restart myportfolio
