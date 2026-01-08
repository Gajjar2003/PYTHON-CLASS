from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")

def register(request):
    id = request.POST.get('id')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    username = request.POST.get('username')
    password = request.POST.get('password')
    image = request.FILES.get('image')
           
    if not id:
      
            student.objects.create(fname=fname, lname=lname, username=username, password=password, image=image)
            return render(request, "index.html", {'meg': 'Successfully Done'})
    else:
                s = student.objects.get(pk=id)
                s.fname = fname
                s.lname = lname
                s.username = username
                s.password = password
                if image:
                    s.image = image
                s.save()
                return render(request, "index.html", {'meg': 'Successfully Data update Done'})

   
def display(request):
    students = student.objects.all()
    return render(request, "display.html", {'students': students})

def delete(request):
    id = request.GET.get('id')
    s = student.objects.get(pk=id)
    s.delete()
    return redirect("display")

def edit(request):
    id = request.GET.get('id')
    s = student.objects.get(pk=id)
    return render(request, "index.html", {'s': s})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate( username=username, password=password)
        if user is None:
            return render(request, "login.html", {'err': 'Invalid credentials!'})
        else:
            login(request,user)
            return redirect('home')
        
    return render(request, "login.html")

@login_required(login_url="user-login")
def home(request):
    return render(request, "home.html")

def user_logout(request):
    logout(request)
    return redirect('user-login')

def view1(request):
    return render(request, "view.html")

def view2(request):
    return render(request, "view2.html")

def profile(request):
    return render(request, "profile.html")

def dashboard_home(request):
    return render(request, 'dashboard_home.html')
