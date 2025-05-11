#!/bin/bash

CURRENT_BRIGHTNESS=$(cat /sys/class/backlight/amdgpu_bl0/brightness)
BRIGHTNESS=$((CURRENT_BRIGHTNESS + 3))

echo "$BRIGHTNESS" | sudo tee /sys/class/backlight/amdgpu_bl0/brightness >/dev/null

dunstify -r 1235 -h int:value:"$BRIGHTNESS" -I ~/.config/qtile/dunst/display-brightness.png -t 3000 "$BRIGHTNESS%"

