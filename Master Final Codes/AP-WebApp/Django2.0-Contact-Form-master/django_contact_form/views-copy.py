#from .forms import ContactForm
from django import forms
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

import sys
import os
import time



def contact(request):

    print('Contact Function')
    os.system('python /home/pi/Desktop/Write_File.py')
    print('Code Run')
    Read_WiFi_File = open("/home/pi/Form1/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
    Default_Static_IP = Read_WiFi_File.readline()
    Default_Frequency = Read_WiFi_File.readline()
    Default_ESSID = Read_WiFi_File.readline()
    Read_WiFi_File.close()

    Read_Serial_File = open("/home/pi/Form1/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
    Default_HOST = Read_Serial_File.readline()
    Default_PORT = Read_Serial_File.readline()
    Default_BaudRate = Read_Serial_File.readline()
    Default_BufferSize = Read_Serial_File.readline()
    Read_Serial_File.close()
    print('\nFile Read')

    class ContactForm(forms.Form):
        Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
        Frequency_Band = forms.CharField(required=False, initial=Default_Frequency)
        S_Host = forms.CharField(required=True, initial=Default_HOST)
        S_Port = forms.CharField(required=True, initial=Default_PORT)
        S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
        S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)


    class ContactForm1(forms.Form):
        Client1 = forms.CharField(required=False)
        Client_Route1 = forms.CharField(required=False)
        Client_Route2 = forms.CharField(required=False)
        Client_Route3 = forms.CharField(required=False)
        Client_Route4 = forms.CharField(required=False)


    if(Default_Frequency.strip() == "2.4"):
            Comp_2_4 = True
            Comp_5_2 = False
    elif(Default_Frequency.strip() == "5.2"):
            Comp_2_4 = False
            Comp_5_2 = True




    if request.method == 'GET':
        print('its in GET Method')
        form = ContactForm()
        form1= ContactForm1()

    elif request.method == 'POST':
        form = ContactForm(request.POST)
        form1 = ContactForm1(request.POST)

        if form.is_valid():
            print('Form:its in Write POST Method')
            Static_IP = form.cleaned_data['Static_IP']
            F_Band1 = request.POST.getlist('band1')
            F_Band1 = ''.join(F_Band1)
            print(F_Band1)
            F_Band2 = request.POST.getlist('band2')
            F_Band2 = ''.join(F_Band2)
            print(F_Band2)
            S_Host = form.cleaned_data['S_Host']
            S_Port = form.cleaned_data['S_Port']
            S_Baud = form.cleaned_data['S_Baud']
            S_Buffer = form.cleaned_data['S_Buffer']

        elif form1.is_valid():
            print('Form1:  its in Write POST Method')
            Client1 = form1.cleaned_data['Client1']
            print(Client1)
            Client_Route1 = form1.cleaned_data['Client_Route1']
            print(Client_Route1)



        Write_WiFi_File = open("/home/pi/Form1/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","w")
        Write_WiFi_File.write(Static_IP)
        Write_WiFi_File.write("\n")
        if(F_Band1=="2"):
            Write_WiFi_File.write("2.4")
            Write_WiFi_File.write("\n")
            print('Writing 2.4 to File')
        elif(F_Band2=="5"):
            Write_WiFi_File.write("5.2")
            Write_WiFi_File.write("\n")
            print('Writing 5.2 to File')
        Write_WiFi_File.close()


        print('Default BaudRate = ')
        print(Default_BaudRate)
        print('Current S_Baud = ')
        print(S_Baud)

        Write_Serial_File = open("/home/pi/Form1/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","w")
        Write_Serial_File.write(S_Host)
        Write_Serial_File.write("\n")
        Write_Serial_File.write(S_Port)
        Write_Serial_File.write("\n")
        Write_Serial_File.write(S_Baud)
        Write_Serial_File.write("\n")
        Write_Serial_File.write(S_Buffer)
        Write_Serial_File.close()
        print('\nFile Write')



        os.system('python /home/pi/Desktop/Read_File.py')
        #time.sleep(1)

        os.system('python /home/pi/Desktop/Write_File.py')
        print('Code Run')
        Read_WiFi_File = open("/home/pi/Form1/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
        Default_Static_IP = Read_WiFi_File.readline()
        Default_Frequency = Read_WiFi_File.readline()
        Default_ESSID = Read_WiFi_File.readline()
        Read_WiFi_File.close()

        Read_Serial_File = open("/home/pi/Form1/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
        Default_HOST = Read_Serial_File.readline()
        Default_PORT = Read_Serial_File.readline()
        Default_BaudRate = Read_Serial_File.readline()
        Default_BufferSize = Read_Serial_File.readline()
        Read_Serial_File.close()
        print('\nFile Read')

        class ContactForm(forms.Form):
            Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
            Frequency_Band = forms.CharField(required=False, initial=Default_Frequency)
            S_Host = forms.CharField(required=True, initial=Default_HOST)
            S_Port = forms.CharField(required=True, initial=Default_PORT)
            S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
            S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)



        class ContactForm1(forms.Form):
            Client1 = forms.CharField(required=False)
            Client_Route1 = forms.CharField(required=False)
            Client_Route2 = forms.CharField(required=False)
            Client_Route3 = forms.CharField(required=False)
            Client_Route4 = forms.CharField(required=False)



        if(Default_Frequency.strip() == "2.4"):
            Comp_2_4 = True
            Comp_5_2 = False
        elif(Default_Frequency.strip() == "5.2"):
            Comp_2_4 = False
            Comp_5_2 = True



    return render(request, 'contact.html', context={'form': ContactForm, 'form1': ContactForm1, 'Default_Static_IP': Default_Static_IP, 'Default_ESSID': Default_ESSID, 'Default_Frequency': Default_Frequency, 'Comp_2_4': Comp_2_4, 'Comp_5_2': Comp_5_2})







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



