#!/bin/sh
#Launcher.sh

sudo iw dev wlan0 set power_save off

cd /home/pi/

sudo python3 /home/pi/Client_Codes/Serial+RSSI_Codes/Serial+RSSI_Combined_LEDs_Client_V2.py

#sudo python3 /home/pi/Serial+RSSI_Combined_Client_UDP_Socket_V3.py

#sudo python3 /home/pi/Serial+RSSI_Combined_Client_V4.py

#sudo python3 /home/pi/Serial+RSSI_Combined_Client_V2.py
#sudo python /home/pi/SerialTest_Working_V6.py
