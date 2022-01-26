from django import forms
import os

os.system('python /home/pi/Form/WiFi_Conf_V1.py')
print('Code Run')
Read_WiFi_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","r")
Default_Static_IP = Read_WiFi_File.readline()
Default_ESSID = Read_WiFi_File.readline()
Default_Frequency = Read_WiFi_File.readline()
Read_WiFi_File.close()

Read_Serial_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
Default_HOST = Read_Serial_File.readline()
Default_PORT = Read_Serial_File.readline()
Default_BaudRate = Read_Serial_File.readline()
Default_BufferSize = Read_Serial_File.readline()
Read_Serial_File.close()

class ContactForm(forms.Form):

    Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
    S_Host = forms.CharField(required=True, initial=Default_HOST)
    S_Port = forms.CharField(required=True, initial=Default_PORT)
    S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
    S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)
