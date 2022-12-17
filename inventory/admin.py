from django.contrib import admin
from .models import Product as product, Invoice as invoice, InvoiceProduct as invoice_product, ImportInvoice as import_invoice, ImportProduct as import_product

class Product(admin.ModelAdmin):
    list_display = ('id','name','avg_price','available_qty','pending_qty','status')

class Invoice(admin.ModelAdmin):
    list_display = ('id','date','customer','products_count','total','delivery_status','payment_status')

class InvoiceProduct(admin.ModelAdmin):
    list_display = ('id','invoice','product','unit_price','weight','total')

class ImportInvoice(admin.ModelAdmin):
    list_display = ('id','date','supplier','products_count','total','load_status','payment_status','invoice_image')

class ImportProduct(admin.ModelAdmin):
    list_display = ('id','invoice','product','unit_price','weight','total')    
    
admin.site.register(product,Product) 
admin.site.register(invoice,Invoice) 
admin.site.register(invoice_product,InvoiceProduct)
admin.site.register(import_invoice,ImportInvoice) 
admin.site.register(import_product,ImportProduct) 