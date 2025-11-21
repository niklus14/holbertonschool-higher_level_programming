#!/usr/bin/env bash

# Function to install the script to /usr/local/bin
install_go_command() {
    if [ ! -w /usr/local/bin ]; then
        echo "Use sudo to write to /usr/local/bin"
        sudo cp "$0" /usr/local/bin/go
        sudo chmod +x /usr/local/bin/go
    else
        cp "$0" /usr/local/bin/go
        chmod +x /usr/local/bin/go
    fi
    echo "Take it easy"
    echo "Usage: go <commit message>"
}

# Install mode
if [ "$1" == "install" ]; then
    install_go_command
    exit 0
fi

# Main commit function
if [ -z "$1" ]; then
    echo "Usage: go <commit message>"
    exit 1
fi

# Commit and push to git repository
commit_message="$*"
git add .
git commit -m "$commit_message"
git push




