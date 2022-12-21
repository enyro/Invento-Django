from django.shortcuts import render
from .models import Ledger,Account
from django.http import JsonResponse

def ledgers(request):
    return render(request,"ledgers.html",{"nbar":"ledgers"})

def accounts(request):
    ledgers = Ledger.objects.all()
    return render(request,"accounts.html",{"nbar":"accounts","ledgers":ledgers})

def getLedgers(request):
    ledgers = Ledger.objects.all().values('id','name')
    return JsonResponse({'id':200,'data':list(ledgers)})

def createLedger(request):
    ledger = Ledger(
        name=request.POST['name']
    )
    ledger.save()
    return JsonResponse({'id':200,'data':'Ledger created successfully!'})

def getAccounts(request):
    ledgerId = request.GET['ledger']
    records = request.GET['records']
    ledger = Ledger.objects.get(pk=ledgerId)
    accounts = Account.objects.all().values('id','date','description','ledger_debit__name','ledger_credit__name','amount','status')
    debit = accounts.filter(ledger_debit=ledger)
    credit = accounts.filter(ledger_credit=ledger) 
        
    return JsonResponse({'id':200,'data':{'debit':list(debit),'credit':list(credit)}})

def createAccount(request):
    debit = Ledger.objects.get(pk=request.POST['debit'])
    credit = Ledger.objects.get(pk=request.POST['credit'])
    account = Account(
        date=request.POST['date'],
        description=request.POST['description'],
        ledger_debit=debit,
        ledger_credit=credit,
        amount=request.POST['amount'],
        status=0,
    )
    account.save()
    return JsonResponse({'id':200,'data':'Record created successfully!!'})