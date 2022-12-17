from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Supplier 
from django.http import JsonResponse

def suppliers(request):    
    if request.user.is_authenticated and request.user.userrole.role.role != 'Store Keeper': 
        return render(request, 'suppliers.html',{'nbar': 'suppliers'})

def getSuppliers(request):
    if request.user.is_authenticated and request.user.userrole.role.role != 'Store Keeper':  
        suppliers = Supplier.objects.order_by('id').all().values('id', 'name','address','country','telephone')
        return JsonResponse({'id': 200, 'data': list(suppliers)})

def createSupplier(request):
    if request.user.is_authenticated and request.user.userrole.role.role != 'Store Keeper':  
        pc = Supplier(
                name = request.POST['name'],
                address =  request.POST['address'],
                country =  request.POST['country'],
                telephone =  request.POST['telephone']
            )
        pc.save() 
        return JsonResponse({'id': 200, 'data':"Supplier created successfully!"})