from django.db import models
 
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
