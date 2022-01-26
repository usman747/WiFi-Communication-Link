#Copy

import time
import serial
import string
import socket
from threading import Thread


#time.sleep(25)


#Function to read data from Wi-Fi and send it to serial port.

def Read_from_Wifi_Ser_Write():
    while True:
        data_wifi = s.recv(buffer_size)         # 1024 is the buffer size 
        print('data from wifi')
        print(data_wifi)
        ser.write(data_wifi)
        
        
#Funtion to read data from Serial Port and sends it to Wi-Fi

def Ser_Read_Send_to_Wifi():
    data_serial = ser.readline()
    print('data from serial',data_serial)
    s.send(data_serial)
    


print('Starting program')

#serial configuration 

ser = serial.Serial('/dev/ttyS0', baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)

HOST = "192.168.4.1"
PORT = 4002
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))

try:
    print('Starting program')
    ser.write('Hello World\r\n')
    ser.write('Serial Communication Using Raspberry Pi\r\n')
    ser.write('BCube (Pvt).Ltd \r\n')
    
    Thread(target = Read_from_Wifi_Ser_Write).start()
    
    while True:
                
        Ser_Read_Send_to_Wifi()
        
        
    ser.close()
    s.close()        
    
        
                
except KeyboardInterrupt:
    print('Exiting Program')

except:
    print('Error Occurs, Exiting Program')

finally:
    ser.close()
    s.close()
    pass
