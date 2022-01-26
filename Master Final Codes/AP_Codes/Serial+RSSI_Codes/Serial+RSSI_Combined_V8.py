

#_V8_Final_26_06_2019
#_V9_Final_17_10_2019-Auto USB port assigning, no need for writing USB0 OR USB1

import time
import subprocess
import serial
import string
import socket
import sys
from threading import Thread

import os
import argparse
import glob
import RPi.GPIO as GPIO

#time.sleep(5)


#Setting Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#
    
#GPIO Setup

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#
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

#*************************************
#Serial Configuration
#*************************************
File=open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
HOST=File.readline()
HOST=HOST.rstrip("\n") #This line was added on 22/May/20 as s.bind method was giving error because of \n in HOST string
port=int(File.readline())
UserBaudrate=int(File.readline())
bufferSize=int(File.readline())
#print(UserBaudrate)
#print(bufferSize)
File.close()

#time.sleep(5)




#Constant_Variables
#SerialPort = '/dev/ttyS0'

#SerialPort = '/dev/ttyUSB0'

TempPort = glob.glob('/dev/ttyUSB*')
SerialPort = TempPort[0]

#User-Defined Variables
#UserBaudrate = 115200
UserParity = serial.PARITY_NONE
UserStopbits = serial.STOPBITS_ONE
UserBytesize = serial.EIGHTBITS


time.sleep(0.1)

ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
                                parity=UserParity,
                                stopbits=UserStopbits,
                                bytesize=UserBytesize,
                                timeout=0,
                                write_timeout=0
                                )


#def ser_flush():

      #while True:
            #time.sleep(5)
            #ser.flush()


#print('LEDs Check Done')

#******************************************************************************************
#  This is the RSSI LED's function used to turn ON LEDs on the basis of Signal Strength in dbm.

#******************************************************************************************

def Signal_LEDs(S_Level):
    
      #Conditions to Observe
      if (S_Level > -53.0):                # > 75 %
            GPIO.output(17,1)
            GPIO.output(27,1)
            GPIO.output(22,1)
            
            
    
      elif(S_Level > -70.0 and S_Level <= -53.0):
            GPIO.output(17,0)
            GPIO.output(27,1)
            GPIO.output(22,1)
            
    
      elif(S_Level > -83.0 and S_Level <= -70.0):
            GPIO.output(17,0)
            GPIO.output(27,0)
            GPIO.output(22,1)
            
        
      else:
            GPIO.output(17,0)
            GPIO.output(27,0)
            GPIO.output(22,0)

#********************************************************************************************
#********************************************************************************************      





#******************************************************************************************
#  This is the RSSI LED's function used to turn OFF all LEDs when there is no Client connected.

#******************************************************************************************
     
     
def RSSI_LEDs_OFF():
      GPIO.output(17,0)
      GPIO.output(27,0)
      GPIO.output(22,0)

#********************************************************************************************
#********************************************************************************************      




#Configuration to read RSSI from Command line (cmd)
          
parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan interface (default: wlan0)')
args = parser.parse_args()

#




# This while loop is just for checking Serial_Conf values 
# Remove this while loop for Serial Working.

#while(True):
    #File=open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
##File=open("/home/pi/Form1/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
##HOST=File.readline()
##port=int(File.readline())
##UserBaudrate=int(File.readline())
##bufferSize=int(File.readline())
###print(UserBaudrate)
###print(bufferSize)
##File.close()
##
###time.sleep(10)
##
##
##
##
###Constant_Variables
##SerialPort = '/dev/ttyS0'
##
##
###User-Defined Variables
###UserBaudrate = 115200
##UserParity = serial.PARITY_NONE
##UserStopbits = serial.STOPBITS_ONE
##UserBytesize = serial.EIGHTBITS


#Variables
#HOST = "192.168.4.1"        # socket.gethostname()      # Host Address
#port = 4002
backlog = 5                 # 5 is the 'backlog' argument which specifies the maximum number of queued connections
#bufferSize = 1024





#******************************************************************************************
# This Function reads data from Serial Port and sends it to Wi-Fi.

#******************************************************************************************

def Ser_Read_Send_to_Wifi():
   
    while True:       
         #ser.flush()
         #ser.reset_input_buffer()
         #ser.reset_output_buffer()
         #print('reset in read-send-to-wifi \n')
         try:  
            #if ser.inWaiting() > 0:
            data_serial = ser.read(8)
            #data_serial = rcvdata
            #print(data_serial)
            conn.send(data_serial)

            #else:
             #     pass
         except:
            #print('Error')
            pass

#********************************************************************************************
#********************************************************************************************



#********************************************************************************************
# This Function reads data from Wi-Fi and sends it to Serial Port    

#********************************************************************************************

