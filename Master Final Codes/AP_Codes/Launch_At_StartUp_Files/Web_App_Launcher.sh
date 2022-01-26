#!/bin/sh
#App_Launcher.sh


IP=$(python /home/pi/Desktop/Wlan_Static_IP.py 2>&1)
sudo su
cd /home/pi/AP-WebApp/Django2.0-Contact-Form-master/
sudo python3 manage.py runserver $IP:8000