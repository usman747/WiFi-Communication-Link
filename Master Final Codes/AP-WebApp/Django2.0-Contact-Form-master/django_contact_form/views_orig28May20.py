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
    Comp_2_4 = True
    Comp_5_2 = False
    print('Contact Function')
    os.system('python /home/pi/Desktop/Write_File.py')
    print('Code Run')
    Read_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
    Default_Static_IP = Read_WiFi_File.readline()
    Default_Frequency = Read_WiFi_File.readline()
    Default_ESSID = Read_WiFi_File.readline()
    Read_WiFi_File.close()

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
        S_Host = forms.CharField(required=True, initial=Default_HOST)
        S_Port = forms.CharField(required=True, initial=Default_PORT)
        S_Baud = forms.CharField(required=True, initial=Default_BaudRate)
        S_Buffer = forms.CharField(required=True, initial=Default_BufferSize)


    #Reading the Default Static Routes for the Devices connected to Client

    os.system('python /home/pi/AP-WebApp/40-Routes.py') #cleaning data, read from 40 route, then writing IPs directly to Write-40-route in dhcpcd-hooks
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

##    if(Default_Frequency.strip() == "2.4"):
##            Comp_2_4 = True
##            Comp_5_2 = False
##    elif(Default_Frequency.strip() == "5.2"):
##            Comp_2_4 = False
##            Comp_5_2 = True




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

            #Writing the variables in Wi-Fi File

            Write_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","w")
            Write_WiFi_File.write(Static_IP)
            Write_WiFi_File.write("\n")
            if(F_Band=="2"):
                Write_WiFi_File.write("2.4")
                Write_WiFi_File.write("\n")
                print('Writing 2.4 to File')
            elif(F_Band=="5"):
                Write_WiFi_File.write("5.2")
                Write_WiFi_File.write("\n")
                print('Writing 5.2 to File')
            Write_WiFi_File.close()

            print('Default BaudRate = ')
            print(Default_BaudRate)
            print('Current S_Baud = ')
            print(S_Baud)


            #Writing the variables in Serial File

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



        #Reading the Data again from Access Point's updated Configuration

        os.system('python /home/pi/Desktop/Write_File.py')
        print('Code Run')
        Read_WiFi_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Wifi_Conf1.txt","r")
        Default_Static_IP = Read_WiFi_File.readline()
        Default_Frequency = Read_WiFi_File.readline()
        Default_ESSID = Read_WiFi_File.readline()
        Read_WiFi_File.close()

        Read_Serial_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/Serial_Conf.txt","r")
        Default_HOST = Read_Serial_File.readline()
        Default_PORT = Read_Serial_File.readline()
        Default_BaudRate = Read_Serial_File.readline()
        Default_BufferSize = Read_Serial_File.readline()
        Read_Serial_File.close()
        print('\nFile Read')


        #Putting the Updated Configuration onto the Wi-Fi and Serial Form

        class ContactForm(forms.Form):
            Static_IP = forms.CharField(required=True, initial=Default_Static_IP)
            Frequency_Band = forms.CharField(required=False, initial=Default_Frequency)
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

##        if(Default_Frequency.strip() == "2.4"):
##            Comp_2_4 = True
##            Comp_5_2 = False
##        elif(Default_Frequency.strip() == "5.2"):
##            Comp_2_4 = False
##            Comp_5_2 = True


        if(Reboot=="1"):
                os.system("sudo reboot")
        else:
                print("Not Rebooting")



        print("Reboot =")
        print(Reboot)
        print("MasterOrClient =")
        print(MasterOrClient)

##        if(MasterOrClient=="1"):
##                Write_MasterOrClient_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/MasterOrClient.txt","w")
##                Write_MasterOrClient_File.write("Client")
##                Write_MasterOrClient_File.write("\n")
##                Write_MasterOrClient_File.close()
##                os.system("sudo reboot")
##        else:
##                Write_MasterOrClient_File = open("/home/pi/AP-WebApp/Django2.0-Contact-Form-master/django_contact_form/templates/MasterOrClient.txt","w")
##                Write_MasterOrClient_File.write("Master")
##                Write_MasterOrClient_File.write("\n")
##                Write_MasterOrClient_File.close()





    #Requesting the HTML for send/recieve Data

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



