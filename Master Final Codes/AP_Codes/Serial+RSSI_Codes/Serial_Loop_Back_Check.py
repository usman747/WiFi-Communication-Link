import time
import subprocess
import serial
import string
import socket
import sys
from threading import Thread


File=open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
HOST=File.readline()
port=int(File.readline())
UserBaudrate=int(File.readline())
bufferSize=int(File.readline())
print(UserBaudrate)
print(bufferSize)
File.close()

#time.sleep(10)




#Constant_Variables
SerialPort = '/dev/ttyS0'


#User-Defined Variables
#UserBaudrate = 115200
UserParity = serial.PARITY_NONE
UserStopbits = serial.STOPBITS_ONE
UserBytesize = serial.EIGHTBITS


def Ser_Read():
    
    while True:
        try:
            if ser.inWaiting() > 0:
                #print('Reading ...')
                data_serial = ser.read()
                print(data_serial)
            #conn.send(data_serial)
            
            #else:
             #     pass
        except:
            #print('Error')
            pass


def Ser_Write():
      global rcvdata
      rcvdata = 1
      while True:
            try:
                #rcvdata = conn.recv(bufferSize)           # 1024 is the buffer size
                ser.write(str.encode('5'))
                time.sleep(1)
                #print('5')
                      
            except:
                  pass


#********************************************************************************************
#********************************************************************************************


Thread(target = Ser_Write).start()

Thread(target = Ser_Read).start()

print('Configuration in Process \n')
print('Program Started')
ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
                                parity=UserParity,
                                stopbits=UserStopbits,
                                bytesize=UserBytesize,
                                timeout=0,
                                write_timeout=0
                                )

