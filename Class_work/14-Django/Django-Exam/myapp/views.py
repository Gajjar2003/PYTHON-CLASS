from django.shortcuts import render,redirect
from myapp.models import *


def index(requset):
    return render(requset,"index.html")

def register(requset):
    id  = requset.POST.get('id')
    name = requset.POST.get('name')
    email = requset.POST.get('email')
    age = requset.POST.get('age')
    salary = requset.POST.get('salary')
    dept = requset.POST.get('dept')
    image = requset.FILES.get('image')  

    if not id:

        employee.objects.create(name=name,email=email,age=age,salary=salary,dept=dept,image=image)

        return render(requset,"index.html",{'meg':'successfully Done by data !'})
    else:
       e =  employee.objects.get(pk=id)
       image = requset.FILES.get('image')

       e.name = name
       e.email = email
       e.age = age
       e.salary =salary
       e.dept =dept
       if requset.FILES:

            e.image= requset.FILES['image']
    e.save()                 

    return render(requset,"index.html",{'meg':'successfully upadte Done by data !'})

def display(requset):
    employes = employee.objects.all()
    return render(requset,"display.html",{'employes':employes})

def delete(requset):

    id = requset.GET.get('id')
    e = employee.objects.get(pk=id)
    e.delete()
    
    return redirect("display")

def edit(requset):
    id = requset.GET.get('id')
    e = employee.objects.get(pk=id)

    return render(requset,"index.html",{'e':e})