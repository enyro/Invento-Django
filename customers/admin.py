from django.contrib import admin
from .models import  Customer as customer, CustomerLog as customerLog

class Customer(admin.ModelAdmin):
    list_display = ('id','name','address','telephone')

class CustomerLog(admin.ModelAdmin):
    list_display = ('id','customer','task','user','date')

admin.site.register(customer,Customer)
admin.site.register(customerLog,CustomerLog)
