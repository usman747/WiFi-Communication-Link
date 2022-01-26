import sys
import subprocess
import time
import argparse
import RPi.GPIO as GPIO




def Frequency_LED(Frequency):
      
      #Setting Mode
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      #
    
      #GPIO Setup
      GPIO.setup(4, GPIO.OUT)
      #
    
      #Conditions to Observe
      if (Frequency >= 5.0):
            GPIO.output(4,1)
            print(" 5 GHz LED Glowing. \n")
      else:
            GPIO.output(4,0)
            print(" 5 GHz LED Not Glowing. \n")




def Signal_LEDs(S_Quality):
      
      #Setting Mode
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      #
    
      #GPIO Setup
      GPIO.setup(15, GPIO.OUT)
      GPIO.setup(16, GPIO.OUT)
      GPIO.setup(1, GPIO.OUT)
      #
    
      #Conditions to Observe
      if (S_Quality > 75.0):
            GPIO.output(15,1)
            GPIO.output(16,1)
            GPIO.output(1,1)
            print(" All LEDs Glowing. \n")
    
      elif(S_Quality > 50.0 & S_Quality <= 75.0):
            GPIO.output(15,1)
            GPIO.output(16,1)
            GPIO.output(1,0)
            print(" Two LEDs Glowing. \n")
    
      elif(S_Quality > 25.0 & S_Quality <= 50.0):
            GPIO.output(15,1)
            GPIO.output(16,0)
            GPIO.output(1,0)
            print(" One LED Glowing. \n")
        
      else:
            GPIO.output(15,0)
            GPIO.output(16,0)
            GPIO.output(1,0)
            print(" ALL LEDs Off \n")
      #
      
          
parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
args = parser.parse_args()




while True:
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
        
        if 'Link Quality' in line:
            #print(line.lstrip(' '))
            Quality_Num=line[23],line[24]
            Quality_Den=line[26],line[27]
            Quality_Num=''.join(Quality_Num)
            Quality_Den=''.join(Quality_Den)
            
            Signal_Quality = (float(Quality_Num)/float(Quality_Den))*100
            print('Signal_Quality in Percentage = ',Signal_Quality)
            Signal_LEDs(Signal_Quality)
            
            print('\n\n')
        
        elif 'Not-Associated' in line:
            print('No signal')
    
    
    time.sleep(2)











#from termcolor import colored
#print(colored('\n    P', 'red'), colored('e', 'yellow'), colored('n', 'green'), colored('t', 'white'), colored('e', 'cyan'), colored('s', 'blue'), colored('t', 'magenta'), colored(' - ', 'white'), colored('R', 'red'), colored('a', 'yellow'), colored('b', 'green'), colored('b', 'white'), colored('i', 'cyan'), colored('t\n', 'blue'))


#def String_to_float(Signal_Quality):
#    return float(Signal_Quality.lstrip(''))



#Quality_Num_Float = String_to_float(Quality_Num)
#print Quality_Float






