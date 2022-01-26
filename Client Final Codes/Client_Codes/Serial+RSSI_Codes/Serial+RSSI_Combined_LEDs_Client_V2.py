import sys
import subprocess
import time
import argparse
import os
import glob
import RPi.GPIO as GPIO
import serial
import string
import socket
from threading import Thread



##time.sleep(1)


#_V3_Final_17_10_2019-Auto USB port assigning, no need for writing USB0 OR USB1
# RSSI Configuration and Functions


#17,27,22,  10

#Setting Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#

#GPIO Setup
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#print('Check LEDs are ON or not')
GPIO.output(17,1)
GPIO.output(27,1)
GPIO.output(22,1)
GPIO.output(10,1)

time.sleep(3)

GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)
GPIO.output(10,0)


def Frequency_LED(Frequency):    
      #Conditions to Observe
      if (Frequency >= 5.0):
            GPIO.output(10,1)
      else:
            GPIO.output(10,0)





def Signal_LEDs(S_Level):

    
      #Conditions to Observe
      if (S_Level > -53.0):                # > 75 %
            GPIO.output(17,1)
            GPIO.output(27,1)
            GPIO.output(22,1)
            #print(" All LEDs Glowing. \n")
    
      elif(S_Level > -70.0 and S_Level <= -53.0):
            GPIO.output(22,0)
            GPIO.output(27,1)
            GPIO.output(17,1)
            #print(" Two LEDs Glowing. \n")
    
      elif(S_Level > -83.0 and S_Level <= -70.0):
            GPIO.output(22,0)
            GPIO.output(27,0)
            GPIO.output(17,1)
            #print(" One LED Glowing. \n")
        
      else:
            GPIO.output(17,0)
            GPIO.output(27,0)
            GPIO.output(22,0)
            #print(" ALL LEDs Off \n")
      #
      
     
     
def All_LEDs_OFF():
  GPIO.output(10,0)
  GPIO.output(17,0)
  GPIO.output(27,0)
  GPIO.output(22,0)



parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser = argparse.ArgumentParser()
parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
args = parser.parse_args()



def RSSI():
    global Connection_Status
    
    All_LEDs_OFF()
    while True:
        #time.sleep(1)
        try:
            cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)
            for line in cmd.stdout:
                if(str.encode('ESSID') in line):
                    Connection_Status = 1
                    
                if(str.encode('Frequency') in line):
                    Frequency=line[34],line[35],line[36],line[37]
                    Frequency=''.join(chr(i) for i in Frequency)
                    Frequency=float(Frequency)
                    Frequency_LED(Frequency)
                    
                if(str.encode('Signal level') in line):
                    Signal_Level=line[43],line[44],line[45]
                    Signal_Level=''.join(chr(i) for i in Signal_Level)
                    Signal_Level=float(Signal_Level)
                    Signal_LEDs(Signal_Level)
        
                elif(str.encode('Not-Associated') in line):
                    Connection_Status = 0
                    All_LEDs_OFF()
                    os.system('sudo ifdown --force wlan0')
                    time.sleep(5)
                    os.system('sudo ifup wlan0')

            
        except KeyboardInterrupt:
            All_LEDs_OFF()
            print('Exiting RSSI Program \n\n')
            time.sleep(10)

        except:
              All_LEDs_OFF()
              #print("RSSI Thread Exception")
              pass


# RSSI Configuration and Functions Ended




# Serial Configuration and Functions

# This while loop is just for checking Serial_Conf values 
# Remove this while loop for Serial Working.

#while(True):
    #File=open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
File=open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")

HOST=File.readline()
HOST=HOST.rstrip("\n")  #This line was added on 22/MAy/20 as s.connect function was giving error becasue of \n in HOST string.
PORT=int(File.readline())
UserBaudrate=int(File.readline())
bufferSize=int(File.readline())
File.close()


#Constant_Variables
#SerialPort = '/dev/ttyS0'
#SerialPort = '/dev/ttyUSB0'

TempPort = glob.glob('/dev/ttyUSB*')
SerialPort = TempPort[0]


#User-Defined_Variables 
#UserBaudrate = 115200
UserParity = serial.PARITY_NONE
UserStopbits = serial.STOPBITS_ONE
UserBytesize = serial.EIGHTBITS


#Variables
#HOST = "192.168.4.1"
#PORT = 4002
#bufferSize = 1024

def LEDs_Status_on_WiFi_Data():
      while True:
            try:
                  #print(LED_Data)
                  
                  if(LED_Data==str.encode('1')):
                        GPIO.output(13,1)
                        GPIO.output(19,0)
                        GPIO.output(26,0)
                        #time.sleep(3)
                  elif (LED_Data==str.encode('2')):
                        GPIO.output(13,0)
                        GPIO.output(19,1)
                        GPIO.output(26,0)
                  else:
                        GPIO.output(13,0)
                        GPIO.output(19,0)
                        GPIO.output(26,1)
                        
            
            except:
                  #print('LED Exception')
                  pass


#Function to read data from Wi-Fi and send it to serial port.

def Read_from_Wifi_Ser_Write():
      global LED_Data
      global WiFi_Data_Status
      global data_wifi
      data_wifi = 1
      
      while True:
            try:
                  data_wifi = s.recv(bufferSize)                  # 1024 is the buffer size
                  #data_wifi_recv_len = len(data_wifi)
                  #print(data_wifi)
                  ser.write(data_wifi)
                  #print(data_wifi)
                  #time.sleep(0.000001)
                  #print(data_wifi)
                          
            except:
                  #print('error')
                  pass
        
