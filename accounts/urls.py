from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_view, name='login'),
    
    path('upload/', upload_image, name='upload_image')
]
