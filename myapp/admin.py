from django.contrib import admin
from .models import ContactUs, UploadedImage

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(UploadedImage)

