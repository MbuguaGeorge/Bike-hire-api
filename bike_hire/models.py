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
    initials = models.CharField(null=True,max_length=3,blank=True)
    
    def __str__(self):
        return self.firstname

    def save(self,*args,**kwargs):
        first = self.firstname
        last = self.lastname
        name = first + ' ' + last
        initials = name.split()
        new = ''
        new_i = ''
        for namec in initials:
            new = first[0][0].upper()
            new_i = last[0][0].upper()
            initial = new + new_i
            self.initials = initial
        super().save(*args,**kwargs)