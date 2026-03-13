import stripe
from django.conf import settings
from django.shortcuts import render,redirect
from .forms import AppointmentForm
from .models import Appointment

stripe.api_key = settings.STRIPE_SECRET_KEY


def book_appointment(request):

    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save()

            request.session['appointment_id'] = appointment.id

            return redirect('payment')

    return render(request,'booking.html',{'form':form})


def payment(request):

    return render(request,'payment.html',{
        'stripe_public_key':settings.STRIPE_PUBLIC_KEY
    })


def success(request):

    appointment_id = request.session.get('appointment_id')

    appointment = Appointment.objects.get(id=appointment_id)

    appointment.payment_status = True
    appointment.save()

    return render(request,'success.html')