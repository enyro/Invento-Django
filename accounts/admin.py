from django.contrib import admin
from .models import Ledger as ledger, Account as account, TrialBalance as trialBalance, TrialBalanceLedger as trialBalanceLedger, AccountLog as accountLog

class Ledger(admin.ModelAdmin):
    list_display = ('id','name')

class Account(admin.ModelAdmin):
    list_display = ('id','date','description','ledger_debit','ledger_credit','amount','status')

class TrialBalance(admin.ModelAdmin):
    list_display = ('id','date','total')

class TrialBalanceLedger(admin.ModelAdmin):
    list_display = ('id','trial_balance','ledger','total')

class AccountLog(admin.ModelAdmin):
    list_display = ('id','account','task','user')

admin.site.register(ledger,Ledger)
admin.site.register(account,Account)
admin.site.register(trialBalance,TrialBalance)
admin.site.register(trialBalanceLedger,TrialBalanceLedger)
admin.site.register(accountLog,AccountLog)