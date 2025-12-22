from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, 'index.html', {'err': 'Invalid credentials!'})
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {'err': 'User already exists!'})

        User.objects.create_user(
            username=username,
            password=password,
            first_name=fname,
            last_name=lname
        )

        return render(request, "register.html", {'meg': 'Successfully registered!'})

    return render(request, "register.html")

@login_required(login_url='index')
def home(request):
    return render(request, "home.html")

def user_logout(request):
    logout(request)
    return redirect('index')
