from django.shortcuts import render
from .models import Cheque
from customers.models import Customer
from django.http import JsonResponse

def cheques(request):
    customers = Customer.objects.all()
    return render(request,'cheques.html',{'nbar':'cheques','customers':customers})

def chequesData(request):
    cheques = Cheque.objects.all().values('id','cheque_number','date','customer__name','bank','account_number','amount','image','status')
    return JsonResponse({'id':200,'data':list(cheques)})

def insertCheque(request):
    number = request.POST['number']
    date = request.POST['date']
    customerId = request.POST['customer']
    bank = request.POST['bank']
    account = request.POST['account']
    amount = request.POST['amount']
    image = request.FILES['image']

    customer = Customer.objects.get(pk=customerId)

    cheque = Cheque(
        cheque_number = number,
        date = date,
        customer = customer,
        bank = bank,
        account_number = account,
        amount = amount,
        image = image
    )
    cheque.save()

    return JsonResponse({'id':200,'data':'Cheque added successfully!!'})

def updateChequeStatus(request):
    id = request.POST['id']
    status = request.POST['status']

    cheque = Cheque.objects.get(pk=id)
    cheque.status = status
    cheque.save()

    return JsonResponse({'id':200,'data':'Cheque updated successfully!!'})