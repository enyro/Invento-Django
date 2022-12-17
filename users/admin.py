from django.contrib import admin
from .models import Role as role,UserRole as user_role
 
class Role(admin.ModelAdmin):
    list_display = ('id','role')

class UserRole(admin.ModelAdmin):
    list_display = ('user','role')
    
admin.site.register(role,Role) 
admin.site.register(user_role,UserRole) 