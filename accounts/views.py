from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password  == password_confirm:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                user.save()
                message = messages.success(request, 'Account created successfully')
                return redirect('home')
            except:
                message = messages.error(request, 'User already exists')
                return redirect('register')
        else:
            message = messages.error(request, 'Passwords did not match')
            return redirect('register')

    return render(request, 'accounts/register.html', context={})

