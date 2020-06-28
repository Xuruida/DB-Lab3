from django.contrib import admin

# Register your models here.

from .models import BranchInfo, StaffInfo, DepartmentInfo

admin.site.register([BranchInfo, StaffInfo, DepartmentInfo])