import sys
import subprocess
import time
import os


File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","r")
Wlan_IP = File.readline()
ESSID = File.readline()
F_Band = File.readline()
File.close()
print(Wlan_IP)
print(len(Wlan_IP))

#os.system("sudo su")
#while True:
time.sleep(0.1)
conf = {}
with open('/etc/dhcpcd.conf') as fp:
    data = fp.readlines()

    if(data[64] == 'static ip_address=/24\n'):
        data[64] = 'static ip_address=192.168.4.16/24\n'
        data[65] = '#nohook wpa_supplicant\n'
        print('Static IP set to default.  Default Static IP = 192.168.4.16')
        os.system("sudo reboot")
            
        if(len(Wlan_IP) < 12):
            File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","w")
            File.write("192.168.4.16\n")
            File.write(ESSID)
            File.write(F_Band)
            print('Writing Default IP in file.')
            File.close()
                
        os.system("sudo reboot")
            
    else:
        print('Static IP is already set.')

    fp.close()
    
    
with open('/etc/dhcpcd.conf','w') as fp:
    fp.writelines(data)
    fp.close()
        
