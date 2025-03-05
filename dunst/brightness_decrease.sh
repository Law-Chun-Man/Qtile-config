#!/bin/bash

brightnessctl set 1%-

BRIGHTNESS=$(brightnessctl get)

dunstify -r 1235 -h int:value:"$BRIGHTNESS" -I ~/.config/qtile/dunst/display-brightness.png -t 3000 "$BRIGHTNESS%"

