import sys
import subprocess
import time
import argparse
import os

#17,27,22,  10

#
#

parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
#parser = argparse.ArgumentParser()
parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
args = parser.parse_args()







    

try:
  cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)
  for line in cmd.stdout:
    if str.encode('Frequency') in line:
      Frequency=line[34],line[35],line[36],line[37]
      Frequency=''.join(Frequency)
      Frequency=float(Frequency)
      print(Frequency)
      #return Frequency
      
    elif str.encode('Not-Associated') in line:
      print('No signal')
          
except KeyboardInterrupt:
  print('Exiting Program \n\n')
  time.sleep(5)




