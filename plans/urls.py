from django.urls import path

from . import views

urlpatterns = [
    path('plans',views.plans,name='plans'),
    
    path('api/v1/plans',views.plansData,name='plans_api'),
    path('api/v1/create-plan',views.createPlan,name='create-plan'),
    path('api/v1/update-plan',views.updatePlan,name='update-plan')
]