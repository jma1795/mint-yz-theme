#!/usr/bin/python3

# Mint-Y

# I can now delete y_hex_colors3 and y_hex_colors4 from the constants.py, generate-themes.py and update-
# variations.py. These were only used for the hover and pressed states on the old window close buttons, and
# those are not used anymore. I searched the whole directory, and now it can only be found in src/Mint-Y/
# gtk-3.0/assets.svg for these old close buttons. Deleting these will make less boring and repetitive work
# when modifying the constants.py. This is true here on Mint-Yz, maybe not on the upstream Mint-Y.

Y_HEX_ACCENT1 = ["#92b372"]  # BASE (You can't change these; sed uses them for search and replace.)
Y_HEX_ACCENT2 = ["#8fa876"]  # DARK (You can't change these; sed uses them for search and replace.)

y_hex_colors1 = {}
y_hex_colors2 = {}

y_hex_colors1["BlueBelize"] = "#297FB9"
y_hex_colors2["BlueBelize"] = "#2574A9"

y_hex_colors1["Grey"] = "#767676"
y_hex_colors2["Grey"] = "#767676"

y_hex_colors1["MintGum"] = "#09A78D"
y_hex_colors2["MintGum"] = "#009980"

y_hex_colors1["BlueElectron"] = "#0B84DA"
y_hex_colors2["BlueElectron"] = "#0070C0"

y_hex_colors1["Purple"] = "#8245A1"
y_hex_colors2["Purple"] = "#8B49AC"

y_hex_colors1["RedShine"] = "#F20D20"
y_hex_colors2["RedShine"] = "#E50013"

y_hex_colors1["OrangeShine"] = "#FF791A"
y_hex_colors2["OrangeShine"] = "#FF791A"

y_hex_colors1["AquaShine"] = "#009CCE"
y_hex_colors2["AquaShine"] = "#0090C0"

y_hex_colors1["Pink"] = "#F656A5"
y_hex_colors2["Pink"] = "#EB4798"
