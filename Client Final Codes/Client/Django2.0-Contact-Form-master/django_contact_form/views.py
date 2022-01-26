#from .forms import ContactForm
from django import forms
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

import sys
import os
import time



def contact(request):

    print('Contact Function')
    #time.sleep(3)
    #message = None

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
    print('\nFile Read')

    class ContactForm(forms.Form):
        Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
        S_Host = forms.CharField(required=True, initial=Default_HOST)
        S_Port = forms.CharField(required=True, initial=Default_PORT)
        S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
        S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)


    if request.method == 'GET':
        print('its in GET Method')
        form = ContactForm()

    elif request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('its in Write POST Method')
            Reboot = request.POST.getlist('Reboot')
            Reboot = ''.join(Reboot)
            ClientOrMaster = request.POST.getlist('ClientOrMaster')
            ClientOrMaster = ''.join(ClientOrMaster)
            Static_IP = form.cleaned_data['Static_IP']
            S_Host = form.cleaned_data['S_Host']
            S_Port = form.cleaned_data['S_Port']
            S_Baud = form.cleaned_data['S_Baud']
            S_Buffer = form.cleaned_data['S_Buffer']


        Write_WiFi_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf.txt","w")
        Write_WiFi_File.write(Static_IP)
        Write_WiFi_File.close()

            #print(type(Default_BaudRate))
            #if S_Baud == Default_BaudRate:
        print('Default BaudRate = ')
        print(Default_BaudRate)
        print('Current S_Baud = ')
        print(S_Baud)

        Write_Serial_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","w")
        Write_Serial_File.write(S_Host)
        Write_Serial_File.write("\n")
        Write_Serial_File.write(S_Port)
        Write_Serial_File.write("\n")
        Write_Serial_File.write(S_Baud)
        Write_Serial_File.write("\n")
        Write_Serial_File.write(S_Buffer)
        Write_Serial_File.close()
        print('\nFile Write')


        os.system('python /home/pi/Dhcpcd_Write_IP.py')


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
        print('\nFile Read')

        class ContactForm(forms.Form):
            Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
            S_Host = forms.CharField(required=True, initial=Default_HOST)
            S_Port = forms.CharField(required=True, initial=Default_PORT)
            S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
            S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)


        if(Reboot == '1'):
                os.system('sudo reboot')
        else:
                print('System not Rebooted')

        if(ClientOrMaster == '1'):
                Write_MasterOrClient_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/MasterOrClient.txt","w")
                Write_MasterOrClient_File.write("Master")
                Write_MasterOrClient_File.write("\n")
                Write_MasterOrClient_File.close()
                os.system("sudo reboot")
        else:
                Write_MasterOrClient_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/MasterOrClient.txt","w")
                Write_MasterOrClient_File.write("Client")
                Write_MasterOrClient_File.write("\n")
                Write_MasterOrClient_File.close()



    return render(request, 'contact.html', context={'form': ContactForm, 'Default_Static_IP': Default_Static_IP, 'Default_ESSID': Default_ESSID, 'Default_Frequency': Default_Frequency })








#def write_conf(request):
    #print('Write Function')

    #if request.method == 'GET':
    #    print('its in GET Method')
    #    form = ContactForm()

    #elif request.method == 'POST':
    #    form = ContactForm(request.POST)

    #    if form.is_valid():
    #        print('its in Write POST Method')
    #        Static_IP = form.cleaned_data['Static_IP']
    #        S_Host = form.cleaned_data['S_Host']
    #        S_Port = form.cleaned_data['S_Port']
    #        Var_S_Baud = form.cleaned_data['S_Baud']
    #        S_Buffer = form.cleaned_data['S_Buffer']
    #        Write_WiFi_File = open("/home/pi/Wifi_Conf.txt","w")
    #        Write_WiFi_File.write(Static_IP)
    #        Write_WiFi_File.close()

    #        Write_Serial_File = open("/home/pi/Form/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","w")
    #        Write_Serial_File.write(S_Host)
    #        Write_Serial_File.write("\n")
    #        Write_Serial_File.write(S_Port)
    #        Write_Serial_File.write("\n")
    #        Write_Serial_File.write(S_Baud)
    #        Write_Serial_File.close()
    #        print('\nFile Write')
    #        print(S_Baud)
    #        time.sleep(1)
    #return render(request, 'contact.html', context={'form': ContactForm})



