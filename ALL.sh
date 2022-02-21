#!/bin/bash

set -e

echo "This script does all you need to update one new colour, or all."; echo

wrong_argument () {
	echo "You must run the script with a valid color name, or 'All'."
	echo "Example: './all.sh All' or './all.sh Purple'"; exit 1
}

color=$1
if [ ! $color ]
then
	wrong_argument
fi
if [ ! -d src/Mint-Y/variations/$color ] && [ "$color" != "All" ]
then
	wrong_argument
fi

echo "GIT STATUS:"
git status; echo
read -p "DO YOU WANT TO CONTINUE? (Y/N) " ok
if [ $ok == "n" ] || [ $ok == "N" ]
then
	exit 0
fi
echo "________________________________________________"; echo

# DELETE $color before updating to avoid any weird rewrite.
if [ $color == "All" ]
then
	rm -rf src/Mint-Y/variations/*
else
	rm -rf src/Mint-Y/variations/$color
fi
git add --all
git diff --staged --quiet || git commit --quiet -m "DELETE $color before updating to avoid any weird rewrite."

# UPDATE-VARIATIONS and COMMIT
./update-variations.py $color # || exit 1
echo
echo "GIT COMMIT: ADD src/Mint-Y/variations/$color"
git add src/Mint-Y/variations/* &&
git commit --quiet -m "ADD src/Mint-Y/variations/$color"
echo "________________________________________________"; echo

# GENERATE-THEMES and COPY
echo "NOW RUNNING generate-themes.py"; echo
./generate-themes.py && echo &&
echo "NOW COPYING FILES into /usr/share/themes as superuser" &&
sudo cp -rf usr/share/themes/Mint-Yz* /usr/share/themes
echo "________________________________________________"; echo
echo "GIT STATUS:"
git status
echo "________________________________________________"; echo

# REFRESH
read -p "LIGHT OR DARK VARIANT? (l/d) " variant
if [ $variant == "d" ] || [ $variant == "D" ]
then
	variant="Dark"
	gsettings set org.cinnamon.desktop.interface icon-theme "Mint-Y-Dark-Grey"
else
	variant="Base"
	gsettings set org.cinnamon.desktop.interface icon-theme "Mint-Y-Grey"
fi
gsettings set org.cinnamon.desktop.interface gtk-theme "Mint-X"
gsettings set org.cinnamon.desktop.interface gtk-theme "Mint-Yz-$variant-$color"

echo "ALL DONE !"
echo "________________________________________________"; echo
exit 0
