from django.urls import path

from . import views

urlpatterns = [
    path('suppliers',views.suppliers,name='suppliers'),  

    path('api/v1/suppliers',views.getSuppliers,name='suppliers-api'),   
    path('api/v1/create-supplier',views.createSupplier,name='create-supplier-api'),
]