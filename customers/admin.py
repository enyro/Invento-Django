from django.contrib import admin
from .models import  Customer as customer

class Customer(admin.ModelAdmin):
    list_display = ('id','name','address','telephone')

admin.site.register(customer,Customer)
