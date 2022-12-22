from django.urls import path

from . import views

urlpatterns = [
    path('employees',views.employees,name='employees'), 
    path('employees-payroll',views.employeesPayroll,name='employeesPayroll'),
    path('employee-roles',views.employeeRoles,name='employee_roles'), 
    path('create-employee',views.create_employee,name='create_employee'),

    path('api/v1/employees',views.employeesData,name='employee_api'),
    path('api/v1/employees-payroll',views.employeesPayrollData,name='employee_payroll_api'),
    path('api/v1/roles',views.rolesData,name='roles_api'),
    path('api/v1/create-role',views.createRole,name='create_role'),
    path('api/v1/insert-employee',views.createEmployee,name='create_employee_api'),   
]