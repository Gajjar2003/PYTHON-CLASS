from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def register(requset):
    id = requset.POST.get('id')
    name = requset.POST.get('name')
    email = requset.POST.get('email')
    age = requset.POST.get('age')
    image = requset.FILES.get('image')
    if not id:

        student.objects.create(name=name,email=email,age=age,image=image)

        return render(requset,"index.html",{'meg':'successfully done !'})
    else:
        s = student.objects.get(pk=id)
        s.name=name
        s.email=email
        s.age = age
        if image:
            s.image = image
        s.save()
        return render(requset,"index.html",{'meg':'successfully update done !'})

def display(requset):
    students =student.objects.all()
    return render(requset,"display.html",{'students':students})

def delete(requset):
    id = requset.GET.get('id')
    s = student.objects.get(pk=id)
    s.delete()
    return redirect("display")

def edit(requset):
    id = requset.GET.get('id')
    s = student.objects.get(pk=id)
    return render(requset,"index.html",{'s':s})