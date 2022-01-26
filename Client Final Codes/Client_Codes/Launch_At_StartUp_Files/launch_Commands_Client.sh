#!/bin/sh
#Launch_Commands_Clients

sudo su

#dhcpcd & dnsmasq start/stop
systemctl stop dnsmasq
systemctl stop create_ap
systemctl stop dhcpcd
systemctl start dhcpcd


