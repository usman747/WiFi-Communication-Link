#_V4_Final_28_03_2019_(3:15)

import time
import serial
import string
import socket
from threading import Thread



#Constant_Variables
SerialPort = '/dev/ttyS0'


#User-Defined_Variables 
UserBaudrate = 115200
UserParity = serial.PARITY_NONE
UserStopbits = serial.STOPBITS_ONE
UserBytesize = serial.EIGHTBITS


#Variables
HOST = "192.168.4.1"
PORT = 4002
bufferSize = 1024



#time.sleep(25)



#Function to read data from Wi-Fi and send it to serial port.

def Read_from_Wifi_Ser_Write():

    data_wifi = s.recv(bufferSize)         # 1024 is the buffer size 
    
    if not data_wifi:
        print('\nStopped Reading Data from AP ')
        print('Returning Program')
        s.close()
        return 0
    else:
        print('Reading Data From AP: ')
        print(data_wifi)
        ser.write(data_wifi)
        return 1
        
        
#Funtion to read data from Serial Port and sends it to Wi-Fi

def Ser_Read_Send_to_Wifi():
    while True:
        try:
            data_serial = ser.readline()
            print('Reading Data From Serial Port: ')
            print(data_serial)
            s.send(data_serial)
        except:
            pass
            


#Funtion to perform Serial Communication Only

def Serial_Communication_Process():
    print('Serial Communication Started')

    try:
        time.sleep(2)
        ser.write(str.encode('Serial Communication Using Raspberry Pi\r\n'))
        ser.write(str.encode('By: BCube (Pvt).Ltd \r\n'))
        
        Thread(target = Ser_Read_Send_to_Wifi).start()
    
        while True:
     
            Connection_Status = Read_from_Wifi_Ser_Write()

            if(Connection_Status==0):
                print('AP Disconnected')
                break
        
            
        ser.close()
        s.close()        
        print('Exiting Program Normally \n\n')
        
    except KeyboardInterrupt:
        print('Exiting Program \n\n')

    except:
        print('Error Occurs, Exiting Program \n\n')

    finally:
        ser.close()
        s.close()
        pass




# void main()

print('Configuration in Process \n')
print('Program Started')


#serial configuration 

ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
                    parity=UserParity,
                    stopbits=UserStopbits,
                    bytesize=UserBytesize
                    )

#Method to Connect and Reconnect if the connecton is Failed

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connected = False

while True:
    if(not connected):
        try:
            ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
                    parity=UserParity,
                    stopbits=UserStopbits,
                    bytesize=UserBytesize
                    )
            s.connect((HOST,PORT))
            print('Server is now Connected \n')
            connected = True
            Serial_Communication_Process()
            s.connect((HOST,PORT))    
            break
        except:
            print('Waiting for a Server \n')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            connected = False
            pass
    time.sleep(3)



