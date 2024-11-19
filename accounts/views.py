from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password ']

        if password  == confirm_password :
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    lastname=lastname,
                    firstname=firstname
                )
                user.save()
                message = messages.success(request, 'Account created successfully')
                return redirect('home')
            except:
                message = messages.error(request, 'User already exists')
                
        else:
            message = messages.error(request, 'Passwords did not match')
            
    return render(request, 'accounts/register.html', context={})

