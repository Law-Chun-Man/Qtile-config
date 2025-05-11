#!/bin/bash

if [ "$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)" = "schedutil" ]; then
    echo ""
else
    echo ""
fi

