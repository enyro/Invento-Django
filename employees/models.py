from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)
    
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

class EmployeeLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now) 

class Leave(models.Model):
    name = models.TextField()
    monthly = models.DecimalField(max_digits=2,decimal_places=1,default=0)
    annually = models.DecimalField(max_digits=2,decimal_places=1,default=0)

class EmployeeLeaveBalance(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,primary_key=True)
    casual = models.DecimalField(max_digits=2,decimal_places=1,default=0)
    annual = models.DecimalField(max_digits=2,decimal_places=1,default=0)
    medical = models.DecimalField(max_digits=2,decimal_places=1,default=0)

class EmployeeLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    Leave = models.ForeignKey(Leave,on_delete=models.DO_NOTHING)
    date = models.DateField()
    days = models.DecimalField(max_digits=2,decimal_places=1,default=0)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True) 
    created_at = models.DateTimeField(default=timezone.now)

class Payroll(models.Model):
    date = models.DateField()
    basic_salary = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    no_pay = models.DecimalField(max_digits=7,decimal_places=2,default=0,null=True)
    epf_liable_salary = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    taxable_salary = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    epf_deduction = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    advance_deduction = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    total_deduction = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    allowance = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    net_salary = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    contribution_12 = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    contribution_3 = models.DecimalField(max_digits=7,decimal_places=2,null=True) 

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    payroll = models.ForeignKey(Payroll,on_delete=models.CASCADE,null=True)
    basic_salary = models.DecimalField(max_digits=7,decimal_places=2)
    no_pay = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    epf_liable_salary = models.DecimalField(max_digits=7,decimal_places=2)
    taxable_salary = models.DecimalField(max_digits=7,decimal_places=2)
    epf_deduction = models.DecimalField(max_digits=7,decimal_places=2)
    advance_deduction = models.DecimalField(max_digits=7,decimal_places=2)
    total_deduction = models.DecimalField(max_digits=7,decimal_places=2)
    allowance = models.DecimalField(max_digits=7,decimal_places=2)
    net_salary = models.DecimalField(max_digits=7,decimal_places=2)
    contribution_12 = models.DecimalField(max_digits=7,decimal_places=2)
    contribution_3 = models.DecimalField(max_digits=7,decimal_places=2)