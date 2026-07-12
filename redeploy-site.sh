#!/bin/bash

# 1. cd into your project folder
cd ~/team1-portfolio-henrique || exit

# 2. Grab the latest changes from GitHub and force reset
git fetch && git reset origin/main --hard

# 3. Ensure dependencies are up to date
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 4. Restart the systemd service to pick up changes
systemctl restart myportfolio