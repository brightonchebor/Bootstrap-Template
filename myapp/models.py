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
    
class Transaction(models.Model):
  
    transaction_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_time = models.DateTimeField()
    status = models.CharField(max_length=50, default="Pending")
    description = models.TextField(null=True, blank=True)
    mpesa_receipt_number = models.CharField(max_length=100, null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    customer_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.phone_number} - {self.status}"
    
    
