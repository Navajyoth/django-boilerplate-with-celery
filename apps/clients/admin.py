from django.contrib import admin

from apps.clients.models import Client, Feed
# Register your models here.

admin.site.register(Client)
admin.site.register(Feed)

