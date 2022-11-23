from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class role(models.Model):
    role = models.CharField(max_length=50)
  
class user_role(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    role = models.ForeignKey(role, on_delete=models.DO_NOTHING)
  