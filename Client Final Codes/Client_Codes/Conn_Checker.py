import os 
import sys
import subprocess
import time
import string
import argparse
from threading import Thread

def Client_Launch_Commands():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/launch_Commands_Client.sh")
def Client_wifi_to_eth_bridge():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/wifi-to-eth-bridge.sh")
def Client_Web_App_Launcher():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/Web_App_Launcher.sh")
def Client_Route_Adder():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/Route_Adder.sh")

#********************************* Pinging the Master *********************************#


parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
args = parser.parse_args()

i=0

while(i!=1):
    cmd1 = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)

    for line in cmd1.stdout:
                            if str.encode('ESSID:"109_Dett_Robot"') in line:
                                i=i+1
                                #print('connected with Master')
                                
                            else:
                                i=i
                                #print ('Wating for connection')
                                


#********************************* Killing web app server PID of app that was created on eth *********************************#                    

##while(it!=1):
##    cmd2 = subprocess.Popen('sudo netstat -ntlp %s' % args.interface, shell=True,stdout=subprocess.PIPE)
##
##    for line in cmd2.stdout:
##        if str.encode(':8000') in line:
##            a=line[78:]
##            b= a[:6]
##            b=str(b)
##            b=b.strip("  b'")
##            print(b)
##            c=int(b)
##            os.system("sudo kill -9 %d" % c)
##            print("killed")
##            it=it+1
##        else:
##            #it=it+1
##            print("eth web not seen, wasn't made in main code probably")
##    break
##
##print("cleared from eth web killer")



#********************************* Removing/Commenting eth0 configuration from dhcpcd *********************************#

File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","r")
Wlan_IP = File.readline()
File.close()
#print('IP Read')
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
        data[66] = '\n'
        data[67] = '\n'
        data[68] = '\n'
        #print('Assigning dhcpcd1')
        #print('Default IP = I92.168.4.16')
    else:
        data[64] = 'static ip_address=' + Wlan_IP.rstrip("\n") + '/24\n'
        data[65] = '#nohook wpa_supplicant\n'
        data[66] = '\n'
        data[67] = '\n'
        data[68] = '\n'
        #print('Assigning dhcpcd2')
        #print(Wlan_IP)

    fp.close()
    
    
with open('/etc/dhcpcd.conf','w') as fp:
    fp.writelines(data)
    fp.close()

#********************************* Restarting the dhcpcd service *********************************#
    #os.system("sudo su")
    time.sleep(0.3)
    Thread(target = Client_Launch_Commands).start()
    print('Dhcpcd stoped & started again')
        

#********************************* Turning ON wifi-to-eth-bridge *********************************#

    #time.sleep(35)
    #os.system("sudo su")
    time.sleep(0.3)
    Thread(target = Client_wifi_to_eth_bridge).start()
    time.sleep(0.3)
    print('Wifi to Eth Bridge started')

        
#********************************* Adding Routing Table to connect with Master's eth & Laptop *********************************#
    
    ##subprocess.Popen('sudo ip route add 192.168.1.1 via 192.168.4.1 dev wlan0', shell=True,stdout=subprocess.PIPE)
    ##subprocess.Popen('sudo ip route add 192.168.1.2 via 192.168.4.1 dev wlan0', shell=True,stdout=subprocess.PIPE)
    #os.system("sudo ip route add 192.168.1.2 via 192.168.4.1 dev wlan0")
    #Thread(target = Client_Add_Route).start()
    #os.system("python /home/pi/Desktop/New.py")
    #print('Routing tables added')

#********************************* Turning ON Web App *********************************#
    time.sleep(10)
    ## Do not remove this delay, because bridge takes time to get ON. And if web app launched without delay then it causes problems
    Thread(target = Client_Web_App_Launcher).start()
    print('\n Web App started')

#********************************* Writing Master eth and PC IP in routing tables *********************************#

##    time.sleep(0.1)
##    Thread(target = Client_Route_Adder).start()
##    print('ROutes adder')
