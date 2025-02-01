#!/bin/bash
xmodmap .Xmodmap
xfce4-clipman &
/usr/bin/sudo tlp start
blueman-applet &
picom --backend glx --vsync --corner-radius 10 --inactive-opacity 0.8 &
/usr/lib/x86_64-linux-gnu/libexec/kdeconnectd &
nm-applet &
xset s 600
