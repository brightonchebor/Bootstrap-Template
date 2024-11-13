from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    
    def __str__(self):

        return self.name