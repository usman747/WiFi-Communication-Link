import os
import sys
import time

time.sleep(3)

Read_WiFi_File = open("/home/pi/Client/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
IP=Read_WiFi_File.readline()
Read_WiFi_File.close()
IP=IP.rstrip("\n")

#print(IP)
exit(IP)
