import sys
import subprocess
import time
import argparse
import os




def main():
  parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
  parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
  args = parser.parse_args()

  try:
    cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)
    for line in cmd.stdout:
      if str.encode('ESSID:"') in line:
        #print(line.lstrip(' '))
        ESSID = line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37],line[38],line[39],line[40],line[41],line[42]
        ESSID=''.join(ESSID)
        print(ESSID)
        
      elif str.encode('Not-Associated') in line:
        ESSID = 'No Signal'
        print(ESSID)
    return ESSID        
  except KeyboardInterrupt:
    print('Exiting Program \n\n')
    time.sleep(5)



main()



