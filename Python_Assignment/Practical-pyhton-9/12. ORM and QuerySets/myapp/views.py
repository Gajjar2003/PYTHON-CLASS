from django.shortcuts import render,redirect
from myapp.models import *

def index(request):
    return render(request,"index.html")

def register(request):
     if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        specialization = request.POST.get('specialization')
        years = request.POST.get("years")

        if not id :
            Doctor.objects.create(name=name,age=age,email=email,phone=phone,specialization=specialization,years=years)
            return render(request,"index.html",{'meg':'successfully done !!'})
        else:
            d = Doctor.objects.get(pk=id)
            d.name=name
            d.age =age
            d.email =email
            d.phone=phone
            d.specialization =specialization
            d.years = years
            d.save()
            return render(request,"index.html",{'meg':'successfully update  done !!'})


def display(request):
    doctors = Doctor.objects.all()
    return render(request,"display.html",{'doctors':doctors})

def delete(request):
    id = request.GET.get('id')
    d = Doctor.objects.get(pk=id)
    d.delete()
    return redirect('display')
  
def edit(request):
    id = request.GET.get('id')
    d = Doctor.objects.get(pk=id)
    return render(request,"index.html",{'d':d})