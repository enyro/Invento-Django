from django.urls import path

from . import views

urlpatterns = [
    path('ledgers',views.ledgers,name='ledgers'),
    path('accounts',views.accounts,name='accounts'), 

    path('api/v1/ledgers',views.getLedgers,name='ledgers-api'),  
    path('api/v1/create-ledger',views.createLedger,name='create-ledgers-api'),  
    path('api/v1/accounts',views.getAccounts,name='accounts-api'), 
    path('api/v1/create-account',views.createAccount,name='create-account-api'),  
]