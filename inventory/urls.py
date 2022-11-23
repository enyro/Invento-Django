from django.urls import path

from . import views

urlpatterns = [
    path('products',views.products,name='products'), 
    path('invoices',views.invoices,name='invoices'), 
    path('api/invoice_data',views.invoice_data,name='invoice_data'), 
    path('create-invoice',views.create_invoice,name='create_invoice'), 
    path('invoice/<int:id>',views.invoice_details,name='invoice_details'), 
    path('api/insert-invoice',views.insert_invoice,name='insert_invoice'),
    path('imports',views.imports,name='imports'),
    path('api/import_invoice_data',views.import_invoice_data,name='import_invoice_data'),
    path('import-products',views.import_products,name='import_products'),
    path('api/import_invoice_products_data',views.import_invoice_products_data,name='import_invoice_products_data'),
    path('add-import-invoice',views.add_import_invoice,name='add_import_invoice'), 
    path('api/insert-import-invoice',views.insert_import_invoice,name='insert_import_invoice'),
]