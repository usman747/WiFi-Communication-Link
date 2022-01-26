#!/bin/sh
sudo ip route add 192.168.1.1/32 via 192.168.4.1 dev wlan0
sudo ip route add 192.168.1.2/32 via 192.168.4.1 dev wlan0