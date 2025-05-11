#!/bin/bash

if [ "$(pactl get-source-mute @DEFAULT_SOURCE@ | grep -oP 'yes|no')" = "yes" ]; then
  echo ""
else
  echo ""
fi
