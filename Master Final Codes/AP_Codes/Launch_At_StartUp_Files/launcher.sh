#!/bin/sh
#Launcher.sh

sudo iw dev wlan0 set power_save off

cd /home/pi/

sudo python3 /home/pi/AP_Codes/Serial+RSSI_Codes/Serial+RSSI_Combined_V8.py

#sudo python3 /home/pi/Serial+RSSI_Combined_UDP_Socket_V5.py


#sudo python3 /home/pi/Serial+RSSI_Combined_V6.py

#sudo python3 /home/pi/Serial+RSSI_Combined_V4.py

#sudo python3 /home/pi/Serial_with_Constant_Ping_V1.py

#sudo python /home/pi/SerialTest_WorkingV3_HOST.py
#sudo python /home/pi/SerialTest_WorkingV7_HOST.py


