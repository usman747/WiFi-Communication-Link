import os
import sys
import subprocess
import time
import RPi.GPIO as GPIO


#Setting Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#
    
#GPIO Setup
GPIO.setup(10, GPIO.OUT)
      
time.sleep(10)

with open('/etc/create_ap.conf') as fp:
    for line in fp:
        if 'FREQ_BAND' in line:
            #print(line.lstrip(''))
            Frequency_Band = line[10]
            Frequency_Band = ''.join(Frequency_Band)
            print(Frequency_Band)

#while(1):
    
    
#Conditions to Observe
if (Frequency_Band == '5'):
    GPIO.output(10,1)
    print(" 5 GHz LED Glowing. \n")
else:
    GPIO.output(10,0)
    print(" 5 GHz LED Not Glowing. \n")



