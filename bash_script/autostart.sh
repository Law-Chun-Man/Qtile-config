#!/bin/bash

xmodmap .Xmodmap
xfce4-clipman &
/usr/bin/sudo tlp start
picom --backend glx --vsync -b
nm-applet &
xset s 600
/usr/lib/x86_64-linux-gnu/libexec/kdeconnectd &
dunst &
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
pactl get-source-mute @DEFAULT_SOURCE@ | grep -q 'no' && pactl set-source-mute @DEFAULT_SOURCE@ toggle &

