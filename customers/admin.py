from django.contrib import admin
from .models import  customer
# Register your models here.
class Customer(admin.ModelAdmin):
    list_display = ('id','name','address','telephone')

admin.site.register(customer,Customer)
