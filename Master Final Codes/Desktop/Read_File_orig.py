import sys
import subprocess
import time
import argparse
#import ConfigParser
import os


File=open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
#File=open("/home/pi/asd.txt")
Wlan_IP=File.readline()
Frequency_Band=File.readline()
#print(Wlan_IP)
#print(type(Frequency_Band))
#print(Frequency_Band)
File.close()

conf = {}

with open('/etc/dhcpcd.conf') as fp1:
    data = fp1.readlines()
    #print data[64]
    data[57] = 'interface eth0\n'
    data[58] = 'static ip_address=192.168.1.1/24\n'
    data[64] = 'static ip_address=' + Wlan_IP.rstrip("\n") + '/24\n'
    data[65] = 'nohook wpa_supplicant\n'
    data[66] = '\n'
    data[67] = '\n'
    data[68] = '\n'
    fp1.close()
    
with open('/etc/dhcpcd.conf','w') as fp1:
    fp1.writelines(data)
    fp1.close()




with open('/etc/create_ap.conf') as fp1:
    data = fp1.readlines()
    if(Frequency_Band.strip() == '2.4'):
        data[19] = 'FREQ_BAND=2.4\n'
        #data[0] = 'CHANNEL=default\n'
    elif(Frequency_Band.strip() == '5'):
        data[19] = 'FREQ_BAND=5\n'
        #data[0] = 'CHANNEL=default\n'
    fp1.close()
    
with open('/etc/create_ap.conf','w') as fp1:
    fp1.writelines(data)
    fp1.close()


