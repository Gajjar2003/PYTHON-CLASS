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
            return render(request, "index.html", {'err': 'Invalid username or password!' })
        else:
            login(request, user)
            return redirect("home")

    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
    

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                'err': "Username already exists!"
            })
        else:
            user = User.objects.create(first_name=fname,last_name=lname,username=username)
            user.set_password(password)
            user.save()

            return render(request, "register.html", {'meg': "Successfully registered!"})

    return render(request, "register.html")

@login_required(login_url="index")
def home(request):
    users = User.objects.all()
    return render(request, "home.html",{'users':users})

def user_logout(request):
    logout(request)
    return redirect("index")

def delete(requset):
    id = requset.GET.get('id')
    u = User.objects.get(pk=id)
    u.delete()
    return redirect("home")

@login_required
def edit(request):
    u = request.user

    if request.method == 'POST':
        u.first_name = request.POST.get('fname')
        u.last_name = request.POST.get('lname')
        u.username = request.POST.get('username')

        password = request.POST.get('password')
        if password:
            u.set_password(password)
        u.save()
        return redirect("index") 

    return render(request, "register.html", {'u': u})