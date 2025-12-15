from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        # Create user with password hashing
        user = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        user.save()

        return render(request, "register.html", {'meg': "Successfully registered!"})

    return render(request, "register.html")


def user_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pass')

        user = authenticate(username=name, password=password)

        if user is None:
            return render(request, "index.html", {'err': 'Invalid credentials!'})

        login(request, user)
        return redirect("home")

    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def user_logout(request):
    logout(request)
    return render(request, "index.html")
