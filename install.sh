#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo -e "Installing KvLibadwaita as a \033[1muser\033[0m. Is this what you want? (y/n)"
    read -p "" -n 1 -r
    echo "" # New line
    if [[ $REPLY =~ ^[Yy]$ ]]
    then # Install theme as user
        cp -r ./src/* ~/.config/Kvantum/
        MESSAGE="Installation complete."
    else # Don't install theme as user
        MESSAGE="Installation aborted."
    fi
else
    echo -e "Installing KvLibadwaita as \033[1mroot\033[0m. Is this what you want? (y/n)"
    read -p "" -n 1 -r
    echo "" # New line
    if [[ $REPLY =~ ^[Yy]$ ]]
    then # Install theme as user
        cp -r ./src/* /usr/share/Kvantum/
        MESSAGE="Installation complete."
    else # Don't install theme as user
        MESSAGE="Installation aborted."
    fi
fi

echo -e $MESSAGE
