from django.db import models
 
class EmployeeRole(models.Model):
    name = models.TextField()

class Employee(models.Model):
    class EmployeeStatus(models.IntegerChoices):
        ACTIVE = 1
        RESIGNED = 2

    name = models.TextField()
    role = models.ForeignKey(EmployeeRole, on_delete=models.DO_NOTHING)
    nic = models.TextField()
    epf_number = models.TextField()
    telephone = models.IntegerField()
    address = models.TextField()
    emloyee_status = models.IntegerField(choices=EmployeeStatus.choices, default=EmployeeStatus.ACTIVE)
    
