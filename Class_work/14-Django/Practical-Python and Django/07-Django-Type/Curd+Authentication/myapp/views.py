from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request,"user-register.html",{'err':'User already exists ??'})
        else:
            u =  User.objects.create(first_name = fname,last_name = lname,username=username)
            u.set_password(password)
            u.save()
            return render(request,"user-register.html",{'meg':'User register successfully done!'})
    
    return render(request,"user-register.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u=authenticate(username=username,password=password)
        if u is None:
            return render(request,"user-login.html",{'err':'Username and password Invalid ???'})
        else:
            login(request,u)
            return redirect('user-add')


    return render(request,"user-login.html")


def user_logout(request):
    logout(request)
    return render(request,"user-login.html")


@login_required(login_url="user-login")
def user_add(request):
        if request.method == 'POST':
            emp_id = request.POST.get('id')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            age = request.POST.get('age')
            salary = request.POST.get('salary')
            dept = request.POST.get('dept')
            phone = request.POST.get('phone')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            image = request.FILES.get('image')

            if not emp_id:
                Employee.objects.create(fname=fname,email=email,age=age,salary=salary,dept=dept,phone=phone,city=city,pincode=pincode,image=image)
                return render(request,"user-add.html",{'meg':'Employee successfully Register !!'})
            else:
                e = Employee.objects.get(pk=emp_id)
                e.fname=fname
                e.email =email
                e.age =age
                e.salary =salary
                e.dept =dept
                e.phone = phone
                e.city =city
                e.pincode = pincode
                if image:
                    e.image = image
                e.save()
                return render(request,"user-add.html",{'meg':'Employee update successfully done !!'})
        return render(request,"user-add.html")

@login_required(login_url="user-login")
def user_display(request):
    employe = Employee.objects.all()
    return render(request,"user-display.html",{'employe':employe})

@login_required(login_url="user-login")
def user_delete(request):
    id = request.GET.get('id')
    e = Employee.objects.get(pk=id)
    e.delete()
    return redirect('user-display')
    
@login_required(login_url="user-login")
def user_edit(request):
    emp_id = request.GET.get('id')
    e = Employee.objects.get(pk=emp_id)
    return render(request, "user-add.html", {'e': e})