#Funtion to read data from Serial Port and sends it to Wi-Fi

def Ser_Read_Send_to_Wifi():
    while True:
        try:
              #if ser.inWaiting() > 0:
              data_serial = ser.read(8)
              #data_serial= data_wifi
              #print(data_serial)
              s.send(data_serial)
                    #print(data_serial)  
        except:
            pass



#********************************************************************************************
# This Function resets the input and output buffer after every 30 secs    

#********************************************************************************************

def Reset_buffers():
      while True:
##            
            time.sleep(30)
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            #print('reset buffers after 30secs \n')
            

#Funtion to perform Serial Communication Only

def Serial_Communication_Process():
    print('Serial Communication Started')
    #ser.flush()
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    try:
        #ser.write(str.encode('The Client can now communicate with the AP\r\n'))
           
        Thread(target = Ser_Read_Send_to_Wifi).start()
        Thread(target = Read_from_Wifi_Ser_Write).start()
        #Thread(target = Reset_buffers).start()

        #WiFi_Data_Status = 1
        
        while True:
              try:
                    try:
                          #data_wifi = s.recv(bufferSize)
                          if not data_wifi:
                                ser.write(str.encode('Stopped reading data from Server.\r\n'))
                                #WiFi_Data_Status = 0
                                break
                          else:
                                pass
                                #LED_Data = data_wifi
                    except:
                          pass


                    if(Connection_Status == 1):                                                                               #and WiFi_Data_Status == 1):
                          continue    
                    elif(Connection_Status ==0):                                                                              #or WiFi_Data_Status == 0):
                          ser.write(str.encode('The server is Disconnected or the code is not running on Server\r\n'))
                          break
              except:
                    pass
        s.close()
        print('Exiting Program normally. \n\n')
               
        
    except KeyboardInterrupt:
        print('Exiting Program \n\n')

    except:
        print('Error Occurs, Exiting Program \n\n')

    finally:
        #ser.close()
        s.close()
        pass




def Closing_Previous_Ports(PORT):
      time.sleep(0.1)
      
      while True:

            try:
                  
                  cmd = subprocess.Popen('netstat -an %s' % args.interface, shell=True,stdout=subprocess.PIPE)
            
                  for line in cmd.stdout:
                      if(str.encode(str(PORT)) in line):
                            #print(line.lstrip(str.encode(' ')))
                            Port=line[33],line[34],line[35],line[36],line[37]
                            Opened_Port=''.join(chr(i) for i in Port)
                      #else:
                            #Opened_Port = '0'

                            #This else won't work properly because giving Opened_Port a '0' disconnects the Client from AP so there is no other option except to keep this else empty.

                  Port = Opened_Port

                  os.system('sudo fuser -k ' +Port+ '/tcp')

                  print('Port Terminated')

                  break

                  

            except:
                  
                  print('Port Check Failed')
                  break
     


#def ser_flush():

#      while True:
            #time.sleep(5)
            #ser.flush()



# void main()

Thread(target = RSSI).start()

#Thread(target = LEDs_Status_on_WiFi_Data).start()


global Socket_Status
Socket_Status = 0

print('Configuration in Process \n')
print('Program Started')

Closing_Previous_Ports(PORT)

#print('Port Checked')
#print('mark1')

##time.sleep(2)
#print('Program Started 2')
#serial configuration 

ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
                    parity=UserParity,
                    stopbits=UserStopbits,
                    bytesize=UserBytesize,
                    timeout=0,
                    write_timeout=0
                    )

#Thread(target = ser_flush).start()

#print('Program Started 3')
ser.write(str.encode('Serial Communication Using Raspberry Pi Started\r\n'))
ser.write(str.encode('By: BCube (Pvt).Ltd \r\n'))
#time.sleep(2)
#Method to Connect and Reconnect if the connecton is Failed

#ser.write(str.encode('Further Configuration is in Process\r\n'))
time.sleep(2)
#ser.flush()
#print('mark2')

while True:
      #print('Program Started 4')
      #print(UserBaudrate)
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      connected = False
      
      if(not connected):
        try:
            ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
                    parity=UserParity,
                    stopbits=UserStopbits,
                    bytesize=UserBytesize,
                    timeout=0,
                    write_timeout=0
                    )
            #print('mark3')
            ##s.connect(("192.168.4.1",PORT))
            #HOST="192.168.4.1"
            s.connect((HOST,PORT))
            #print('mark4')
            #s.settimeout(5.0)
            s.setblocking(0)
            ser.write(str.encode('Connection to Server is established\r\n'))
            ser.write(str.encode('You can communicate now.\r\n'))
            Socket_Status = 1
            #print('Server is now Connected \n')
            connected = True
            Serial_Communication_Process()
            Socket_Status = 0
            s.connect((HOST,PORT))
            #s.settimeout(5.0)
            s.setblocking(0)
            #print('mark5')
            break
        except:
            Socket_Status = 0
            ser.write(str.encode('Waiting for the Server to connect\r\n'))
            #print('mark6')
            #print('Waiting for a Server \n')
            #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            connected = False
            pass
      time.sleep(1)
