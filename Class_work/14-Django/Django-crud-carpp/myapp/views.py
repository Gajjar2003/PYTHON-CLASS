from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(requset):
    return render(requset,"index.html")

def register(requset):
   id = requset.POST.get('id')
   name = requset.POST.get('name')
   model =requset.POST.get('model')
   price = requset.POST.get('price')

   if not id:
    car.objects.create(name=name,model=model,price=price)
    return render(requset,"index.html",{'success':'successfully done'})
   else:
       cr = car.objects.get(id=id)
       cr.name=name
       cr .model=model
       cr.price=price
       cr.save()

       return render(requset,"index.html",{'success':'successfully upadate done'})
      

def display(requset):
    cars = car.objects.all()
    return render(requset,"display.html",{"cars": cars})


def delete(reqsert):
    id = reqsert.GET.get("id")
    cr = car.objects.get(id=id)
    cr.delete()
    return redirect("display")

def edit(requset):
    id  = requset.GET.get("id")
    cr = car.objects.get(id=id)
    return render(requset,"index.html",{'car' : cr})

   

    