from django.contrib import admin
from .models import Supplier as supplier

class Supplier(admin.ModelAdmin):
    list_display = ('id','name','address','country','telephone')

admin.site.register(supplier,Supplier)
