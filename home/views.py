from django.shortcuts import render,redirect
from inventory.models import Product,InvoiceProduct,Invoice,ImportProduct
from django.utils import timezone

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user = request.user
        if user.userrole.role.role == 'Admin':
            return redirect('/admin/')
        if user.userrole.role.role == 'Manager':
            return render(request,'dashboard-manager.html',{'nbar': 'dashboard'}) 

        if user.userrole.role.role == 'Chief Accountant':
            products = Product.objects.all().filter(status=1)
            return render(request,'dashboard-accountant.html',{'nbar': 'dashboard','products':products}) 

        if user.userrole.role.role == 'Accountant':
            products = Product.objects.all().filter(status=1)
            return render(request,'dashboard-accountant.html',{'nbar': 'dashboard','products':products}) 

        if user.userrole.role.role == 'Sales Representative':
            products = Product.objects.all().filter(status=1)
            return render(request,'dashboard-sales.html',{'nbar': 'dashboard','products':products}) 

        if user.userrole.role.role == 'Store Keeper':
            products = Product.objects.all().filter(status=1)
            date = timezone.now()
            loads = InvoiceProduct.objects.all().filter(invoice__delivery_date__gte=date)
            upcomingloads = ImportProduct.objects.all().filter(invoice__arrival_date__gte=date)
            return render(request,'dashboard-store.html',{'nbar': 'dashboard','products':products,'loads':loads,'upcomingloads':upcomingloads}) 
    return redirect('signin')

