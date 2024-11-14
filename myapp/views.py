from django.shortcuts import render, redirect
from .models import ContactUs

# Create your views here.
def home(request):

    return render(request, 'home.html', context={})


def about(request):

    return render(request, 'about.html', context={})

def news(request):

    return render(request, 'news.html', context={})

def portfolio(request):

    return render(request, 'portfolio.html', context={})

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