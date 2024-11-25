from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactUs
from django.contrib.auth.decorators import login_required

import requests
import json
from myapp.credentials import LipanaMpesaPpassword, MpesaAccessToken

from django.http import HttpResponse
# Create your views here.
def home(request):

    return render(request, 'home.html', context={})


def about(request):

    return render(request, 'about.html', context={})

def news(request):

    return render(request, 'news.html', context={})

def portfolio(request):

    return render(request, 'portfolio.html', context={})

@login_required(login_url='accounts:login')
def contact(request):
    if request.method == 'POST':
        message = ContactUs(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message'],
            phone = request.POST['phone'],
            date = request.POST['date']

        )
        message.save()
        
        return redirect('home')
    else:
        return render(request, 'contact.html', context={})

def message_detail(request):
    messages = ContactUs.objects.all()
    context={'messages':messages}
    
    return render(request, 'message_detail.html', context )

def message_delete(request, id):
    message = ContactUs.objects.get(id=id)    
    message.delete()

    return redirect('messages')


def update_message(request, id):

    message = get_object_or_404(ContactUs, id=id)

    if request.method == 'POST':
        
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.phone = request.POST.get('phone')
        message.date = request.POST.get('date')
        message.message = request.POST.get('message')

        message.save()

        return redirect("messages")

    return render(request, "message_update.html", context={'message' : message})


# Adding the mpesa functions

#Display the payment form
def pay(request):
   """ Renders the form to pay """
   return render(request, 'pay.html')


# Generate the ID of the transaction
def token(request):
    """ Generates the ID of the transaction """
    consumer_key = 'qvQFfRUmIIMKcLutXyGEdAbkKtYN7RzIjVKiMz8Ma94qQt4q'
    consumer_secret = 'HRSVAAGk1AEG4ZATjzWmqYSTpGluFG6Erf8gRab85NEepozIGSmTPmR6k2Cu9Ivr'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})


# Send the stk push
def stk(request):
    """ Sends the stk push prompt """
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")