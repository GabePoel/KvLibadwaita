#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo -e "Uninstalling KvLibadwaita as a \033[1muser\033[0m. Is this what you want? (y/n)"
    read -p "" -n 1 -r
    echo "" # New line
    if [[ $REPLY =~ ^[Yy]$ ]]
    then # Uninstall theme as user
        rm -R ~/.config/Kvantum/KvLibadwaita
        MESSAGE="Uninstallation complete."
    else # Don't uninstall theme as user
        MESSAGE="Uninstallation aborted."
    fi
else
    echo -e "Uninstalling KvLibadwaita as \033[1mroot\033[0m. Is this what you want? (y/n)"
    read -p "" -n 1 -r
    echo "" # New line
    if [[ $REPLY =~ ^[Yy]$ ]]
    then # Uninstall theme as user
        rm -R /usr/share/Kvantum/KvLibadwaita
        MESSAGE="Uninstallation complete."
    else # Don't uninstall theme as user
        MESSAGE="Uninstallation aborted."
    fi
fi

echo -e $MESSAGE
