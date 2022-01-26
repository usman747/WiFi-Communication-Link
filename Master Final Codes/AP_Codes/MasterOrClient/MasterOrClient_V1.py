import os
import sys
import time
import subprocess
#import argparse
#import ConfigParser
import RPi.GPIO as GPIO
from threading import Thread

time.sleep(3)


# 10


#Setting Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#
    
#GPIO Setup
GPIO.setup(10, GPIO.OUT)



def Client_Launch_Commands():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/launch_Commands_Client.sh")
def Client_Static_IP_Check():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/Static_IP_Check.sh")
def Client_wifi_to_eth_bridge():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/wifi-to-eth-bridge.sh")
def Client_Web_App_Launcher():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/Web_App_Launcher.sh")
def Client_Serial():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/Serial_launcher.sh")
def Connection_Re_establisher():
    os.system("sh /home/pi/Client_Codes/Launch_At_StartUp_Files/Connection_Check.sh")




def AP_Launch_Commands():
    os.system("sh /home/pi/AP_Codes/Launch_At_StartUp_Files/launch_Commands_AP.sh")
def AP_Web_App_Launcher():
    os.system("sh /home/pi/AP_Codes/Launch_At_StartUp_Files/Web_App_Launcher.sh")
def AP_Serial():
    os.system("sh /home/pi/AP_Codes/Launch_At_StartUp_Files/launcher.sh")
def AP_FBand():
    os.system("sh /home/pi/AP_Codes/Launch_At_StartUp_Files/F-Band.sh")


    

  

File=open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/MasterOrClient.txt","r")

MasterOrClient_Status=File.readline()

print(MasterOrClient_Status)
#print(type(MasterOrClient_Status))
File.close()



#Conditions to Observe
if (MasterOrClient_Status == "Master\n"):
    
    GPIO.output(10,1)
    
    print(" Master Code, Master LED Glowing. \n")

    os.system("sudo su")
    os.system("python /home/pi/Desktop/Read_File.py")

    time.sleep(0.1)

    os.system("python /home/pi/AP_Codes/Master_Ip_Settings/Master_IP_Settings.py")

    time.sleep(0.1)

    Thread(target = AP_Launch_Commands).start()

    time.sleep(0.2)

    Thread(target = AP_Web_App_Launcher).start()

    time.sleep(0.1)

    Thread(target = AP_Serial).start()

    time.sleep(0.1)

    Thread(target = AP_FBand).start()
    GPIO.output(10,0)

    
else:
    GPIO.output(10,1)
    
    print(" Client Code, Master LED Not Glowing. \n")
    
    os.system("sudo su")
    os.system("python /home/pi/Dhcpcd_Write_IP.py")
    
    time.sleep(0.1)

    #Thread(target = Client_Static_IP_Check).start()

    #time.sleep(0.1)

    os.system("python /home/pi/Client_Codes/Client_Ip_Settings/Client_IP_Settings.py")

    time.sleep(0.1)
    
    Thread(target = Client_Launch_Commands).start()
    
    print('Client_Launch Commands working')

    time.sleep(0.1)



    #Thread(target = Client_Launch_Commands).start()



    #Thread(target = Client_wifi_to_eth_bridge).start()

    #print('WiFi to eth bridge working  working')


    Thread(target = Client_Web_App_Launcher).start()
    #GPIO.output(10,0)
    #print('Web App Launched')
    time.sleep(0.1)

    Thread(target = Client_Serial).start()
    time.sleep(0.1)
    Thread(target = Connection_Re_establisher).start()

    GPIO.output(10,0)
    



