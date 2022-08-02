#!/bin/bash

echo; echo; echo; echo
echo "Please enter your password to remove any old Mint-Yz"
echo "and copy the new ones in /usr/share/themes"
echo
sudo rm -rf /usr/share/themes/Mint-Yz-*
sudo cp -rf themes/* /usr/share/themes
echo
echo "Done."
echo "Now, select your new themes in"
echo "Menu > Preferences > Themes or Appearance"
echo
echo "You may need to close and re-open your windows"
echo "to refresh everything... Enjoy!"
