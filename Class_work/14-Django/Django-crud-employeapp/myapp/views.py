from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def regitser(requset):
    id = requset.POST.get("id")
    name = requset.POST.get('name')
    email = requset.POST.get('email')
    age = requset.POST.get('age')
    salary = requset.POST.get('salary')
    department = requset.POST.get('department')
    image = requset.FILES.get('image')

    if not id:
        employee.objects.create(name = name,email = email, age = age,salary = salary,department = department,image=image)

        return render(requset,"index.html",{'success' : 'successfully Done !'})
    else:
         e = employee.objects.get(id=id)
         e.name = name
         e.email = email
         e.age = age
         e.salary = salary
         e.department = department
         if image:
            e.image = image
         e.save()
         return render(requset,"index.html",{'success' : 'successfully update Done !'})


def display(requset):

    employees = employee.objects.all()
    return render(requset,"display.html",{'employees' : employees})

def delete(requset):
    id = requset.GET.get("id")
    e = employee.objects.get(id=id)
    e.delete()
    return redirect("display")

def edit(requset):
    id = requset.GET.get("id")
    e = employee.objects.get(id=id)
    return render(requset,"index.html",{'e':e})