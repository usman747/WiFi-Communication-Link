import sys
import subprocess
import time
import argparse
import ConfigParser
import os




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

    cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)

    Wifi_Conf_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","w+")

    Wifi_Conf_File.write(Static_IP[11][1])
    Wifi_Conf_File.write("\n")

    for line in cmd.stdout:
      if str.encode('ESSID:"') in line:
        ESSID = line.lstrip(' ')
        #ESSID = line[30],line[31],line[32],line[33],line[34],line[35],line[36],line[37],line[38],line[39],line[40],line[41],line[42]
        #ESSID=''.join(ESSID)
        Wifi_Conf_File.write(ESSID)
        #print(ESSID)


      if str.encode('Frequency') in line:
        Frequency=line[34],line[35],line[36],line[37]
        Frequency=''.join(Frequency)
        #Frequency=float(Frequency)
        Wifi_Conf_File.write(Frequency)
        #print(Frequency)

      elif str.encode('Not-Associated') in line:
        ESSID = 'No Signal'
        Frequency = 0.0
        #print(ESSID)
        #print(Frequency)

    Wifi_Conf_File.close()
  except KeyboardInterrupt:
    print('Exiting Program \n\n')
    time.sleep(5)



main()



