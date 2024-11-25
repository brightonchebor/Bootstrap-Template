from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('messages/', message_detail, name='messages'),
    path('messages/delete/<int:id>/', message_delete, name='delete'),
    path('message/update/<int:id>/', update_message, name='update'),

    path('pay/', pay, name='pay'), # view the payment form
    path('stk/', stk, name='stk'), # send the stk push prompt
    path('token/', token, name='token'), # generate the token for that particular transaction
]
