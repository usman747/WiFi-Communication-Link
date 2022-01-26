import sys
import subprocess
import time
import argparse
import ConfigParser
import os
import RPi.GPIO as GPIO

#Setting Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#
    
#GPIO Setup
GPIO.setup(17, GPIO.OUT)



class FakeGlobalSelectionHead(object):
    def __init__(self,fp):
        self.fp = fp
        self.sechead = '[global]\n'
    def readline(self):
        if self.sechead:
            try: return self.sechead
            finally: self.sechead = None
        else: return self.fp.readline()


config = ConfigParser.ConfigParser(allow_no_value=True)
config.readfp(FakeGlobalSelectionHead(open('/etc/dhcpcd.conf')))

Static_IP = config.items('global')
#print(Static_IP[11][1])




def main():
  parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
  parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
  args = parser.parse_args()


  try:
    i=0
    cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)
        
    Wifi_Conf_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","w+")
    IP=Static_IP[11][1]
    wlan=[]
    while(True):
        if(IP[i]!='/'):
            wlan.append(IP[i])
        else:
            break
        i=i+1
    wlan=''.join(wlan)
    i=0    
    Wifi_Conf_File.write(wlan)
    Wifi_Conf_File.write("\n")
    print(wlan)
    #Connected = 0
    #while(Connected == 0): 

        #cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)
        #GPIO.output(17,1)
        #time.sleep(1)
    for line in cmd.stdout:
        if str.encode('ESSID:"') in line:
            ESSID = line.lstrip(' ')
            #ESSID = line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37],line[38],line[39],line[40],line[41],line[42]
            #ESSID=''.join(ESSID)
            Wifi_Conf_File.write(ESSID)
            print(ESSID)
            #Connected = 1


        if str.encode('Frequency') in line:
            Frequency=line[34],line[35],line[36],line[37]
            Frequency=''.join(Frequency)
            #Frequency=float(Frequency)
            Wifi_Conf_File.write(Frequency)
            print(Frequency)
            #Connected = 1

        elif str.encode('Not-Associated') in line:
            ESSID = 'No Signal'
            Frequency = 0.0
            #Connected = 0
            #print(ESSID)
            #print(Frequency)

        #GPIO.output(17,0)
                
    #GPIO.output(17,0)

#GPIO.output(17,0)
    Wifi_Conf_File.close()
  except KeyboardInterrupt:
    print('Exiting Program \n\n')
    time.sleep(5)



main()



