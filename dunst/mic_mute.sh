#!/bin/bash

MUTED=$(pactl get-source-mute @DEFAULT_SOURCE@ | grep -oP 'yes|no')

pactl set-source-mute @DEFAULT_SOURCE@ toggle

if [ "$MUTED" = "yes" ]; then
  dunstify -r 1232 -I ~/.config/qtile/dunst/microphone-sensitivity-high.png -t 3000 ""
else
  dunstify -r 1232 -I ~/.config/qtile/dunst/microphone-sensitivity-muted.png -t 3000 ""
fi

.local/qtile/bin/qtile cmd-obj -o widget mic -f force_update

