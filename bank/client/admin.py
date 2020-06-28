from django.contrib import admin

# Register your models here.

from .models import ClientInfo, ClientStaff, ContactInfo

admin.site.register([ClientInfo, ClientStaff, ContactInfo])