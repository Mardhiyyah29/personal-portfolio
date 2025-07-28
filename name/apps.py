from django.apps import AppConfig


class NameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'name'

# Is responsible for configuring the personal name application.
# This file sets up the application and its models, ensuring they are ready for use in the Django project.