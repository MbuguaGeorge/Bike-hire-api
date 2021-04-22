from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(('password'), max_length=128, help_text=("use'[algo]$[salt]$[hexdigest]'"))

class Profile(models.Model):
    firstname = models.CharField(max_length=50, unique=True)
    lastname = models.CharField(max_length=50, unique=True)
    admission = models.CharField(max_length=10,unique=True)
    
