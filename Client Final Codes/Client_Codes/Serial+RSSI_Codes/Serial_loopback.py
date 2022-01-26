import sys
import subprocess
import time
import argparse
import os
import RPi.GPIO as GPIO
import serial
import string
import socket
from threading import Thread

File=open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")

HOST=File.readline()
PORT=int(File.readline())
UserBaudrate=int(File.readline())
bufferSize=int(File.readline())

File.close()


#Constant_Variables
SerialPort = '/dev/ttyS0'



#User-Defined_Variables 
#UserBaudrate = 115200
UserParity = serial.PARITY_NONE
UserStopbits = serial.STOPBITS_ONE
UserBytesize = serial.EIGHTBITS

ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
                    parity=UserParity,
                    stopbits=UserStopbits,
                    bytesize=UserBytesize,
                    timeout=0,
                    write_timeout=0
                    )


def Ser_Write():
      
      while True:
            try:
                  
                  ser.write(str.encode('1'))
                  time.sleep(1)
                  
                          
            except:
                  #print('error')
                  pass
        
#Funtion to read data from Serial Port and sends it to Wi-Fi

def Ser_Read():
    while True:
        try:
              if ser.inWaiting() > 0:
                    data_serial = ser.read(8)
                    print(data_serial)
  
        except:
            pass

Thread(target = Ser_Read).start()
#Thread(target = Ser_Write).start()
