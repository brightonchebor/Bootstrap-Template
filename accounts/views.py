from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from myapp.models import UploadedImage
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if password  == confirm_password :
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    last_name=last_name,
                    first_name=first_name,
                    email = email
                )
                user.save()
                messages.success(request, 'Your profile has been set up! Explore your dashboard.')
                return redirect('accounts:login')
            except:
                messages.error(request, 'It seems you already have an account. Try logging in')
                
        else:
            messages.error(request, 'Password mismatch. Ensure both fields are identical')
            return redirect('accounts:register')
            
    return render(request, 'accounts/register.html', context={})

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(
                request,
                'You are now logged in'
            )
        else:
            messages.error(
                request,
                'Invalid login credentials'
            )    
    return render(request, 'accounts/login.html', context={})

def superuser_required(user): 
    return user.is_superuser 


@user_passes_test(superuser_required)
def upload_image(request):
    if request.method == 'POST':
        title = request.POST['title']
        uploaded_file = request.FILES['image']

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        image = UploadedImage.objects.create(title=title, image=filename)
        image.save()

        return render(request, 'accounts/upload_success.html', {'file_url':file_url})
    return render(request, 'accounts/upload_image.html')
        