#!/bin/bash

MUTED=$(pactl get-sink-mute @DEFAULT_SINK@ | grep -oP 'yes|no')
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -oP '\d+%' | head -n 1)

pactl set-sink-mute @DEFAULT_SINK@ toggle

if [ "$MUTED" = "yes" ]; then
  dunstify -r 1234 -h int:value:"$VOLUME" -I ~/.config/qtile/dunst/audio-volume-high.png -t 3000 "$VOLUME"
else
  dunstify -r 1234 -h int:value:"$VOLUME" -I ~/.config/qtile/dunst/audio-volume-muted.png -t 3000 "Muted"
fi

