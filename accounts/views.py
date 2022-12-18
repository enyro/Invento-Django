from django.shortcuts import render
from .models import Ledger
from django.http import JsonResponse

def ledgers(request):
    return render(request,"ledgers.html",{"nbar":"ledgers"})

def getLedgers(request):
    ledgers = Ledger.objects.all().values('id','name')
    return JsonResponse({'id':200,'data':list(ledgers)})

def createLedger(request):
    ledger = Ledger(
        name=request.POST['name']
    )
    ledger.save()
    return JsonResponse({'id':200,'data':'Ledger created successfully!'})