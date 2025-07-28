from django.shortcuts import render,redirect
from .models import ContactMessage
from  django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def Index(request):
    return render(request, 'index.html')
def About(request):
    return render(request, 'about.html')
def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
            )
        full_message = f"Message from {name} <{email}>:\n\n{message}"
        send_mail (
        subject,
        full_message,
        settings.DEFAULT_FROM_EMAIL
        [settings .CONTACT_RECEIVER_EMAIL],
     )
        messages.success(request,"Your message has been sent successfully!")
        return redirect('contact')
    return render(request, 'contact.html')

        # Process the form data here
        # Here you would typically save the contact message to the database
        # For example: ContactMessage.objects.create(name=name, email=email, subject=subject, 
        # message=message)
def Resume(request):
    return render(request, 'resume.html')
def Portfolio(request):
    return render(request, 'portfolio.html')
def Portfolio_details(request):
    return render(request, 'portfolio-details.html')
def starter_page(request):
    return render(request, 'starter-page.html')


# Is responsible for handling the views of the personal name application.
# This file contains the logic for rendering different pages of the application, such as index,
#  about, contact, etc.