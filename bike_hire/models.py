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
    contact = models.IntegerField(unique=True,null=True)
    hourly = models.FloatField(null=True)
    daily = models.FloatField(null=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.firstname