import sys
import subprocess
import time
import argparse
import ConfigParser
#import configparser
import os


#Client_IP=os.popen("sudo nano /etc/dhcpcd.conf").read()
#print(Client_IP)

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

