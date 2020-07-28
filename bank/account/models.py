from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class AccountBase(models.Model):
    """
    Account Base Class.
    Fields: account_ID, open_date, is_savings, branch
    """

    account_ID = models.CharField(max_length=20, primary_key=True)
    open_date = models.DateField(default=datetime.date.today)
    is_savings = models.BooleanField()

    branch = models.ForeignKey(
        'branch.BranchInfo',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s" % self.account_ID

class CheckingAccountInfo(models.Model):
    """
    Checking Account Information.
    Fields: overdraft
    """

    account_base = models.OneToOneField(
        AccountBase, on_delete=models.CASCADE, related_name="checking")
    overdraft = models.DecimalField(max_digits=20, decimal_places=3, default=0)

    def __str__(self):
        return '%s, %s' % (self.account_base, self.overdraft)

class SavingsAccountInfo(models.Model):
    """
    Savings Account Information.
    Fields: balance, interest_rate, currency_type
    """

    account_base = models.OneToOneField(
        AccountBase, on_delete=models.CASCADE, related_name="savings")
    balance = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    interest_rate = models.FloatField()
    currency_type = models.CharField(max_length=10)
        
    def __str__(self):
        return '%s, %s' % (self.account_base, self.balance)

class ClientAccount(models.Model):
    """
    Client to Account Relations
    Fields: client, account, latest_time
    """

    client = models.ForeignKey('client.ClientInfo', on_delete=models.CASCADE)
    account = models.ForeignKey(AccountBase, on_delete=models.CASCADE)
    latest_time = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['client', 'account'],
                name='unique_cl_ac'
            )
        ]
    def __str__(self):
        return '%s, %s, %s' % (self.client, self.account, self.latest_time)

class LoanInfo(models.Model):
    """
    Loans.
    Field: loan_ID, branch, total_amount, clients
    """

    loan_ID = models.CharField(max_length=30, primary_key=True)
    branch = models.ForeignKey('branch.BranchInfo', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=20, decimal_places=3)
    clients = models.ManyToManyField('client.ClientInfo')
    create_time = models.DateTimeField(default=timezone.now)

    def get_releases(self):
        return ReleaseInfo.objects.filter(loan=self)
    
    def get_remaining_amount(self):
        return self.total_amount - sum([release.amount for release in self.get_releases()])

class ReleaseInfo(models.Model):
    """
    Loan Release Information.
    Fields: loan, amount, time
    """

    loan = models.ForeignKey(LoanInfo, related_name='releases',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    time = models.DateTimeField(default=timezone.now)
