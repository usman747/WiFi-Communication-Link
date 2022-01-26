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
    Wifi_Channel = fp.readline()
    Wifi_Channel = Wifi_Channel.rstrip()
    fp.close()

Wifi_Channel = Wifi_Channel[8:]
print(Wifi_Channel)


with open('/etc/create_ap.conf') as fp:
    for line in fp:
        if line.startswith('#'):
            continue
##        if 'CHANNEL' in line:
##            Wifi_Channel = line[8], line[9], line[10], line[11], line[12], line[13], line[14]
##            Wifi_Channel = ''.join(Wifi_Channel)
##            print(Wifi_Channel)

        if 'WPA_VERSION' in line:
            Encryption_Key = line[12]
            Encryption_Key = ''.join(Encryption_Key)
            print(Encryption_Key)

        if 'ISOLATE_CLIENTS' in line:
            Isolate_Client = line[16]
            Isolate_Client = ''.join(Isolate_Client)
            print(Isolate_Client)

        if 'IEEE80211N' in line:
            Wifi_Mode = line[11]
            Wifi_Mode = ''.join(Wifi_Mode)
            print(Wifi_Mode)

        if 'IEEE80211AC' in line:
            Wifi_Mode2 = line[12]
            Wifi_Mode2 = ''.join(Wifi_Mode2)
            print(Wifi_Mode2)
     
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

Wifi_Conf_File2 = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf2.txt","w+")
if(Encryption_Key == '2'):
    Wifi_Conf_File2.write("wpa2\n")
elif(Encryption_Key == '1'):
    Wifi_Conf_File2.write("wpa\n")
if(Wifi_Mode == '1' and Wifi_Mode2 == '0'):
    Wifi_Conf_File2.write("802.11n\n")
elif(Wifi_Mode == '0' and Wifi_Mode2 == '1'):
    Wifi_Conf_File2.write("802.11ac\n")
if(Isolate_Client == '0'):
    Wifi_Conf_File2.write("No\n")
elif(Isolate_Client == '1'):
    Wifi_Conf_File2.write("Yes\n")
Wifi_Conf_File2.write(Wifi_Channel + "\n")

Wifi_Conf_File2.close()


