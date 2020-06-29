from django.contrib import admin

# Register your models here.

from .models import CheckingAccountInfo, SavingsAccountInfo, AccountBase, ClientAccount, LoanInfo, ReleaseInfo

admin.site.register([CheckingAccountInfo, SavingsAccountInfo, AccountBase, ClientAccount, LoanInfo, ReleaseInfo])