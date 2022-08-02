#!/bin/bash

echo; echo; echo; echo

unzip -q mint-yz-theme*
echo "Please enter your password to remove any old Mint-Yz"
echo "and copy the new ones in /usr/share/themes"
sudo rm -rf /usr/share/themes/Mint-Yz-*
sudo cp -rf themes/* /usr/share/themes
echo
echo "Done."
echo "Select your new themes in"
echo "Menu > Preferences > Themes or Appearance"
echo
echo "You may need to close and re-open your windows"
echo "to refresh everything... Enjoy!"
