#!/bin/bash
xmodmap .Xmodmap
xfce4-clipman &
/usr/bin/sudo tlp start
blueman-applet &
#picom --backend glx --vsync &
picom --backend glx --vsync --corner-radius 10 --inactive-opacity 0.8 &
/usr/lib/x86_64-linux-gnu/libexec/kdeconnectd &
xrandr --output DisplayPort-1 --same-as eDP --mode 1920x1080
nm-applet &
xset s 600
/bin/bash -c "sudo rfkill unblock bluetooth"
#/usr/lib/x86_64-linux-gnu/libexec/kdeconnectd
#echo schedutil | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
#ibus start &
#rofi -show run
