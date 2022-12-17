from django.urls import path

from . import views

urlpatterns = [
    path('create-invoice', views.create_invoice, name='create_invoice'),
    path('invoice/<int:id>', views.invoice_details, name='invoice_details'),
    path('invoices', views.invoices, name='invoices'),
    path('products', views.products, name='products'),
    path('imports', views.imports, name='imports'),
    path('pending-imports', views.pending_imports, name='pending_imports'),
    path('import-products', views.import_products, name='import_products'),
    path('add-import-invoice', views.add_import_invoice, name='add_import_invoice'),
    

    path('api/v1/insert-invoice', views.insert_invoice, name='insert_invoice'),
    path('api/v1/invoice_data', views.invoice_data, name='invoice_data'),
    path('api/v1/import_invoice_data',views.import_invoice_data,name='import_invoice_data'),
    path('api/v1/import_invoice_products_data',views.import_invoice_products_data,name='import_invoice_products_data'),
    path('api/v1/insert-import-invoice',views.insert_import_invoice,name='insert_import_invoice'),
    path('api/v1/update-invoice-delivery',views.update_invoice_delivery,name='update_invoice_delivery'),
    path('api/v1/products', views.products_data, name='products_data'),
    path('api/v1/create-product',views.insert_product, name='insert_product')
]