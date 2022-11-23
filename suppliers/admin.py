from django.contrib import admin
from .models import supplier
# Register your models here.
class Supplier(admin.ModelAdmin):
    list_display = ('id','name','address','country','telephone')

admin.site.register(supplier,Supplier)
