from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Login
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, "index.html", {'err': 'Invalid credentials!'})
        else:
            login(request, user)  
            return redirect("home")

    return render(request, "index.html")



def reg(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {'err': "Username already exists!"})

        user = User(first_name=fname, last_name=lname, username=username)
        user.set_password(password)
        user.save()

        return render(request, "register.html", {'meg': "Successfully registered!"})

    return render(request, "register.html")


@login_required(login_url="index")
def home(request):
    return render(request, "home.html")

def user_logout(requset):
    logout(requset)
    return render(requset,"index.html")

