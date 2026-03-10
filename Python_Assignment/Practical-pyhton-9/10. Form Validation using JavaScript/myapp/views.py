from django.shortcuts import render,redirect
from myapp.models import * 
from django.shortcuts import render, redirect
from .models import UserRegistration


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        UserRegistration.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password
        )

        return redirect('success')

    return render(request, 'index.html')


def success(request):
    return render(request, "success.html")