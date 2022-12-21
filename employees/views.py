from django.shortcuts import render 
from .models import Employee,EmployeeRole
from django.http import JsonResponse

def employees(request):
    roles = EmployeeRole.objects.all()
    return render(request,'employees.html',{'nbar':'employees','roles':roles})

def create_employee(request):
    return render(request,'create-employee.html',{})

def employeesData(request):
    role = int(request.GET['role'])
    employees = Employee.objects.all().values('id','name','role__name','nic','epf_number','telephone','address')
    if(role > 0):
        roleObj = EmployeeRole.objects.get(pk=role)
        employees = employees.filter(role=roleObj)
    return JsonResponse({'id': 200, 'data':list(employees)})