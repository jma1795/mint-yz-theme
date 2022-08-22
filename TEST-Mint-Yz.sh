#!/bin/bash

sudo rm -rf /usr/share/themes/Mint-Yz-*
sudo cp -R usr/share/themes/* /usr/share/themes

# Force refresh
gsettings set org.cinnamon.desktop.interface gtk-theme 'Mint-Y'
gsettings set org.cinnamon.desktop.interface gtk-theme 'Mint-Yz-Base-Aqua'

gsettings set org.cinnamon.theme name 'Mint-Y'
gsettings set org.cinnamon.theme name 'Mint-Yz-Dark-Aqua'
