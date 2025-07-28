from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('resume/', views.Resume, name='resume'),
    path('portfolio/', views.Portfolio, name='portfolio'),
    path('portfolio-details/', views.Portfolio_details, name='portfolio_details'),
    path('starter-page/', views.starter_page, name='starter_page'),
    

    
]
# Is responsible for defining the URL patterns for the personal name application.
# This file maps URLs to views, allowing users to navigate through different pages of the application.