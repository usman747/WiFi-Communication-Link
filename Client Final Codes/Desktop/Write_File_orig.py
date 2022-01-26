import sys
import subprocess
import time
import argparse
#import ConfigParser
import os

wlan_IP=[]
conf = {}
i=0
with open('/etc/dhcpcd.conf') as fp:
    for line in fp:
        if line.startswith('#'):
            continue
        if(i==0):        
            if 'static ip_address' in line:
                #print(line.lstrip(''))
                #eth_Static_IP = line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32]
                #eth_Static_IP = ''.join(eth_Static_IP)
                #print(eth_Static_IP)
                i=1
        elif(i==1):
            if 'static ip_address' in line:
                #print(line.lstrip(''))
                #
                j=18;
                while(True):
                    if(line[j] != '/'):
                        wlan_IP.append(line[j])
                    else:
                        break
                    j=j+1
                wlan_IP=''.join(wlan_IP)      
                #print(wlan_IP)
                #
                #wlan_Static_IP = line[18],line[19],line[20],line[21],line[22],line[23],line[24],line[25],line[26],line[27],line[28],line[29],line[30],line[31],line[32]
                #print(wlan_Static_IP)
                #wlan_Static_IP = ''.join(wlan_Static_IP)
                #print(wlan_Static_IP)
                #time.sleep(20)
                i=0

with open('/etc/create_ap.conf') as fp:
    for line in fp:
        if line.startswith('#'):
            continue
        if 'FREQ_BAND' in line:
            #print(line.lstrip(''))
            Frequency_Band = line[10]
            Frequency_Band = ''.join(Frequency_Band)
            print(Frequency_Band)

Wifi_Conf_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","w+")
Wifi_Conf_File.write(wlan_IP)
Wifi_Conf_File.write('\n')
if(Frequency_Band == '2'):
    Wifi_Conf_File.write("2.4\n")
elif(Frequency_Band == '5'):
    Wifi_Conf_File.write("5\n")
    
Wifi_Conf_File.close()
