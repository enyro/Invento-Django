from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Supplier
from .forms import SupplierForm
from django.http import JsonResponse

def suppliers(request):
    if request.method == 'POST':
        form  = SupplierForm(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            pc = Supplier(
                name = cd['name'],
                address =  cd['address'],
                country = cd['country'],
                telephone =  cd['telephone']
            )
            pc.save() 
            messages.success(request, 'Supplier created : ' + cd['name'])
            return redirect('suppliers')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request') 
            suppliers_data = Supplier.objects.order_by('id').all()
            form = SupplierForm()
            return render(request, 'suppliers.html',{'nbar': 'suppliers','suppliers':suppliers_data,'form':form})

    if request.method == 'GET': 
        form = SupplierForm()
        suppliers_data = Supplier.objects.order_by('id').all()
        return render(request, 'suppliers.html',{'nbar': 'suppliers','suppliers':suppliers_data,'form':form})

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