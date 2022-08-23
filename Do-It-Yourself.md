
### Automated color updates
This Mint-Yz fork lets you change or add colors easier and faster than with the official Mint-Y scripts. But I have a Pull Request going on to copy these features to the official Mint-Y, so eventually, maybe, the official Mint-Y will be easier too.

With this Mint-Yz fork here, building Mint-Y-Colors is now 100% automated. As of March 2022, the following directories have to be edited by hand on the official Mint-Y:

  * gtk-3.0/thumbnails/  
  * cinnamon/thumbnails/  

So if you want to build your own themes, you will find it less difficult starting from here. But there are always unforeseen events, things to learn, things to fix. It is not so easy. Make sure you have the time and the will before you embark on this adventure. And be careful, always make backup copies. Be aware you must have some basic knowledge of the Linux system and terminal. There is no warranty, this is at your own risk.

### Required
If you want to build your own theme, you will need to install those packages:
 
  * Inkscape, preferably version 1.0 or higher (from PPA?)
  * optipng
  * imagemagick
  * sassc
  * git

### Compatibility issues
There are a few `render-assets.sh` scripts scattered around the `src/Mint-Y` directory and its sub-directories. They contain some `--export-filename` or `--export-png` Inkscape commands. Check that you have the required command for your version of Inkscape, or just replace as required:
 
  * Inkscape version 1.0 or higher: `--export-filename`  
  * Inkscape version 0.x: `--export-png`

### Steps-by-steps
If you want to create your own theme, here is what to do.

FIRST, install the required software and packages listed above.

SECOND, Git clone this repository, using your terminal:  
`git clone https://github.com/SebastJava/mint-yz-theme.git`.

THIRD, Edit the main colors 1, plus colors 2 in **Mint-Y-Colors/Mint-Y-Variations.svg** and then in **constants.py**

* **Mint-Y-Variations SVG and PNG files:** This is where all the colors are displayed. View them all there, grouped into one picture, one vision.
* **constants.py file:** All the #HEX values from Mint-Y-Variations.svg are there. This file will be used by the `./update-variations.py All` and `./generate-themes.py` scripts to re-create everything.

All those colors are displayed in **Mint-Y-Colors/Mint-Y-Variations.svg** and then they are all pasted one-by-one in **constants.py** using a color picker.

**Take a look at this** `constants.py` **file:**

* `colors1` is the base color.
* `colors2` ≅ 5% darker for the dark variants.

FOURTH, Do you want to do any other colour edit? Or design? Check this `mint-yz-theme/src/Mint-Y/gtk-3.0/sass/_colors.scss` And all the other files in this `mint-yz-theme/src/Mint-Y/gtk-3.0/sass/` directory! Everything is defined there, and then the `gtk.css` and `gtk-dark.css` are auto-generated when building the themes.

BUILD, METHOD A:

1. Open your Terminal and change directory: `cd ~/mint-yz-theme`.
1. On the first time, you must run `./update-variations.py All` from your terminal, in the mint-yz-theme directory. Later, you can replace `All` with one specific color name like `Blue` for quick specific updates.
1. Next, run `./generate-themes.py` from your terminal, in the mint-yz-theme directory.
1. And finally, copy all the files from ~/mint-yz-theme/usr/share/themes/ into /usr/share/themes/ as root: `sudo cp -rf usr/share/themes/Mint-Yz* /usr/share/themes` from your terminal, in the mint-yz-theme directory.
1. Change your theme in the system preferences.

THAT'S IT !

BUILD, METHOD B:

All the steps from "method A" are included in the `ALL.sh <color>` script...

1. Open your Terminal and change directory: `cd ~/mint-yz-theme`.
1. On the first time, you must run `./ALL.sh All` from your terminal, in the mint-yz-theme directory. Later, you can replace `All` with one specific color name like `Blue` for quick specific updates.

THAT'S IT !

### Publish (optional)
The files needed to create a Debian package are probably still there, but are not used anymore. We now make a simple ZIP file instead. It is super-easy, and makes it universally accessible.

First, edit the changelog file. Next:
```
cd ~/mint-yz-theme
rm -f mint-yz-theme*.zip
cp -r usr/share/themes .
# X.x.x = version number:
zip -q -r mint-yz-theme_X.x.x.zip COPYRIGHT INSTALLER.sh LICENSE
zip -q -r mint-yz-theme_X.x.x.zip README.md changelog themes
rm -r themes
```

And finally:

* `git status # one final check`
PUBLISH on GitHub releases page and on LM-forums:  
* upload some image or screenshot(s)
* copy-paste the latest changelog
* upload assets: mint-yz-theme_X.x.x.zip
* check
* publish
* test install from GitHub
* like release
* LM-forums: new post
* `git status # one final check`
* Grsync (optional)