from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home.html', context={})

def contact(request):

    return render(request, 'contact.html', context={})

def about(request):

    return render(request, 'about.html', context={})

def news(request):

    return render(request, 'news.html', context={})

def portfolio(request):

    return render(request, 'portfolio.html', context={})
