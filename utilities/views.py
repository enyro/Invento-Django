from django.shortcuts import render
from .models import Utility
from django.http import JsonResponse

def utilities(request):
    return render(request,'utilities.html',{'nbar':'utilities'})

def utilitiesData(request):
    utilitiesData = Utility.objects.all().values('id','name','account_number','connected_date','disconnected_date','status')
    return JsonResponse({'id':200 , 'data':list(utilitiesData)})

def createUtility(request):
    if request.user.is_authenticated and request.user.userrole.role.role != 'Store Keeper':  
        pc = Utility(
                name = request.POST['name'],
                account_number =  request.POST['accountNumber'],
                connected_date =  request.POST['date'] 
            )
        pc.save() 
        return JsonResponse({'id': 200, 'data':"Utility connection created successfully!"})