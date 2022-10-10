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

y_hex_colors1["MintSoda"] = "#3DB884"
y_hex_colors2["MintSoda"] = "#3BB07F"

y_hex_colors1["MintGum"] = "#09A78D"
y_hex_colors2["MintGum"] = "#009980"

y_hex_colors1["Grey"] = "#767676"
y_hex_colors2["Grey"] = "#767676"

y_hex_colors1["Aqua"] = "#1F9EDE"
y_hex_colors2["Aqua"] = "#1F9EDE"

y_hex_colors1["BlueBelize"] = "#277CB7"
y_hex_colors2["BlueBelize"] = "#2471A8"

y_hex_colors1["BlueElectron"] = "#0C75DE"
y_hex_colors2["BlueElectron"] = "#0B6BCB"

y_hex_colors1["Purple"] = "#8245A1"
y_hex_colors2["Purple"] = "#8245A1"

y_hex_colors1["Red"] = "#F20D20"
y_hex_colors2["Red"] = "#E50012"

y_hex_colors1["Orange70s"] = "#E8602E"
y_hex_colors2["Orange70s"] = "#E8602E"

y_hex_colors1["Orange"] = "#FF791A"
y_hex_colors2["Orange"] = "#FF791A"

y_hex_colors1["Pink"] = "#EB47B4"
y_hex_colors2["Pink"] = "#EB47B4"
