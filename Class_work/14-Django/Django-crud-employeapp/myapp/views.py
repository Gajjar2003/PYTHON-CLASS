from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def regitser(requset):

    name = requset.POST.get('name')
    email = requset.POST.get('email')
    age = requset.POST.get('age')
    salary = requset.POST.get('salary')
    department = requset.POST.get('department')

    employee.objects.create(name = name,email = email, age = age,salary = salary,department = department)

    return render(requset,"index.html",{'success' : 'successfully Done !'})

def display(requset):

    employees = employee.objects.all()
    return render(requset,"display.html",{'employees' : employees})