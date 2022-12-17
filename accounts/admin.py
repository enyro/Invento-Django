from django.contrib import admin
from .models import Ledger as ledger

class Ledger(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(ledger,Ledger)
