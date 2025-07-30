from django.shortcuts import render
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

        if not all([name, email, subject, message]):
            return render(request, 'contact.html', {'error': 'Please fill all required fields.'})

        email_content = f"From: {name} <{email}>\n\nMessage:\n{message}"
        # Save the contact message to the database
        # ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        # subject = f"Contact Form Submission: {subject}"
        try:
            send_mail(
                subject=subject,
                message=email_content,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return render(request, 'contact.html', {'success': 'Your message has been sent. Thank you!'})
        except Exception as e:
            return render(request, 'contact.html', {'error': f"Failed to send: {str(e)}"})

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