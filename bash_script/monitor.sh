#!/bin/bash

echo "Choose an option:"
echo "1) Mirror display"
echo "2) Only external monitor"
echo "3) Only built-in monitor"

read -p "Enter your choice (1-3): " choice

case $choice in
  1)
    xrandr --output HDMI-A-0 --same-as eDP --mode 1920x1200 --output eDP --auto
    ;;
  2)
    xrandr --output HDMI-A-0 --mode 1920x1080 --output eDP --off
    ;;
  3)
    xrandr --output HDMI-A-0 --off --output eDP --auto
    ;;
  *)
esac

