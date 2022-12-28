from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ledger(models.Model):
    name = models.CharField(max_length=100)

class TrialBalance(models.Model):
    date = models.DateField()
    total = models.DecimalField(decimal_places=2, max_digits=11)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)

class TrialBalanceLedger(models.Model):
    trial_balance = models.ForeignKey(TrialBalance, on_delete=models.CASCADE)
    ledger = models.ForeignKey(Ledger,on_delete=models.DO_NOTHING)
    total = models.DecimalField(decimal_places=2, max_digits=11)

class Account(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    ledger_debit = models.ForeignKey(Ledger, on_delete=models.DO_NOTHING, related_name='debit')
    ledger_credit = models.ForeignKey(Ledger, on_delete=models.DO_NOTHING, related_name='credit')
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    status = models.SmallIntegerField()
    trial_balance_ledger = models.ForeignKey(TrialBalanceLedger,on_delete=models.DO_NOTHING,null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)

class AccountLog(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)  



