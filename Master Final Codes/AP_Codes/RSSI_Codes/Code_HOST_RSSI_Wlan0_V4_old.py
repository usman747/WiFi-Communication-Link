import os
import sys
import subprocess
import time
#time.sleep(5)
import argparse
import ConfigParser
import RPi.GPIO as GPIO


# 10


#Setting Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#
    
#GPIO Setup
GPIO.setup(10, GPIO.OUT)
      

global Ping_Status
Ping_Status = 5


class FakeGloabalSectionHead(object):
  def __init__(self,fp):
    self.fp = fp
    self.sechead = '[global]\n'
  def readline(self):
    if self.sechead:
      try: return self.sechead
      finally: self.sechead = None
    else: return self.fp.readline()

def Frequency_LED(Frequency):
      
      #Conditions to Observe
      if (Frequency == 'a'):
            GPIO.output(10,1)
            print(" 5 GHz LED Glowing. \n")
      else:
            GPIO.output(10,0)
            print(" 5 GHz LED Not Glowing. \n")







#Configuration to read RSSI from Command line (cmd)
          
parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
args = parser.parse_args()

#

#Configuration to read data from Hostapd.conf


#Reading Data from Hostapd.conf

config = ConfigParser.ConfigParser()
config.readfp(FakeGloabalSectionHead(open('/etc/hostapd/hostapd.conf')))

My_String = config.items('global')
print(My_String[3])

Frequency = My_String[3][1]
Frequency_LED(Frequency)

#Reading Data from Hostapd.conf


