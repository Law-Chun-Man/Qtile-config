#!/bin/bash

# Other settings
xfce4-clipman &
dunst &
/usr/bin/sudo tlp start
picom --backend glx --vsync -b
xset s 600 &
xset b off &
pactl get-source-mute @DEFAULT_SOURCE@ | grep -q 'no' && pactl set-source-mute @DEFAULT_SOURCE@ toggle &
xsetroot -cursor_name left_ptr

# XFCE
nm-applet &
/usr/libexec/at-spi-bus-launcher --launch-immediately &
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/x86_64-linux-gnu/libexec/kdeconnectd &
xfce4-power-manager &
light-locker &
xiccd &

