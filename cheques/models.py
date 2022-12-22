from django.db import models
from customers.models import Customer

class Cheque(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 0
        PASSED = 1
        RETURNED = 2
        REISSUED = 3

    cheque_number = models.IntegerField()
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING) 
    bank = models.TextField()
    account_number = models.BigIntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    image = models.ImageField(upload_to='static/img/cheques/',default='static/img/cheques/default.jpg')
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)
