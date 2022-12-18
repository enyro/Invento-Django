from django.db import models

class Ledger(models.Model):
    name = models.CharField(max_length=100)

class Account(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    ledger_debit = models.ForeignKey(Ledger, on_delete=models.DO_NOTHING, related_name='debit')
    ledger_credit = models.ForeignKey(Ledger, on_delete=models.DO_NOTHING, related_name='credit')
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    status = models.SmallIntegerField()