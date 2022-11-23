from django.contrib import admin
from .models import role,user_role
# Register your models here.
class Role(admin.ModelAdmin):
    list_display = ('id','role')

class UserRole(admin.ModelAdmin):
    list_display = ('user','role')
    
admin.site.register(role,Role) 
admin.site.register(user_role,UserRole) 