import sys
import subprocess
import time
import os


File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","r")
Wlan_IP = File.readline()
File.close()
#print(Wlan_IP)
#print(len(Wlan_IP))


conf = {}
with open('/etc/dhcpcd.conf') as fp:
    data = fp.readlines()
    data[57] = '#interface eth0\n'
    data[58] = '#static ip_address=192.168.1.1/24\n'
    if(len(Wlan_IP) == 1):
        data[64] = 'static ip_address=192.168.4.16/24\n'
        data[65] = '#nohook wpa_supplicant\n'
        data[66] = 'interface eth0\n'
        data[67] = 'static ip_address=192.168.4.16/24\n'
        data[68] = '##\n'
        #print('Default IP = I92.168.4.16')
    else:
        data[64] = 'static ip_address=' + Wlan_IP.rstrip("\n") + '/24\n'
        data[65] = '#nohook wpa_supplicant\n'
        data[66] = 'interface eth0\n'
        data[67] = 'static ip_address=' + Wlan_IP.rstrip("\n") + '/24\n'
        data[68] = '##\n'
        #print(Wlan_IP)

    fp.close()
    
    
with open('/etc/dhcpcd.conf','w') as fp:
    fp.writelines(data)
    fp.close()
