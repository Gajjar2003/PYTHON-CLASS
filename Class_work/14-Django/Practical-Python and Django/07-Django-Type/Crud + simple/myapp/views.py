from django.shortcuts import render,redirect
from myapp .models import *

# Create your views here.

def index(requset):
    return render(requset,"index.html")

def register(requset):
    id = requset.POST.get('id')
    name = requset.POST.get('name')
    age = requset.POST.get('age')
    email = requset.POST.get('email')
    image = requset.FILES.get('image')  
    if not id  :
        Student.objects.create(name=name,age=age,email=email,image=image)
        return render(requset,"index.html",{"meg":'successfully done!'})
    else:
        s = Student.objects.get(pk=id)
        s.name =name
        s.age = age
        s.email = email
        if image:
            s.image =image
        s.save()
        return render(requset,"index.html",{"meg":'successfully update done!'})


def display(requset):
    student =Student.objects.all()
    return render(requset,"display.html",{'student':student})

def delete(requset):
    id = requset.GET.get('id')
    s = Student.objects.get(pk=id)
    s.delete()
    return redirect('display')

def edit(requset):
    id = requset.GET.get('id')
    s = Student.objects.get(pk=id)
    return render(requset,"index.html",{'s':s})