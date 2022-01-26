
import time
import serial
import string
import socket


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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))

try:
    print('Starting program')
    ser.write('Hello World\r\n')
    ser.write('Serial Communication Using Raspberry Pi\r\n')
    ser.write('By: Embedded Laboratory\r\n')
    
    while True:
        
        #s.send(data_wifi)
        #s.send('data_wifi')
        #if ser.inwaiting() > 0:
        data_wifi = s.recv(1024)
        print('data from wifi')
        print(data_wifi)
        ser.write(data_wifi)
        
        data_serial = ser.readline()
        print('data from serial',data_serial)
        s.send(data_serial)
    
    
        
        
    
    ser.close()
    s.close()        
    

#try:
    
   # ser.write('Hello World\r\n')
    #ser.write('Serial Communication Using Raspberry Pi\r\n')
    #ser.write('By: Embedded Laboratory\r\n')
    #print('Data Echo Mode Enabled')
    #while True:
    #    if ser.inWaiting() > 0:
    #        data = ser.readline()
          
            
    #        print(data)
        
                
except KeyboardInterrupt:
    print('Exiting Program')

except:
    print('Error Occurs, Exiting Program')

finally:
    ser.close()
    s.close()
    pass
