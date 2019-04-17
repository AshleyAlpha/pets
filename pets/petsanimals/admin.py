from django.contrib import admin
from .models import Pet,Client

# Registering models here.
admin.site.register(Pet)
admin.site.register(Client)
