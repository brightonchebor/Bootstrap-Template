from django.contrib import admin
from .models import ContactUs, UploadedImage, Transaction

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(UploadedImage)
admin.site.register(Transaction)
