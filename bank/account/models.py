from django.db import models

# Create your models here.
class AbstractAccount(models.Model):
    """
    Abstract Class of Account.
    Fields: account_ID, open_date, is_savings, branch
    
    ! Needs constraint here but I have no idea.

    """

    account_ID = models.CharField(max_length=20, primary_key=True)
    open_date = models.DateField(auto_now=True)
    is_savings = models.BooleanField()

    branch = models.ForeignKey(
        'branch.BranchInfo',
        on_delete=CASCADE
    )

    class Meta:
        abstract = True

class CheckingAccountInfo(AbstractAccount):
    """
    Checking Account Information.
    Fields: overdraft
    """

    overdraft = models.DecimalField(max_digits=20, decimal_places=3, default=0)

    def __str__(self):
        return '%s, %s' % (account_ID, overdraft)

class SavingsAccountInfo(AbstractAccount):
    """
    Savings Account Information.
    Fields: balance, interest_rate, currency_type
    """

    balance = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    interest_rate = models.FloatField()
    currency_type = models.CharField(max_length=10)
        
    def __str__(self):
        return '%s, %s' % (account_ID, balance)

class ClientAccount(models.Model):
    """
    Client to Account Relations
    Fields: client, account, latest_time
    """

    client = models.ForeignKey('client.ClientInfo', on_delete=models.CASCADE)
    account = models.ForeignKey(AbstractAccount, on_delete=models.CASCADE)
    latest_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s, %s' % (client, account, latest_time)

class LoanInfo(models.Model):
    """
    Loans.
    Field: loan_ID, branch, total_amount, clients
    """

    loan_ID = models.CharField(max_length=30, primary_key=True)
    branch = models.ForeignKey('branch.BranchInfo', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=20, decimal_places=3)
    clients = models.ManyToManyField('clients.ClientInfo', on_delete=models.CASCADE)

class IssuranceInfo(models.Model):
    """
    Loan Issurance Information.
    Fields: loan, amount, time
    """

    loan = models.ForeignKey(LoanInfo, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    time = models.DateTimeField(auto_now=True)
