#!/bin/bash

if [ "$(pactl get-sink-mute @DEFAULT_SINK@ | grep -oP 'yes|no')" = "yes" ]; then
    echo ""
else
    echo ""
fi

