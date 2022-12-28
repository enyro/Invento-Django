from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone

class Cheque(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 0
        PASSED = 1
        RETURNED = 2
        REISSUED = 3

    cheque_number = models.IntegerField()
    date = models.DateField()
    remarks = models.TextField() 
    bank = models.TextField()
    account_number = models.BigIntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    image = models.ImageField(upload_to='static/img/cheques/',default='static/img/cheques/default.jpg')
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)

class ChequeLog(models.Model):
    cheque = models.ForeignKey(Cheque, on_delete=models.DO_NOTHING)
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now) 