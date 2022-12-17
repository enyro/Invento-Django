from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Customer 
from django.http import JsonResponse

def customers(request): 
    if request.user.is_authenticated and request.user.userrole.role.role != 'Store Keeper':  
        return render(request, 'customers.html',{'nbar':'customers'})

def getCustomers(request):
    if request.user.is_authenticated and request.user.userrole.role.role != 'Store Keeper':  
        customers = Customer.objects.order_by('id').all().values('id', 'name','address','telephone')
        return JsonResponse({'id': 200, 'data': list(customers)})

def createCustomer(request):
    if request.user.is_authenticated and request.user.userrole.role.role != 'Store Keeper':  
        pc = Customer(
                name = request.POST['name'],
                address =  request.POST['address'],
                telephone =  request.POST['telephone']
            )
        pc.save() 
        return JsonResponse({'id': 200, 'data':"Customer created successfully!"})