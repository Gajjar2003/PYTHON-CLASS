from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def register(requset):
    id  = requset.POST.get('id')
    fname = requset.POST.get('fname')
    lname = requset.POST.get('lname')
    username = requset.POST.get('username')
    password = requset.POST.get('password')
    image = requset.FILES.get('image')




    if not id:

        student.objects.create(fname=fname,lname=lname,username=username,password=password,image=image)
        return render(requset,"index.html",{'meg':'Successfully Done'})
    
    else:
        s = student.objects.get(pk=id)
        s.fname = fname
        s.lname = lname
        s.username = username
        s.password = password
        if image:
            s.image = image
        s.save()

        return render(requset,"index.html",{'meg':'Successfully Data update Done'})


def display(requset):
    students = student.objects.all()
    return render(requset,"display.html",{'students':students})


def delete(requset):
    id = requset.GET.get('id')
    s = student.objects.get(pk=id)
    s.delete()
    return redirect("display")

def edit(requset):
    id = requset.GET.get('id')
    s = student.objects.get(pk=id)
    return render(requset,"index.html",{'s':s})


def user_login(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']

        user=authenticate(requset,username=username,password=password)

        if user is None:
             return render(requset,"login.html",{'err':'Invalid username and password !!'})
        else:
            login(requset,user)
            return redirect("home")



    return render(requset,"login.html")


@login_required(login_url="user-login")
def home(requset):
    return render(requset,"home.html")


def user_logout(request):
    logout(request)
    return redirect('login')
  

