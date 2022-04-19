**Mint-Yz GTK themes:**

# Colors, Contrasts, and Design

**This is an abbreviated version from my original README, intended for the LinuxMint Design Team. Sorry to bother you again, but I don't know if my Slack posts were seen or not. This is sort of a list of issues. I can't break this down into a few small issues because there are too many.**  

**What's new:**  
* The colours have evolved considerably since the beginnings, with many considerations on mind.
* There are also many other improvements made to contrasts and design.
* There is a lot of work into this new Mint-Yz. Over 200 commits. Build onto the latest stable Mint-Y, version 1.9.8.

## Colors
Contemporary colours. Subdued, flat or shining. Sufficiently contrasted.  
(see images here below ▼)  

**Color contrasts with the foreground white text**  
Method: https://marijohannessen.github.io/color-contrast-checker/

| Mint-Y colour contrast ratios  | Mint-Yz colour contrast ratios |
| ------------------------------ | ------------------------------ |
| 2.4 Mint                       | 2.4 MintClassic = Mint         |
| 4.5 Blue                       | 4.3 BlueBelize                 |
| 2.7 Grey                       | 4.5 Grey                       |
| 2.7 Teal                       | 3.0 MintGum                    |
| 0.0 (nothing)                  | 3.9 BlueElectron               |
| 4.0 Purple                     | 6.3 Purple                     |
| 4.3 Red                        | 4.3 RedShine                   |
| 2.3 Orange                     | 2.6 OrangeShine                |
| 2.5 Aqua                       | 3.0 AquaShine                  |
| 3.8 Pink                       | 3.1 Pink                       |
| 3.3 Brown                      | 0.0 (nothing)                  |
| 2.2 Sand                       | 0.0 (nothing)                  |
| 6 out of 11 colors lacks sufficient contrast | 1 out of 9 colors lacks sufficient contrast (1) |

(1) *Not counting MintClassic because this one is mostly there for technical purposes.*

**Other color related considerations**  

And then there are also "gloss" issues that were taken into account. But don't overdo it here either: there is a difference between the background color for a full page versus the background color of a focused element. And, of course, beyond these technical considerations, the color must transmit some good vibrations...

To sum up, here i tried to create a mix of some subdued, flat, or shining colours. Something for each one of us. But please, don't ask me for a subdued orange or red... I could make it, of course, but then i don't call it "orange" or "red" anymore !

## Contrasts

| Variant | Category                        | Mint-Y                | Mint-Yz               |
| ------- | ------------------------------- | --------------------- | --------------------- |
| all     | buttons and entries backgrounds | no contrast           | subtle contrast       |
| base    | hovering on buttons             | lighten (too subtle!) | darken 5% (better)    |
| dark    | base color vs background color  | almost no difference  | 2X difference         | 
| dark    | check and radio buttons         | almost invisible when empty | subtle outline  |
| dark    | check and radio buttons         | dark foreground | white foreground (\#F0F0F0) |
| dark    | window title, unfocused/focused | not much difference   | much more difference  |
| all     | terminal background color       | Dark grey (\#3F3F3F)  | 6% darker (\#303030)  |

(see images here below ▼)  

## Design

* Square window corners everywhere. I like round corners, but not when the top ones are round while the bottom ones are square. Additionally, on the official Mint-Y, the design keeps changing all the time. You get round top corners when the window is in the middle of the screen, and they turn square when you push tile. I don't like that. More over, there is a small rendering bug with Metacity round corners. All these problems are simply avoided by making all window corners square. Everywhere.
* No backgrounds on window close buttons. Round red background on hovering. That's nicer, and more logical. Before, with the default Mint-Y color, the close button was... green !? And we are also avoiding an old bug in the theme chooser !
* Accent color on active button background. That's a revert, setting it as it is on the old Mint-Y-Legacy. Things are more consistent that way, in my opinion. Small buttons such as radio and checkbox are coloured, and the same rule applies for bigger buttons, here on Mint-Yz.
* Subtle rounded corners on buttons and entries (3px -> 5px).
* Solid and coloured outlines on focused buttons and entries: more visible and nicer.
* No dashed outlines on other elements. This was unneeded and ugly. (Same as Mint-X here.)
* Message colors are better. That's for things like that green save button in the Xed text editor, or this red Logout button.
* And there are some small bug fixes. Et cetera.

---

**More information and download:**  
https://github.com/SebastJava/mint-yz-theme#readme  

**References:**  
https://colorable.jxnblk.com  
https://marijohannessen.github.io/color-contrast-checker/  
https://uxmovement.com/content/why-you-should-avoid-bright-saturated-background-colors/  
https://uxmovement.com/content/why-you-should-never-use-pure-black-for-text-or-backgrounds/  
https://flatuicolors.com/  

---

![Mint-Y-Colors/contrasts-dark.png](https://raw.githubusercontent.com/SebastJava/mint-yz-theme/master/Mint-Y-Colors/contrasts-dark.png)  
▲ Many subtle contrasts and design improvements there.  

![Mint-Y-Colors/Mint-Y-Variations-compare-OLD.png](https://raw.githubusercontent.com/SebastJava/mint-yz-theme/master/Mint-Y-Colors/Mint-Y-Variations-compare-OLD.png)  
▲ An image is worth a thousand words...  

![Mint-Y-Colors/Mint-Y-Variations.png](https://raw.githubusercontent.com/SebastJava/mint-yz-theme/master/Mint-Y-Colors/Mint-Y-Variations.png)  
▲ There is no simple and standard way to make the dark variants.  

![Mint-Y-Colors/mix/mix.png](https://raw.githubusercontent.com/SebastJava/mint-yz-theme/master/Mint-Y-Colors/mix/mix.png)  
▲ Mix themes and icons colours !  

---

P.S.: Your [Mint-Y-Colors](https://github.com/linuxmint/mint-themes/tree/master/Mint-Y-Colors) directory is outdated. Please delete it.