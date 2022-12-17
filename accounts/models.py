from django.db import models

class Ledger(models.Model):
    name = models.CharField(max_length=100)
