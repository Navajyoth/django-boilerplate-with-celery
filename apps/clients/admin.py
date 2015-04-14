from django.contrib import admin

from .models import Client, MedicalHistory, ClientFeed
# Register your models here.

admin.site.register(Client)
admin.site.register(MedicalHistory)
admin.site.register(ClientFeed)
