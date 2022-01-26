import os
import sys
import time

time.sleep(0.1)

#os.system("python /home/pi/Form/WiFi_Conf_V1.py")
Read_WiFi_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","r")
IP = Read_WiFi_File.readline()
Read_WiFi_File.close()

#print(len(IP))

if(len(IP) == 1):
    IP = "192.168.4.16"
else:
    IP=IP.rstrip("\n")

#print(IP)
exit(IP)
