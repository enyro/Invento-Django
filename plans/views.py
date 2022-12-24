from django.shortcuts import render
from .models import Plan
from django.http import JsonResponse
def plans(request):
    return render(request,'plans.html',{'nbar':'plans'})

def plansData(request):
    plans = Plan.objects.all().values('id','name','description','created_date','target_date','status')
    return JsonResponse({'id':200,'data':list(plans)})

def createPlan(request):
    name = request.POST['name']
    description = request.POST['description']
    target_date = request.POST['target']

    plan = Plan(
        name=name,
        description=description,
        target_date=target_date
    )
    plan.save()
    return JsonResponse({'id':200,'data':"Plan created successfully!!"})

def updatePlan(request):
    id = request.POST['id']
    status = request.POST['status']

    plan = Plan.objects.get(pk=id)
    plan.status = status
    plan.save()
    
    return JsonResponse({'id':200,'data':'Plan updated successfully!!'})