def Read_from_Wifi_Ser_Write():
      global rcvdata
      rcvdata = 1
      #rcvdata1 = conn.recv(1024) 
      while True:
            try:
                rcvdata = conn.recv(bufferSize)           # 1024 is the buffer size
                ser.write(rcvdata)
                #print(rcvdata)
                      
            except:
                  pass


#********************************************************************************************
#********************************************************************************************



#********************************************************************************************
# This Function resets the input and output buffer after every 30 secs    

#********************************************************************************************

def Reset_buffers():
      while True:
            
            time.sleep(30)
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            #print('reset buffers after 30secs \n')


#******************************************************************************************
# This is the ping function used to get the status of the ping.
# if the ping gives a response the Ping_Status is 1 else 0 similarly it is for RSSI_Status
#******************************************************************************************
def Ping_Function(Client_IP):
      global Ping_Status
      global RSSI_Status
      global Ping_Failed
            
      try:
            time.sleep(1)
            #print(Client_IP)
            ping=subprocess.check_output(["ping", "-c", "1", Client_IP])

            #after the response to ping is received we check for TTL in the line if TTL is present we say the ping is successful
            if str.encode('ttl') in ping:
                  Ping_Failed = 0
                  Ping_Status = 1
                  RSSI_Status = 1
                  return Ping_Status
            else:
                  Ping_Status = 0
                  RSSI_Status = 0
                  return Ping_Status
                  

      except:
            #print('Ping Exception')
            if(Ping_Failed == 1):
                  Ping_Status = 0
                  print("\nPing Exception Occured in Ping Function")
                  RSSI_LEDs_OFF()
                  RSSI_Status = 0
                  return Ping_Status
            else:
                  print("\nPing Failed")
                  Ping_Failed = Ping_Failed + 1
                  pass
      
#********************************************************************************************
#********************************************************************************************      
                  
def RSSI():

      global Ping_Status

      Signal_Level_2 =0.0
      
      while True:

            line_counter = 0

            
            if(Ping_Status == 1):

                  cmd = subprocess.Popen('iw dev wlan0 station dump %s' % args.interface, shell=True,stdout=subprocess.PIPE)

                  for line in cmd.stdout:
                      line_counter=line_counter+1
                      if(line_counter==8):

                            # Obtaining Signal Strength in 'dbm' from 'station_dump' command
                            
                            if str.encode('signal') in line:
                                  Signal_Level_1=line[11],line[12],line[13]
                                  Signal = ''.join(chr(i) for i in Signal_Level_1)
                                  Signal_Level_2=float(Signal)
                                  Signal_LEDs(Signal_Level_2)
                                  
                                  break
                              
                            else:
                                  Signal_LEDs(Signal_Level_2)
            
      
                      #print(Code_Run_Counter)
              
                      if(line_counter==0):
                            RSSI_LEDs_OFF()
                            print('\nClient is Disconnected')

                      else:
                            Signal_LEDs(Signal_Level_2)

            else:
                  RSSI_LEDs_OFF()





def PING():      
      
        global RSSI_Status
        RSSI_Status = 0
        
      
        RSSI_LEDs_OFF()
        
        global Ping_Status
        Ping_Status = 0

        global Ping_Failed
        Ping_Failed = 0
        
        Count_For_Wlan_Disconnect=0

        Code_Run_Counter=0
        
        while True:
            
            Code_Run_Counter=Code_Run_Counter+1
    
    
            
            try:
                cmd = subprocess.Popen('iw dev wlan0 station dump %s' % args.interface, shell=True,stdout=subprocess.PIPE)
                cmd1 = subprocess.Popen('iwconfig %s' % args.interface, shell=True,stdout=subprocess.PIPE)
                
                
                
                

                for line in cmd1.stdout:
                    if str.encode('Access Point: Not-Associated') in line:
                        os.system('sh launch_Commands_AP.sh')
                        print('Done Reconfiguration of Hostapd')
                        time.sleep(10)
      

                if(Ping_Status == 0):

                      cmd2=subprocess.check_output(["arp", "-a"])
                      
                      #print('if: Obtaining Client IP and Mac Address')

                      # The following code is to obtain Mac Adress of the Client

                      j=0
                      Client_Mac = []
                      for line in cmd.stdout:
                            if str.encode('Station') in line:
                                  j=10;
                                  line = str(line)
                                  while(True):
                                        if(line[j] != ' '):
                                              Client_Mac.append(line[j])
                                        else:
                                              break
                                        j=j+1
                                  Client_Mac=''.join(Client_Mac)
                                  break

                      
                   

                      # Mac Adress obtained
                
                      # Following code is to obtain IP Adress of Client from it's Mac Adress

                      i=0
                      For_Loop_Counter=0
                      count=0
                      Client_IP = []
                
                      if str.encode(Client_Mac) in cmd2:
                            cmd2 = str(cmd2)
                      
                            while(True):
                                  for j in cmd2:
                                        For_Loop_Counter = For_Loop_Counter + 1
                                  
                                        if(Client_Mac[i] == j):
                                              i = i + 1
                                              count = count + 1
                                              if(count==17):
                                                    break
                                        elif(Client_Mac[i] != j):
                                              i=0
                                              count=0
                                                

                                  if(count==17):
                                        break
                                         
                            index = For_Loop_Counter - 34
                            for j in cmd2:
                                  while(True):
                                        if(cmd2[index] != ')'):
                                              Client_IP.append(cmd2[index])
                                        else:
                                              break
                                        index=index+1
                                  Client_IP=''.join(Client_IP)
                            

                         
                #Ping_Function_Call
                #print(Client_Mac)
                #print(Client_IP)
                Ping_Function(Client_IP)

                #
          
      
            except KeyboardInterrupt:
                RSSI_LEDs_OFF()
                #print('Exiting Program \n\n')

            except:
                  RSSI_LEDs_OFF()
                  #print(' ======================>>>>>>>>>>>>>    Error')
                  pass






