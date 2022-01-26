#Libraries and Dependencies

from django import forms
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

#Required Modules

import sys
import os
import time



#Function Definition

def contact(request):


    #Reading Wi-Fi and Serial Data from the Access Point's Default Configuration
    #Comp_2_4 = True
    #Comp_5_2 = False
    print('Contact Function')
    os.system('python /home/pi/Desktop/Write_File.py')
    print('Code Run')
    Read_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
    Default_Static_IP = Read_WiFi_File.readline()
    Default_Frequency = Read_WiFi_File.readline()
    #Default_ESSID = Read_WiFi_File.readline()
    Read_WiFi_File.close()

    #print("DEfault freq below me")
    #print(Default_Static_IP)
    #print(Default_Frequency)

    Read_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf2.txt","r")
    Default_Encryption_Key = Read_WiFi_File.readline()
    Default_Wifi_Mode = Read_WiFi_File.readline()
    Default_Isolate_Client = Read_WiFi_File.readline()
    Default_Wifi_Channel = Read_WiFi_File.readline()
    Read_WiFi_File.close()

    #print("channel below")
    #print(Default_Wifi_Channel)

    Read_Serial_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
    Default_HOST = Read_Serial_File.readline()
    Default_PORT = Read_Serial_File.readline()
    Default_BaudRate = Read_Serial_File.readline()
    Default_BufferSize = Read_Serial_File.readline()
    Read_Serial_File.close()
    print('\nFile Read')


    #Creating Wi-Fi and Serial Configuration Form and giving them Default Values

    class ContactForm(forms.Form):
        Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
        Frequency_Band = forms.CharField(required=False, initial=Default_Frequency)
        Encryption_Key = forms.CharField(required=False, initial=Default_Encryption_Key)
        Wifi_Mode = forms.CharField(required=False, initial=Default_Wifi_Mode)
        Isolate_Client = forms.CharField(required=False, initial=Default_Isolate_Client)
        W_Channel = forms.CharField(required=True, initial=Default_Wifi_Channel)
        S_Host = forms.CharField(required=True, initial=Default_HOST)
        S_Port = forms.CharField(required=True, initial=Default_PORT)
        S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
        S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)


    #Reading the Default Static Routes for the Devices connected to Client

    os.system('python /home/pi/AP-WebApp/40-Routes.py') #cleaning data; read from 40 route in dhcpcd-hooks, then cleaning it and writing IPs directly to Write-40-route in dhcpcd-hooks
    Routes_File = open("/lib/dhcpcd/dhcpcd-hooks/Write-40-route","r")
    Cl=Routes_File.readline()
    Cl_R1=Routes_File.readline()
    Cl_R2=Routes_File.readline()
    Cl_R3=Routes_File.readline()
    Cl_R4=Routes_File.readline()
    Routes_File.close()


    #Creating Static Routes Configuration Form and giving them Default Values

    class ContactForm1(forms.Form):
        Client1 = forms.CharField(required=False, initial=Cl)
        Client_Route1 = forms.CharField(required=False, initial=Cl_R1)
        Client_Route2 = forms.CharField(required=False, initial=Cl_R2)
        Client_Route3 = forms.CharField(required=False, initial=Cl_R3)
        Client_Route4 = forms.CharField(required=False, initial=Cl_R4)


    #Check Frequency Band of Access Point to initialize Checkboxes in HTML
    #print("Started")
    if(Default_Frequency.strip() == "2.4"):
            Comp_2_4 = True
    elif(Default_Frequency.strip() == "5"):
            Comp_2_4 = False

    #Check Encryption Key Method of Access Point to initialize corresponding Checkboxes in HTML
    if(Default_Encryption_Key.strip() == "wpa2"):
            En_Key = True  
    elif(Default_Encryption_Key.strip() == "wpa"):
            En_Key = False

    #Check Wifi Mode of Access Point to initialize corresponding Checkboxes in HTML

    if(Default_Wifi_Mode.strip() == "802.11n"):
            W_Mode = True
    elif(Default_Wifi_Mode.strip() == "802.11ac"):
            W_Mode = False
        
    #Check Frequency Band of Access Point to initialize corresponding Checkboxes in HTML

    if(Default_Isolate_Client.strip() == "No"):
            Iso_Client = True
    elif(Default_Isolate_Client.strip() == "Yes"):
            Iso_Client = False



    #Collecting Data from Wi-Fi and Serial Configuration Form and storing in variables

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
            F_Band = request.POST.getlist('band')
            F_Band = ''.join(F_Band)
            E_Key = request.POST.getlist('key')
            E_Key = ''.join(E_Key)
            Wi_Mode = request.POST.getlist('mode')
            Wi_Mode = ''.join(Wi_Mode)
            Iso_Client = request.POST.getlist('iso')
            Iso_Client = ''.join(Iso_Client)
            Wifi_Ch = form.cleaned_data['W_Channel']
            Reboot = request.POST.getlist('Reboot')
            Reboot = ''.join(Reboot)
            MasterOrClient = request.POST.getlist('MasterOrClient')
            MasterOrClient = ''.join(MasterOrClient)
            print(F_Band)
            S_Host = form.cleaned_data['S_Host']
            S_Port = form.cleaned_data['S_Port']
            S_Baud = form.cleaned_data['S_Baud']
            S_Buffer = form.cleaned_data['S_Buffer']


            print("Reboot =")
            print(Reboot)
            print("MasterOrClient =")
            print(MasterOrClient)

            #Writing the variables in Wifi_Conf1 File

            Write_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","w")
            Write_WiFi_File.write(Static_IP)
            Write_WiFi_File.write("\n")
            if(F_Band=="2"):
                Write_WiFi_File.write("2.4")
                Write_WiFi_File.write("\n")
                print('Writing 2.4 to File')
            elif(F_Band=="5"):
                Write_WiFi_File.write("5")
                Write_WiFi_File.write("\n")
                print('Writing 5 to File')
            Write_WiFi_File.close()


            #Writing the variables in Wifi_Conf2 File

            Write_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf2.txt","w")
            if(E_Key=="2"):
                Write_WiFi_File.write("wpa2")
                Write_WiFi_File.write("\n")
                print('Writing wpa2 to File')
            elif(E_Key=="1"):
                Write_WiFi_File.write("wpa")
                Write_WiFi_File.write("\n")
                print('Writing wpa to File')
            if(Wi_Mode=="1"):
                Write_WiFi_File.write("802.11n")
                Write_WiFi_File.write("\n")
                print('Writing 802.11n to File')
            elif(Wi_Mode=="2"):
                Write_WiFi_File.write("802.11ac")
                Write_WiFi_File.write("\n")
                print('Writing 802.11ac to File')
            if(Iso_Client=="1"):
                Write_WiFi_File.write("No")
                Write_WiFi_File.write("\n")
                print('Writing No to File')
            elif(Iso_Client=="2"):
                Write_WiFi_File.write("Yes")
                Write_WiFi_File.write("\n")
                print('Writing Yes to File')
            Write_WiFi_File.write(Wifi_Ch)
            Write_WiFi_File.write("\n")
            Write_WiFi_File.close()




            #Writing the variables in Serial File

            print('Default BaudRate = ')
            print(Default_BaudRate)
            print('Current S_Baud = ')
            print(S_Baud)

            Write_Serial_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","w")
            Write_Serial_File.write(S_Host)
            Write_Serial_File.write("\n")
            Write_Serial_File.write(S_Port)
            Write_Serial_File.write("\n")
            Write_Serial_File.write(S_Baud)
            Write_Serial_File.write("\n")
            Write_Serial_File.write(S_Buffer)
            Write_Serial_File.close()
            print('\nFile Write')



        #Collecting data from Static Routes Configuration Form and saving in variables

        elif form1.is_valid():
            Reboot = request.POST.getlist('Reboot')
            Reboot = ''.join(Reboot)
            MasterOrClient = request.POST.getlist('MasterOrClient')
            MasterOrClient = ''.join(MasterOrClient)
            print('Form1:  its in Write POST Method')
            Cl1 = form1.cleaned_data['Client1']
            print(Cl1)
            Cl_R1 = form1.cleaned_data['Client_Route1']
            print(Cl_R1)
            Cl_R2 = form1.cleaned_data['Client_Route2']
            print(Cl_R2)
            Cl_R3 = form1.cleaned_data['Client_Route3']
            print(Cl_R3)
            Cl_R4 = form1.cleaned_data['Client_Route4']
            print(Cl_R4)


            #writing the variables in Static Routes File

            Write_Routes_File = open("/lib/dhcpcd/dhcpcd-hooks/40-route","w+")
            if( len(Cl1) != 0):
                if(len(Cl_R1) != 0):
                    Write_Routes_File.write("ip route add " + Cl_R1  + " via " + Cl1 + "\n")
                else:
                    Write_Routes_File.write("\n")
                if(len(Cl_R2) != 0):
                    Write_Routes_File.write("ip route add " + Cl_R2  + " via " + Cl1 + "\n")
                else:
                    Write_Routes_File.write("\n")
                if(len(Cl_R3) != 0):
                    Write_Routes_File.write("ip route add " + Cl_R3  + " via " + Cl1 + "\n")
                else:
                    Write_Routes_File.write("\n")
                if(len(Cl_R4)!=0):
                    Write_Routes_File.write("ip route add " + Cl_R4  + " via " + Cl1 + "\n")
                else:
                    Write_Routes_File.write("\n")
            else:
                Write_Routes_File.write("\n")
            Write_Routes_File.close()



        #Configuring the Access Point on the basis of collected Form Data

        os.system('python /home/pi/Desktop/Read_File.py')



        #READING the Data again from Access Point's updated Configuration

        os.system('python /home/pi/Desktop/Write_File.py')
        print('Code Run')
        Read_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
        Default_Static_IP = Read_WiFi_File.readline()
        Default_Frequency = Read_WiFi_File.readline()
        #Default_ESSID = Read_WiFi_File.readline()
        Read_WiFi_File.close()

        Read_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf2.txt","r")
        Default_Encryption_Key = Read_WiFi_File.readline()
        Default_Wifi_Mode = Read_WiFi_File.readline()
        Default_Isolate_Client = Read_WiFi_File.readline()
        Default_Wifi_Channel = Read_WiFi_File.readline()
        Read_WiFi_File.close()

        Read_Serial_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
        Default_HOST = Read_Serial_File.readline()
        Default_PORT = Read_Serial_File.readline()
        Default_BaudRate = Read_Serial_File.readline()
        Default_BufferSize = Read_Serial_File.readline()
        Read_Serial_File.close()
        print('\nFile Read')


        #Putting the UPDATED Configuration onto the Wi-Fi and Serial Form

        class ContactForm(forms.Form):
            Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
            Frequency_Band = forms.CharField(required=False, initial=Default_Frequency)
            Encryption_Key = forms.CharField(required=False, initial=Default_Encryption_Key)
            Wifi_Mode = forms.CharField(required=False, initial=Default_Wifi_Mode)
            Isolate_Client = forms.CharField(required=False, initial=Default_Isolate_Client)
            W_Channel = forms.CharField(required=False, initial=Default_Wifi_Channel)
            S_Host = forms.CharField(required=True, initial=Default_HOST)
            S_Port = forms.CharField(required=True, initial=Default_PORT)
            S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
            S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)

        #Reading the Updated Configuration of Static Routes

        os.system('python /home/pi/AP-WebApp/40-Routes.py')
        Routes_File = open("/lib/dhcpcd/dhcpcd-hooks/Write-40-route","r")
        Cl=Routes_File.readline()
        Cl_R1=Routes_File.readline()
        Cl_R2=Routes_File.readline()
        Cl_R3=Routes_File.readline()
        Cl_R4=Routes_File.readline()
        Routes_File.close()


        #Putting the Updated Configuration of Static Routes on the Form

        class ContactForm1(forms.Form):
            Client1 = forms.CharField(required=False, initial=Cl)
            Client_Route1 = forms.CharField(required=False, initial=Cl_R1)
            Client_Route2 = forms.CharField(required=False, initial=Cl_R2)
            Client_Route3 = forms.CharField(required=False, initial=Cl_R3)
            Client_Route4 = forms.CharField(required=False, initial=Cl_R4)



    #Updated Frequency Band for the Checkbox

        if(Default_Frequency.strip() == "2.4"):
            Comp_2_4 = True
        elif(Default_Frequency.strip() == "5.2"):
            Comp_2_4 = False

    #Updated Encryption Key Method for Checkbox

        if(Default_Encryption_Key.strip() == "wpa2"):
            En_Key = True  
        elif(Default_Encryption_Key.strip() == "wpa"):
            En_Key = False

    #Updated Wifi Mode for Checkbox

        if(Default_Wifi_Mode.strip() == "802.11n"):
            W_Mode = True
        elif(Default_Wifi_Mode.strip() == "802.11ac"):
            W_Mode = False
        
    #Updated Frequency for Checkbox

        if(Default_Isolate_Client.strip() == "No"):
            Iso_Client = True
        elif(Default_Isolate_Client.strip() == "Yes"):
            Iso_Client = False


        if(Reboot=="1"):
                os.system("sudo reboot")
        else:
                print("Not Rebooting")



        print("Reboot =")
        print(Reboot)
        print("MasterOrClient =")
        print(MasterOrClient)
##        if(MasterOrClient != 1):
##            MoC = 0
##        else:
##            MoC = 1
##
##        print("MasterOrClient =check2   moc")
##        print(MoC)
##        
##        print("MasterOrClient =ceck1 MAster or client")
##        print(MasterOrClient)
        
        if(MasterOrClient=="1"):
                Write_MasterOrClient_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/MasterOrClient.txt","w")
                Write_MasterOrClient_File.write("Client")
                Write_MasterOrClient_File.write("\n")
                Write_MasterOrClient_File.close()
                os.system("sudo reboot")
        else:
                Write_MasterOrClient_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/MasterOrClient.txt","w")
                Write_MasterOrClient_File.write("Master")
                Write_MasterOrClient_File.write("\n")
                Write_MasterOrClient_File.close()





    #Requesting the HTML for send/recieve Data

    return render(request, 'contact.html', context={'form': ContactForm, 'form1': ContactForm1, 'Comp_2_4': Comp_2_4, 'En_Key' : En_Key, 'W_Mode' : W_Mode, 'Iso_Client' : Iso_Client})









