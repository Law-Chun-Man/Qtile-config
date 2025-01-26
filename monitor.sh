#!/bin/bash

echo "Choose an option:"
echo "1) Mirror display"
echo "2) Only external monitor"
echo "3) Only built-in monitor"

read -p "Enter your choice (1-3): " choice

case $choice in
  1)
    xrandr --output DisplayPort-1 --same-as eDP --mode 1920x1080
    ;;
  2)
    xrandr --output DisplayPort-1 --mode 1920x1080 --output eDP --off
    ;;
  3)
    xrandr --output DisplayPort-1 --off --output eDP --auto
    ;;
  *)
esac

echo "Press any key to leave..."
read -n 1
