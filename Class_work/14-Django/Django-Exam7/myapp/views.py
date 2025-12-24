from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']

        u = authenticate(username=username,password=password)
        if u is None:
            return render(requset,"index.html",{'err':'username and password invalid !'})
        else:
            login(requset,u)
            return redirect("home")
             



    return render(requset,"index.html")

def register(requset):
    if requset.method == 'POST':
        fname = requset.POST['fname']
        lname = requset.POST['lname']
        username = requset.POST['username']
        password = requset.POST['password']

        if User.objects.filter(username=username).exists():
            return render(requset,"register.html",{'err':'Username already exists  !'})
        else:
            u = User.objects.create(first_name =fname , last_name = lname, username=username)
            u.set_password(password)
            u.save()
            return render(requset,"register.html",{'meg':'successfully done !'})
    return render(requset,"register.html")
      

@login_required(login_url="index")
def home(requset):
    students = User.objects.all()
    return render(requset,"home.html",{'students': students})

def user_logout(request):
    logout(request)
    return redirect("index")


@login_required(login_url="index")
def delete(requset):
    id = requset.GET.get('id')
    s = User.objects.get(pk=id)
    s.delete()
    return redirect("home")

@login_required(login_url="index") 
def edit(request):
     id = request.GET.get('id') 
     s = User.objects.get(pk=id) 
     
     return render(request, "register.html", {"s": s})


     
    