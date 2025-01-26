#!/bin/bash

CURRENT_GOVERNOR=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)

# Determine the new governor
if [ "$CURRENT_GOVERNOR" = "schedutil" ]; then
    NEW_GOVERNOR="performance"
else
    NEW_GOVERNOR="schedutil"
fi

echo $NEW_GOVERNOR | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

echo "Press any key to leave..."
read -n 1
