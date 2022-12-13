from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Supplier
from .forms import SupplierForm
# Create your views here.

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

