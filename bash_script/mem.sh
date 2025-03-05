#!/bin/bash

mem_total=$(grep -w MemTotal /proc/meminfo | awk '{print $2}')
mem_available=$(grep -w MemAvailable /proc/meminfo | awk '{print $2}')

used=$((mem_total - mem_available))

percent=$(echo "scale=1; $used*100/$mem_total"|bc)

if (( $(bc <<< "$percent < 10") )); then
    printf "%.2f%%" "$percent"
else
    printf "%.1f%%" "$percent"
fi

