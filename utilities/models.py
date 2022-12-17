from django.db import models 

class Utility(models.Model):
    name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    connected_date = models.DateField(default=None, blank=True, null=True)
    disconnected_date = models.DateField(default=None, blank=True, null=True)
    status = models.IntegerField(default=1)

class UtilityInvoice(models.Model):
    Utility = models.ForeignKey(Utility, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(decimal_places=2,max_digits=6)