# void main()

Thread(target = PING).start()

Thread(target = RSSI).start()

#Thread(target = ser_flush).start()

#time.sleep(20)

print('Configuration in Process \n')
print('Program Started')
##ser = serial.Serial(SerialPort, baudrate=UserBaudrate,
##                                parity=UserParity,
##                                stopbits=UserStopbits,
##                                bytesize=UserBytesize,
##                                timeout=0,
##                                write_timeout=0
##                                )
##    
##ser.write(str.encode('Serial Communication Using Raspberry Pi\r\n'))
##ser.write(str.encode('By: BCube (Pvt).Ltd \r\n'))
##ser.write(str.encode('Waiting for the Client to Connect \r\n'))
##        
while(True):
    try:
        global Serial_Connected  
        Serial_Connected=0
        
        print('Waiting for the Client to Connect \n')
      

        if(RSSI_Status == 0):
              #ser.write(str.encode('Waiting for the Client to Connect \r\n'))
              #print('im in rssi 0')
              time.sleep(1)
              

        elif(RSSI_Status == 1):
              
              #print('host below me')
              #print(HOST)
              #print(port)
              #print(UserBaudrate)
              time.sleep(2)
              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
              #print('bind below me')
              ##s.bind(("192.168.4.1",4002))
              ##s.bind(("192.168.4.1",port))
              s.bind((HOST,port))
              print('Port Created')
              s.listen(backlog)           # 5 is the 'backlog' argument which specifies the maximum number of queued connections
              inputs = [s]
              outputs = []
              message_queues = []

              print('waiting for Client to accept')
              conn, addr = s.accept()
              conn.setblocking(0)
              Serial_Connected=1
              print('Connected')
              #data_extra = ser.read(8)        
              #ser.flush()
              ser.reset_input_buffer()
              ser.reset_output_buffer()
              #print('resetting buffers in main when connection establishes \n')



              try:
                    #time.sleep(1)
                    # this starts  the code for serial communication
                    #ser.write(str.encode('You can now communicate with the Client \r\n'))
        
                    #print('Data Echo Mode Enabled')
    
    
                    Thread(target = Ser_Read_Send_to_Wifi).start()
                    
                    Thread(target = Read_from_Wifi_Ser_Write).start()

                    #Thread(target = Reset_buffers).start()

                    #WiFi_Data_Status = 1
    
                    while True:
                          try:
                                try:
                                      #rcvdata = conn.recv(bufferSize)
                                      if not rcvdata:
                                            ser.write(str.encode('Client stopped sending data. \r\n'))
                                            #WiFi_Data_Status = 0
                                            break
                                      else:
                                            pass
                                except:
                                      pass
                                 
                
                                if(Ping_Status==1):                                                                                             #and WiFi_Data_Status == 1):
                                      continue
                                elif(Ping_Status == 0):                                                                                         #or WiFi_Data_Status == 0):
                                      ser.write(str.encode('Client is disconnected or the code on client side is stopped. \r\n'))
                                      break

                          except:
                                pass
                              
                    #ser.close()
                    s.close()
                    conn.close()

                    #print('Exiting Program Normally \n\n')   
        
        

        
              except KeyboardInterrupt:
                    s.close() 
                    #ser.close()
                    print('Exiting Program \n\n')
                    break
    

              except:
                    print('Error Occurs, Exiting Program \n\n')
                    s.close()
                    break

              finally:
                  #ser.close()
                  s.close()
                  pass


    except:
        print('S.bind Error, Pass')
        time.sleep(5)
        s.close()
        pass







