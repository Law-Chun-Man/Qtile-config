#!/bin/bash

temp_milli=$(cat "/sys/class/thermal/thermal_zone0/temp")

temp_celsius=$((temp_milli / 1000))

echo "${temp_celsius:0:2}°C"

