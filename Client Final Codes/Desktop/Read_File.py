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

File2=open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf2.txt","r")
Encryption_Key=File2.readline()
Wifi_Mode=File2.readline()
Isolate_Client=File2.readline()
Wifi_Channel=File2.readline()
File2.close()

Encryption_Key=Encryption_Key.rstrip()
Wifi_Mode=Wifi_Mode.rstrip()
Isolate_Client=Isolate_Client.rstrip()
Wifi_Channel=Wifi_Channel.rstrip()

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
    elif(Frequency_Band.strip() == '5'):
        data[19] = 'FREQ_BAND=5\n'
    if(Encryption_Key == 'wpa2'):
        data[2] = 'WPA_VERSION=2\n'
    elif(Encryption_Key == 'wpa'):
        data[2] = 'WPA_VERSION=1\n'
    if(Wifi_Mode == '802.11n'):
        data[12] = 'IEEE80211N=1\n'
        data[13] = 'IEEE80211AC=0\n'
    elif(Wifi_Mode == '802.11ac'):
        data[12] = 'IEEE80211N=0\n'
        data[13] = 'IEEE80211AC=1\n'
    if(Isolate_Client == 'No'):
        data[10] = 'ISOLATE_CLIENTS=0\n'
    elif(Isolate_Client == 'Yes'):
        data[10] = 'ISOLATE_CLIENTS=1\n'

    data[0] = 'CHANNEL=' + Wifi_Channel + '\n'
    fp1.close()
    
with open('/etc/create_ap.conf','w') as fp1:
    fp1.writelines(data)
    fp1.close()


