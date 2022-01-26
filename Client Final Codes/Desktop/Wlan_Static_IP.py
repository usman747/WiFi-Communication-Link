import sys
import subprocess
import time
import argparse
#import ConfigParser
import os

wlan_IP=[]
conf = {}
i=0
with open('/etc/dhcpcd.conf') as fp:
    for line in fp:
        if line.startswith('#'):
            continue
        if(i==0):        
            if 'static ip_address' in line:
                i=1
        elif(i==1):
            if 'static ip_address' in line:
                #print(line.lstrip(''))
                #
                j=18;
                while(True):
                    if(line[j] != '/'):
                        wlan_IP.append(line[j])
                    else:
                        break
                    j=j+1
                wlan_IP=''.join(wlan_IP)      
                i=0

wlan_IP=wlan_IP.rstrip("\n")                                
exit(wlan_IP)
