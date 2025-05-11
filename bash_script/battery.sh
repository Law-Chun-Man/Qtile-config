#!/bin/bash

status=$(cat "/sys/class/power_supply/BAT0/status" 2>/dev/null)

case "$status" in
    "Charging")     symbol="" ;;
    "Discharging")  symbol="" ;;
    "Full")         symbol="" ;;
    "Not charging") symbol="" ;;
    *)              symbol="?" ;;
esac

echo $symbol
