from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    
    def __str__(self):

        return self.name
    
class User(AbstractUser):
    firstname = models.CharField(max_length=50)   
    lasrname = models.CharField(max_length=50) 
    username = models.CharField(max_length=50) 
    email = models.EmailField()
    password = models.CharField(max_length=50)
