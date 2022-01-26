from .forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

import os

def contact(request):
    message = None

    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            Write_WiFi_File = open("/home/pi/Data.txt","w+")
            Write_WiFi_File.write(contact_name)
            Write_WiFi_File.write("\n")
            Write_WiFi_File.write(contact_email)
            Write_WiFi_File.close()
            print(contact_name)
            print(contact_email)
            #contact_content = form.cleaned_data['contact_content']
            #try:
            #    send_mail('Feedback From ' + contact_name, contact_content, 'from-email-here', [contact_email])
            #except BadHeaderError:
            #    message = "Error: Bad Header."

            #message = "Success. Thank you for your feedback."

    #return render(request, 'contact.html', context={'form': ContactForm, 'message': message})
    return render(request, 'contact.html', context={'form': ContactForm})
