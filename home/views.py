from django.shortcuts import render,redirect
from inventory.models import product
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user = request.user
        if user.user_role.role.role == 'Manager' or user.user_role.role.role == 'Admin':
            return render(request,'dashboard-manager.html',{'nbar': 'dashboard'}) 

        if user.user_role.role.role == 'Chief Accountant' or user.user_role.role.role == 'Admin':
            return render(request,'dashboard-manager.html',{'nbar': 'dashboard'}) 

        if user.user_role.role.role == 'Accountant' or user.user_role.role.role == 'Admin':
            return render(request,'dashboard-manager.html',{'nbar': 'dashboard'}) 

        if user.user_role.role.role == 'Sales Representative' or user.user_role.role.role == 'Admin':
            return render(request,'dashboard-sales.html',{'nbar': 'dashboard'}) 

        if user.user_role.role.role == 'Store Keeper' or user.user_role.role.role == 'Admin':
            products = product.objects.all().filter(status=1)
            return render(request,'dashboard-store.html',{'nbar': 'dashboard','products':products}) 
    return redirect('signin')

