# Mint-Yz-theme branches: a short description

Please be aware that new branches are being created and old branches are being deleted as this repository evolves. So, this description here is quite possibly not up-to-date.

Branch name | Description
-------| -----------
**master** | (DEFAULT BRANCH) That is the big one. Where all the improvements from other branches are merged or will be merged.
**source** | (UPSTREAM) This one remains untouched. It is a copy of the upstream master source.
OLD-auto | Added and modified scripts for a complete automation. The `newcolors` branch was started from there. And then the `newflat` branch was started on top of all that.
OLD-buttonscolor | This is a reverting branch. Some kind of "undo". The new and official Mint-Y keeps the colors on the tiny little assets, but removes the colors on the buttons. This branch brings back the color on the active or "toggled" buttons. — This branch is old. It got duplicated outside of git and transformed into a commit which is now part of the new `buttons-all` branch. So, there isn't any common references in git and thus this old branch here could be safely deleted without affecting other branches.
OLD-corners | This branch makes the corners on buttons and entries a bit more rounded. Before, on the original Mint-Y, it was just too subtle. (border-radius: 3px -> 5px) — This branch is old. It got duplicated outside of git and transformed into a commit which is now part of the new `buttons-all` branch. So, there isn't any common references in git and thus this old branch here could be safely deleted without affecting other branches.
OLD-master | This is just an old backup branch. It could be deleted.
OLD-newflat | This one is not new anymore. That's an old master branch. It could be deleted.
OLD-outlines | The outlines are there to show what is the focused element. The outlines are made solid and coloured on buttons, so it is now more visible. And on the opposite, there are now no outlines on other elements, as I found this superfluous and distractive. Take a look at Mint-X for example: there aren't any outlines in there. — This branch is old. It got duplicated outside of git and transformed into a commit which is now part of the new `buttons-all` branch. So, there isn't any common references in git and thus this old branch here could be safely deleted without affecting other branches.
**PR-newmain** | Part of a GROUP of pull requests for the official Mint-Y. For a complete automation. This newmain has merged all the other parts of this group for demonstration purposes. Complete description: https://github.com/SebastJava/mint-yz-theme/tree/newmain#readme
PR-cinthumb | Part of a GROUP of pull requests for the official Mint-Y. For a complete automation. One chunk at a time. Complete description: https://github.com/SebastJava/mint-yz-theme/tree/newmain#readme
PR-menubar-toolbar | Part of a GROUP of pull requests for the official Mint-Y. For a complete automation. One chunk at a time. Complete description: https://github.com/SebastJava/mint-yz-theme/tree/newmain#readme
PR-thumbnails | Part of a GROUP of pull requests for the official Mint-Y. For a complete automation. One chunk at a time. Complete description: https://github.com/SebastJava/mint-yz-theme/tree/newmain#readme
PR-variations | Part of a GROUP of pull requests for the official Mint-Y. For a complete automation. One chunk at a time. Complete description: https://github.com/SebastJava/mint-yz-theme/tree/newmain#readme
PR-xfwm4 | Part of a GROUP of pull requests for the official Mint-Y. For a complete automation. One chunk at a time. Complete description: https://github.com/SebastJava/mint-yz-theme/tree/newmain#readme
buttons-all | This branch is a group of small edits, all in `src/Mint-Y/gtk-3.0/sass` directory. **First**, there is some kind of "undo" on active buttons color. The new and official Mint-Y keeps the colors on the tiny little assets, but removes the colors on the buttons. This branch brings back the color on the active (or "toggled") buttons. **Second**, the corners on buttons and entries get a bit more rounded. Before, on Mint-Y, it was just too subtle. **Third**, the outlines got re-edited. The outlines are there to show what is the focused element. The outlines are now made solid and coloured on buttons, so it is now more visible. And, on the opposite, there are now no outlines on other elements, as I found this superfluous and distractive. Take a look at Mint-X for example: there aren't any outlines in there. 
newcolors | This is where the new colors are being selected and displayed.
smallsvg | `src/Mint-Y/metacity-1/*.svg` re-edited to make these files much smaller and faster, but without changing the image appearance. (11 SVGs)