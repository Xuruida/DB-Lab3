from django.contrib import admin

# Register your models here.

from .models import CheckingAccountInfo, SavingsAccountInfo, ClientAccount, LoanInfo, IssuranceInfo

admin.site.register([CheckingAccountInfo, SavingsAccountInfo, ClientAccount, LoanInfo, IssuranceInfo])