from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'index.html')
def About(request):
    return render(request, 'about.html')
def Contact(request):
    return render(request, 'contact.html')
def Resume(request):
    return render(request, 'resume.html')
def Portfolio(request):
    return render(request, 'portfolio.html')
def Portfolio_details(request):
    return render(request, 'portfolio-details.html')
def starter_page(request):
    return render(request, 'starter-page.html')