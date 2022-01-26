#!/bin/sh
#Web_App_Launcher.sh

python2 /home/pi/Form/WiFi_Conf_V1.py
IP=$(python /home/pi/Client/Django2.0-Contact-Form-master/django_contact_form/Client_IP_for_settings.py 2>&1)
sudo su
cd /home/pi/Client/Django2.0-Contact-Form-master/
sudo python3 manage.py runserver $IP:8000

