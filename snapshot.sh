#!/bin/bash
set -e
# Generate project tree without node_modules or __pycache__
tree -I 'node_modules|__pycache__' > tree.txt
# Freeze Python packages
pip freeze > dune-backend/requirements.txt
# List top-level npm packages from the frontend directory
npm list --depth=0 --prefix chatbot-ui --omit=peer > chatbot-ui/npm-packages.txt 2>/dev/null
# Output git status and recent log
git status
git log --oneline -n 5
