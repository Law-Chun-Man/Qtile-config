#!/bin/bash

pactl set-sink-volume @DEFAULT_SINK@ -5%

MUTED=$(pactl get-sink-mute @DEFAULT_SINK@ | grep -oP 'yes|no')
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\d+%' | head -n 1)

if [ "$MUTED" = "yes" ]; then
  dunstify -r 1234 -h int:value:"$VOLUME" -I ~/.config/qtile/dunst/audio-volume-muted.png -t 3000 "Muted"
else
  dunstify -r 1234 -h int:value:"$VOLUME" -I ~/.config/qtile/dunst/audio-volume-high.png -t 3000 "$VOLUME"
fi

