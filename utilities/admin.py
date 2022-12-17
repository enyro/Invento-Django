from django.contrib import admin
from .models import Utility as utility, UtilityInvoice as utilityInvoice

class Utility(admin.ModelAdmin):
    list_display = ('id','name','account_number','connected_date','disconnected_date','status')

class UtilityInvoice(admin.ModelAdmin):
    list_display = ('id','Utility','invoice_number','date','due_date','amount')

admin.site.register(utility,Utility) 
admin.site.register(utilityInvoice,UtilityInvoice) 