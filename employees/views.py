from django.shortcuts import render

# Create your views here.

def employees(request):
    return render(request,'employees.html',{'nbar':'employees'})

def create_employee(request):
    return render(request,'create-employee.html',{})