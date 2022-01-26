import sys
import subprocess
import time
import argparse
import ConfigParser
#import configparser
import os




Wifi_Conf_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","r")
IP=Wifi_Conf_File.readline()
print(IP)

Parser = ConfigParser.SafeConfigParser()

#Parser.open('/etc/dhcpcd.conf')
Parser.read('/etc/dhcpcd.conf')

Parser.get()


time.sleep(50)
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
print(Static_IP[11][1])

