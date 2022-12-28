from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)

class SupplierLog(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now) 
