from django.contrib import admin

# Register your models here.

from .models import ClientInfo, ClientStaff

admin.site.register([ClientInfo, ClientStaff])