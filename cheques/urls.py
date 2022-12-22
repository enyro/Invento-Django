from django.urls import path
from . import views 

urlpatterns = [
    path('cheques',views.cheques,name='cheques'),

    path('api/v1/cheques',views.chequesData,name='cheques_api'),
    path('api/v1/insert-cheque',views.insertCheque,name='insert-cheque'),
    path('api/v1/update-cheque-status',views.updateChequeStatus,name='updateChequeStatus')
]
