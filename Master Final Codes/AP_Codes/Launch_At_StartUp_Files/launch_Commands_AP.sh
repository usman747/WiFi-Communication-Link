#!/bin/sh
#Launch_Commands_AP


#Restoring IP tables
#sudo iptables-restore < /etc/iptables/iptables.rules


#dhcpcd & dnsmasq start/stop
systemctl stop dhcpcd
systemctl stop dnsmasq
systemctl stop create_ap
systemctl start dnsmasq
systemctl start dhcpcd
systemctl start create_ap

