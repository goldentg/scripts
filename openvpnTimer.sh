#!/bin/bash

SERVICE=openvpn-server@server.service
TIMEOUT=600
IP=8.8.8.8

if systemctl is-active --quiet $SERVICE; then
    echo "$SERVICE is running"
else
    echo "$SERVICE is not running"
    sleep $TIMEOUT
    if ! systemctl is-active --quiet $SERVICE; then
        if ping -c 1 $IP &> /dev/null; then
            echo "Restarting server"
            shutdown -r now
        else
            echo "$IP is not reachable"
        fi
    fi
fi
