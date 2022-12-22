from django.shortcuts import render 
from .models import Employee,EmployeeRole,EmployeeContact,EmployeeBankAccount,EmployeePayrollInfo
from django.http import JsonResponse

def employees(request):
    roles = EmployeeRole.objects.all()
    return render(request,'employees.html',{'nbar':'employees','roles':roles})

def employeesPayroll(request):
    roles = EmployeeRole.objects.all()
    return render(request,'employees-payroll.html',{'nbar':'employees-payroll','roles':roles})

def create_employee(request):
    roles = EmployeeRole.objects.all()
    return render(request,'create-employee.html',{'roles':roles})

def employeesData(request):
    role = int(request.GET['role'])
    employees = Employee.objects.all().values('id','name','role__name','nic','image','maritial_status','date_of_birth','gender')
    if(role > 0):
        roleObj = EmployeeRole.objects.get(pk=role)
        employees = employees.filter(role=roleObj)
    return JsonResponse({'id': 200, 'data':list(employees)})

def employeesPayrollData(request):
    role = int(request.GET['role'])
    employees = Employee.objects.all().values('id','name','role__name','employeepayrollinfo__joined_date','employeepayrollinfo__epf_number','employeepayrollinfo__basic_salary','employeepayrollinfo__allowance','employeebankaccount__bank','employeebankaccount__branch','employeebankaccount__account_number')
    if(role > 0):
        roleObj = EmployeeRole.objects.get(pk=role)
        employees = employees.filter(role=roleObj)
    return JsonResponse({'id': 200, 'data':list(employees)})

def employeeRoles(request):
    return render(request,'employee-roles.html',{'nbar':'employee-roles'})

def rolesData(request):
    roles = EmployeeRole.objects.all().values('id','name')
    return JsonResponse({'id':200, 'data':list(roles)})

def createRole(request):
    name = request.POST['name']
    role = EmployeeRole(
        name=name
    )
    role.save()
    return JsonResponse({'id':200, 'data':"Employee role created successfully!"})

def createEmployee(request):
    name = request.POST['name']
    nic = request.POST['nic']
    dob = request.POST['dob']
    gender = request.POST['gender']
    status = request.POST['status']
    image = request.FILES['image']
    address = request.POST['address']
    mobile = request.POST['mobile']
    bank = request.POST['bank']
    branch = request.POST['branch']
    account = request.POST['account']
    epf = request.POST['epf']
    appointmentDate = request.POST['appointmentDate']
    job = request.POST['job']
    basicSalary = request.POST['basicSalary']
    allowance = request.POST['allowance']

    role = EmployeeRole.objects.get(pk=job)
    employee = Employee(
        name=name,
        role=role,
        nic=nic,
        date_of_birth=dob,
        gender=gender,
        maritial_status=status,
        image=image
    )
    employee.save() 

    employee_contact = EmployeeContact(
        employee=employee,
        telephone=mobile,
        address=address
    )
    employee_contact.save()

    employee_bank = EmployeeBankAccount(
        employee=employee,
        bank=bank,
        branch=branch,
        account_number=account
    )
    employee_bank.save()

    employee_payroll = EmployeePayrollInfo(
        employee=employee,
        epf_number = epf,
        joined_date=appointmentDate,
        basic_salary=basicSalary,
        allowance=allowance
    )
    employee_payroll.save()

    return JsonResponse({'id':200,'data':'Success'})