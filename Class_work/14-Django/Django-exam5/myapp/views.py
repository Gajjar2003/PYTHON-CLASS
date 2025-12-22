from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Login view
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {'err': 'Invalid username or password!'})
        else:
            login(request, user)
            return redirect("home")

    return render(request, "index.html")



def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {'err': 'Username already exists!'})
        else:
            user = User.objects.create(first_name=fname,last_name=lname,username=username)
            user.set_password(password)
            user.save()

            return render(request, "register.html", {'msg': 'Successfully registered!'})

    return render(request, "register.html")



@login_required(login_url='index')
def home(request):
    return render(request, "home.html")



def user_logout(request):
    logout(request)
    return redirect("index")
