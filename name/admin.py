from django.contrib import admin
from .models import ContactMessage

# Register your models here.
 

#  Is responsible for managing the admin interface for personal names.
# This file allows you to customize how personal names are displayed and managed
#  in the Django admin panel


admin.site.register(ContactMessage)





