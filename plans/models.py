from django.db import models 
from django.utils import timezone
class Plan(models.Model):
    class Status(models.IntegerChoices):
        ONGOING = 0
        SUCCESS = 1
        FAILED = 2
        DROPPED = 3

    name = models.TextField()
    description = models.TextField()
    created_date = models.DateField(default=timezone.now)
    target_date = models.DateField()
    status = models.IntegerField(choices=Status.choices, default=Status.ONGOING)