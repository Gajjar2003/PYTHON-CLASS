from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def register(requset):
    name = requset.POST.get('name')
    email = requset.POST.get('email')
    age = requset.POST.get('age')
    dept = requset.POST.get('dept')
    salary = requset.POST.get('salary')
    gender = requset.POST.get('gender')
    language = requset.POST.get('language')
    phone = requset.POST.get('phone')
    city = requset.POST.get('city')
    pincode = requset.POST.get('pincode')
    address = requset.POST.get('address')

    Employee.objects.create(name=name,email=email,age=age,dept=dept,salary=salary,gender=gender,language=language,phone=phone,city=city,pincode=pincode,address=address)

    return render(requset,"index.html",{'meg':'Employee Resgister successfully done !'})

def display(requset):
    employee = Employee.objects.all()
    return render(requset,"display.html",{'employee':employee})

