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

def message_delete(request, id):
    message = ContactUs.objects.get(id=id)    
    message.delete()

    return redirect('messages')

# Update

def update_appointment(request, appointment_id):

    """ Update the appointments """

    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Put the condition for the form to update

    if request.method == 'POST':

        appointment.name = request.POST.get('name'),

        appointment.email = request.POST.get('email'),

        appointment.phone = request.POST.get('phone'),

        appointment.date = request.POST.get('date'),

        appointment.doctor = request.POST.get('doctor'),

        appointment.department = request.POST.get('department'),

        appointment.message = request.POST.get('message'),

        # Once you click on the update button

        appointment.save()

        return redirect("medi_app:show_appointments")

    

    return render(request, "edit_appointment.html")