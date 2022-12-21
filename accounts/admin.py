from django.contrib import admin
from .models import Ledger as ledger, Account as account

class Ledger(admin.ModelAdmin):
    list_display = ('id','name')

class Account(admin.ModelAdmin):
    list_display = ('id','date','description','ledger_debit','ledger_credit','amount','status')

admin.site.register(ledger,Ledger)
admin.site.register(account,Account)
