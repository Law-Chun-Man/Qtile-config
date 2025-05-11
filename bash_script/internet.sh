#!/bin/bash

if [ "$(cat /sys/class/net/w*/operstate 2>/dev/null)" = 'up' ] ; then
	wifi=""
elif [ "$(cat /sys/class/net/w*/operstate 2>/dev/null)" = 'down' ] ; then
	[ "$(cat /sys/class/net/w*/flags 2>/dev/null)" = '0x1003' ] && wifi="" || wifi=""
fi

[ -n "$(cat /sys/class/net/tun*/operstate 2>/dev/null)" ] && wifi=""

[ "$(cat /sys/class/net/e*/operstate 2>/dev/null)" = 'up' ] && wifi=""

echo $wifi

