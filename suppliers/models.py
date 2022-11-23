from django.db import models

# Create your models here.
class supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
