from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User

class Plan(models.Model):
    class Status(models.IntegerChoices):
        ONGOING = 0
        SUCCESS = 1
        FAILED = 2
        DROPPED = 3

    name = models.TextField()
    description = models.TextField() 
    target_date = models.DateField()
    status = models.IntegerField(choices=Status.choices, default=Status.ONGOING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)

class PlanLog(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.DO_NOTHING)
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now) 