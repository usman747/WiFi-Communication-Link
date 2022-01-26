import sys
import subprocess
import time
import argparse
import os
import RPi.GPIO as GPIO


#17,27,22,  10

#Setting Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#
    
#GPIO Setup
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
#GPIO Setup
GPIO.setup(10, GPIO.OUT)
#
#

def Frequency_LED(Frequency):
      
      
      
    
      #Conditions to Observe
      if (Frequency >= 5.0):
            GPIO.output(10,1)
            print(" 5 GHz LED Glowing. \n")
      else:
            GPIO.output(10,0)
            print(" 5 GHz LED Not Glowing. \n")




def Signal_LEDs(S_Level):
      
      #Setting Mode
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      #
    
      #GPIO Setup
      GPIO.setup(17, GPIO.OUT)
      GPIO.setup(27, GPIO.OUT)
      GPIO.setup(22, GPIO.OUT)
      #
    
      #Conditions to Observe
      if (S_Level > -53.0):                # > 75 %
            GPIO.output(17,1)
            GPIO.output(27,1)
            GPIO.output(22,1)
            print(" All LEDs Glowing. \n")
    
      elif(S_Level > -70.0 and S_Level <= -53.0):
            GPIO.output(17,1)
            GPIO.output(27,1)
            GPIO.output(22,0)
            print(" Two LEDs Glowing. \n")
    
      elif(S_Level > -83.0 and S_Level <= -70.0):
            GPIO.output(17,1)
            GPIO.output(27,0)
            GPIO.output(22,0)
            print(" One LED Glowing. \n")
        
      else:
            GPIO.output(17,0)
            GPIO.output(27,0)
            GPIO.output(22,0)
            print(" ALL LEDs Off \n")
      #
      
     
     
def All_LEDs_OFF():
  GPIO.output(10,0)
  GPIO.output(17,0)
  GPIO.output(27,0)
  GPIO.output(22,0)
  
  
  



          
parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
args = parser.parse_args()






while True:
    
    time.sleep(1)
    try:
      cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)
      for line in cmd.stdout:
        if 'ESSID' in line:
          print(line.lstrip(' '))
        if 'Frequency' in line:
          #print(line.lstrip(' '))
          Frequency=line[34],line[35],line[36],line[37]
          Frequency=''.join(Frequency)
          print('Frequency = ',Frequency, 'GHz')
          Frequency=float(Frequency)
          Frequency_LED(Frequency)
        if 'Signal level' in line:
          print(line.lstrip(' '))
          Signal_Level=line[43],line[44],line[45],line[46],line[47],line[48],line[49]
          Signal_Level=''.join(Signal_Level)
          print Signal_Level
          Signal_Level=line[43],line[44],line[45]
          Signal_Level=''.join(Signal_Level)
          Signal_Level=float(Signal_Level)
          print Signal_Level
          Signal_LEDs(Signal_Level)
          print('\n')
        
        elif 'Not-Associated' in line:
          print('No signal')
          All_LEDs_OFF()
          print('restarting wifi')
          os.system('sudo ifdown --force wlan0')
          time.sleep(10)
          os.system('sudo ifup wlan0')
  
        
    except KeyboardInterrupt:
      All_LEDs_OFF()
      print('Exiting Program \n\n')
      time.sleep(10)




