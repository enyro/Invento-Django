from django.db import models
from django.contrib.auth.models import User
 
class Role(models.Model):
    role = models.CharField(max_length=50)
  
class UserRole(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
  