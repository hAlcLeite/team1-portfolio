#!/bin/bash

# 1. Kill all existing tmux sessions
tmux kill-server 2>/dev/null

# 2. cd into your project folder
cd ~/team1-portfolio-henrique || exit

# 3. Grab the latest changes from GitHub and force reset
git fetch && git reset origin/main --hard

# 4. Create virtual environment if it doesn't exist, then activate and install deps
if [ ! -d "python3-virtualenv" ]; then
  python3 -m venv python3-virtualenv
fi
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 5. Start a new detached Tmux session, activate the venv, and start the Flask server
tmux new-session -d -s flask_app 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'