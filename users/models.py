from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
 
class Role(models.Model):
    role = models.CharField(max_length=50)
  
class UserRole(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='created_by') 
    created_at = models.DateTimeField(default=timezone.now)

class UserLog(models.Model):
    user_updated = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='user_updated')
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    date = models.DateTimeField(default=timezone.now) 