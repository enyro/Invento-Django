from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone

class Utility(models.Model):
    name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    connected_date = models.DateField(default=None, blank=True, null=True)
    disconnected_date = models.DateField(default=None, blank=True, null=True)
    status = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)

class UtilityInvoice(models.Model):
    Utility = models.ForeignKey(Utility, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(decimal_places=2,max_digits=6)

class UtilityLog(models.Model):
    utility = models.ForeignKey(Utility, on_delete=models.DO_NOTHING)
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now) 

class UtilityInvoiceLog(models.Model):
    utility_invoice = models.ForeignKey(UtilityInvoice, on_delete=models.DO_NOTHING)
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now) 