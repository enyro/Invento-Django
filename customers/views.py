from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm
# Create your views here.

def customers(request):
    if request.method == 'POST':
        form  = CustomerForm(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            pc = Customer(
                name = cd['name'],
                address =  cd['address'],
                telephone =  cd['telephone']
            )
            pc.save() 
            messages.success(request, 'Customer created : ' + cd['name'])
            return redirect('customers')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request') 
            customers_data = Customer.objects.order_by('id').all()
            form = CustomerForm()
            return render(request, 'customers.html',{'nbar':'customers','customers':customers_data,'form':form})

    if request.method == 'GET':
        customers_data = Customer.objects.order_by('id').all()
        form = CustomerForm()
        return render(request, 'customers.html',{'nbar':'customers','customers':customers_data,'form':form})
