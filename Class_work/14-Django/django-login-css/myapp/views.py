from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(requset):

    return render(requset,"index.html")

def register(requset):
    uname = requset.POST.get('uname')
    email = requset.POST.get('email')
    password = requset.POST.get('pass')
  

    u = User.objects.create(username=uname,email=email)
    u.set_password(password)
    u.save()
    return render(requset,"index.html",{'meg':'successfully done !'})

    
    

def login_user(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(username=uname, password=password)

        if user is None:
            return render(request, "index.html", {'err': 'Invalid credentials!'})
        else:
            login(request, user)
            return redirect("home")

    return render(request, "index.html")

def home(request):
    return render(request, "home.html")


   