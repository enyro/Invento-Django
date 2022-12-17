from django.db import models
 
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
