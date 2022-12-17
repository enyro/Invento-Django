from django.urls import path

from . import views

urlpatterns = [
    path('customers',views.customers,name='customers'),

    path('api/v1/customers',views.getCustomers,name='customers-api'),  
    path('api/v1/create-customer',views.createCustomer,name='create-customer-api'),  
]