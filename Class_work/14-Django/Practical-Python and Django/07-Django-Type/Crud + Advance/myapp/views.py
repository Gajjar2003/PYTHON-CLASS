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
    dept = requset.POST.get('dept')
    salary = requset.POST.get('salary')
    gender = requset.POST.get('gender')
    language = requset.POST.get('language')
    phone = requset.POST.get('phone')
    city = requset.POST.get('city')
    pincode = requset.POST.get('pincode')
    address = requset.POST.get('address')
    image = requset.FILES.get('image')
    if not id:

        Employee.objects.create(name=name,email=email,age=age,dept=dept,salary=salary,gender=gender,language=language,phone=phone,city=city,pincode=pincode,address=address,image=image)
        return render(requset,"index.html",{'meg':'Employee Resgister successfully done !'})
    else:
        e = Employee.objects.get(pk=id)
        e.name=name
        e.email =email
        e.age = age
        e.dept = dept
        e.salary =salary
        e.language = language
        e.phone = phone
        e.city = city
        e.pincode = pincode
        e.address  = address
        if image:
            e.image = image
        e.save()
        return render(requset,"index.html",{'meg':'Employee Updated successfully done !'})



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
    return render(requset,"index.html",{'e' : e})


