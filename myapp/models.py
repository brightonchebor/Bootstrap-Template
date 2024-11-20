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
    
class UploadedImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploaded_images/')

    def __str__(self):
        return self.title
    
