from django.shortcuts import render,redirect
from inventory.models import Product
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user = request.user
        if user.userrole.role.role == 'Manager' or user.userrole.role.role == 'Admin':
            return render(request,'dashboard-manager.html',{'nbar': 'dashboard'}) 

        if user.userrole.role.role == 'Chief Accountant' or user.userrole.role.role == 'Admin':
            return render(request,'dashboard-manager.html',{'nbar': 'dashboard'}) 

        if user.userrole.role.role == 'Accountant' or user.userrole.role.role == 'Admin':
            return render(request,'dashboard-manager.html',{'nbar': 'dashboard'}) 

        if user.userrole.role.role == 'Sales Representative' or user.userrole.role.role == 'Admin':
            return render(request,'dashboard-sales.html',{'nbar': 'dashboard'}) 

        if user.userrole.role.role == 'Store Keeper' or user.userrole.role.role == 'Admin':
            products = Product.objects.all().filter(status=1)
            return render(request,'dashboard-store.html',{'nbar': 'dashboard','products':products}) 
    return redirect('signin')

