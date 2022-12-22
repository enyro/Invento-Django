from django.db import models
 
class EmployeeRole(models.Model):
    name = models.TextField()

class Employee(models.Model):
    class EmployeeStatus(models.IntegerChoices):
        ACTIVE = 1
        RESIGNED = 2

    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'

    name = models.TextField()
    role = models.ForeignKey(EmployeeRole, on_delete=models.DO_NOTHING)
    nic = models.TextField()  
    date_of_birth = models.DateField()
    gender = models.CharField(choices=Gender.choices, max_length=1)
    maritial_status = models.TextField()
    emloyee_status = models.IntegerField(choices=EmployeeStatus.choices, default=EmployeeStatus.ACTIVE)
    image = models.ImageField(upload_to='static/img/employees/',default='static/img/employees/default.jpg')
    
class EmployeeContact(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,primary_key=True)
    telephone = models.IntegerField()
    address = models.TextField()

class EmployeeBankAccount(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,primary_key=True)
    bank = models.TextField()
    branch = models.TextField()
    account_number = models.BigIntegerField()

class EmployeePayrollInfo(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,primary_key=True)
    epf_number = models.TextField()
    joined_date = models.DateField() 
    basic_salary = models.IntegerField()
    allowance = models.IntegerField()