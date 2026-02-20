from django.shortcuts import render,redirect
from myapp.models import *

def index(requset):
    return render(requset,"index.html")


def register(requset):
    id = requset.POST.get('id')
    name = requset.POST.get('name')
    email  = requset.POST.get('email')
    age = requset.POST.get('age')
    salary = requset.POST.get('salary')
    dept = requset.POST.get('dept')
    address = requset.POST.get('address')

    if not id:
        Employee.objects.create(name=name,email=email,age=age,salary=salary,dept=dept,address=address)
        return render(requset,"index.html",{'meg':'Employee successfully done !'})
    else:
        e = Employee.objects.get(pk=id)
        e.name=name
        e.email =email
        e.age=age
        e.salary=salary
        e.dept=dept
        e.address=address
        e.save()
        return render(requset,"index.html",{'meg':'Employee  Update successfully done !'})


def display(requset):
    employee = Employee.objects.all()
    return render(requset,"display.html",{'employee':employee})

def delete(requset):
    id = requset.GET.get('id')
    e = Employee.objects.get(pk=id)
    e.delete()
    return redirect('display')

def edit(requset):
    id = requset.GET.get('id')
    e = Employee.objects.get(pk=id)
    return render(requset,"index.html",{'e':e})