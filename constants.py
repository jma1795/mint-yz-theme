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

y_hex_colors1["BlueBelize"] = "#2980B9"
y_hex_colors2["BlueBelize"] = "#277AB0"

y_hex_colors1["Grey"] = "#767676"
y_hex_colors2["Grey"] = "#767676"

y_hex_colors1["MintSoda"] = "#29BF68"
y_hex_colors2["MintSoda"] = "#27B663"

y_hex_colors1["MintGum"] = "#1BBB9B"
y_hex_colors2["MintGum"] = "#1AB294"

y_hex_colors1["BlueElectron"] = "#0984E3"
y_hex_colors2["BlueElectron"] = "#097ED8"

y_hex_colors1["Purple"] = "#8F4CB1"
y_hex_colors2["Purple"] = "#8848A9"

y_hex_colors1["RedShine"] = "#FF1A2C"
y_hex_colors2["RedShine"] = "#F20D1F"

y_hex_colors1["OrangeShine"] = "#FF791A"
y_hex_colors2["OrangeShine"] = "#FF791A"

y_hex_colors1["AquaShine"] = "#00ABE5"
y_hex_colors2["AquaShine"] = "#00A3DA"

y_hex_colors1["Pink"] = "#FF4CA5"
y_hex_colors2["Pink"] = "#F3489D"
