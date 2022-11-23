from django.urls import path

from . import views

urlpatterns = [
    path('employees',views.employees,name='employees'), 
    path('create-employee',views.create_employee,name='create_employee') 
]