from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django .contrib.auth.decorators import login_required
from myapp.models import *

def index(requset):
    if requset.method == 'POST':
        username = requset.POST['username']
        password = requset.POST['password']

        u = authenticate(username=username,password=password)

        if u is None:
              return render(requset, "index.html", {'err': 'Invalid username and password !'})
        else:
            login(requset,u)
            return redirect('home')
    return render(requset,"index.html")

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {'err': 'Username already exists!'})

        u = User.objects.create_user(first_name=fname,last_name=lname,username=username)
        u.set_password(password)
        u.save()

        return render(request, "register.html", {'msg': 'Successfully registered!'})

    return render(request, "register.html")

def user_logout(request):
    logout(request)
    return redirect("index")  

@login_required(login_url="index")
def home(request):
    return render(request, "home.html")

@login_required(login_url="index")
def insert(requset):
    id  =requset.POST.get('id')
    name = requset.POST.get('name')
    email  = requset.POST.get('email')
    dept = requset.POST.get('dept')
    age = requset.POST.get('age')
    salary = requset.POST.get('salary')
    phone = requset.POST.get('phone')
    image = requset.FILES.get('image')

    if not id:
        employee.objects.create(name = name ,email=email,dept=dept,age=age,salary=salary,phone=phone,image=image)
        return render(requset,"home.html",{'msg':'successfully doen by employee'})
    else:
        e = employee.objects.get(pk=id)
        e.name = name
        e.email = email
        e.age  = age
        e.dept = dept
        e.phone = phone
        e.salary = salary
        if image :
            e.image = image
        e.save() 

        return render(requset,"home.html",{'msg':'successfully update data by employee'})
    
@login_required(login_url="index")
def display(requset):
    employees = employee.objects.all()
    return render(requset,"display.html",{'employees':employees})

@login_required(login_url="index")
def delete(requset):
    id  = requset.GET.get('id')
    e = employee.objects.get(pk=id)
    e.delete()
    return redirect('display')

@login_required(login_url="index")
def edit(requset):
    id  = requset.GET.get('id')
    e = employee.objects.get(pk=id)
    return render(requset,"home.html",{'e':e})

def show(requset):
    return render(requset,"show.html")

def view1(requset):
    return render(requset,"view1.html")
