from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(requset):   
        if requset.method == 'POST':
            username = requset.POST['username']
            password = requset.POST['password']

            u = authenticate(username=username,password=password)
            if u is None:
                 return render (requset,"index.html",{'err':'invalid username !'})
            else:
                 login(requset,u)
                 return redirect("home")
                 

        return render (requset,"index.html")

def register(requset):
    if requset.method == 'POST':
        fname = requset.POST['fname']
        lname = requset.POST['lname']
        username = requset.POST['username']
        password = requset.POST['password']

        if User.objects.filter(username=username).exists():
            return render(requset,"register.html",{'err':'Username alredy exist !'})
        else:
            u = User.objects.create(first_name=fname,last_name=lname,username=username)
            u.set_password(password)
            u.save()

            return render(requset,"register.html",{'meg':'successfully done !'})
    return render(requset,"register.html")

@login_required(login_url="index")
def home(requset):
     return render(requset,"home.html")

def user_logout(requset):
     return render(requset,"index.html")