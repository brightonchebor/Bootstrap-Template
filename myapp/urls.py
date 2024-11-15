from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('messages/', message_detail, name='messages'),
    path('messages/delete/<int:id>/', message_delete, name='delete')
]
