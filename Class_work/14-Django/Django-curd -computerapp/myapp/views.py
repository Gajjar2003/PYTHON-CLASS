from django.shortcuts import render,redirect
from myapp.models import *


def index(requset):
    return render(requset,"index.html")

def register(requset):
    id = requset.POST.get('id')
    name = requset.POST.get('name')
    email = requset.POST.get('email')
    type = requset.POST.get('type')
    model = requset.POST.get('model')
    years = requset.POST.get('years')
    qty = requset.POST.get('qty')
    price = requset.POST.get('price')
    gst = requset.POST.get('gst')
    online = requset.POST.get('online')
    rating = requset.POST.get('rating')
    
    if not id:

        computer.objects.create(name=name,email=email,type=type,model=model,years=years,qty=qty,price=price,gst=gst,online=online,rating=rating)
        return render(requset, "index.html",{'success':'successfull Done !'})
    
    else:
        c = computer.objects.get(id=id)
        c.name = name
        c.email = email
        c.type = type
        c.model = model
        c.years = years
        c.qty = qty
        c.price = price
        c.gst = gst
        c.online = online
        c.rating = rating
        return render(requset, "index.html",{'success':'successfull update Done !'})

def display(requset):

    computers = computer.objects.all()

    return render(requset,"display.html",{'computers':computers})

def delete(requset):
    id  = requset.GET.get('id')
    c = computer.objects.get(id=id)
    c.delete()
    return redirect("display")

def edit(requset):
    id  = requset.GET.get('id')
    c = computer.objects.get(id=id)
    return render(requset,"index.html",{'c':c})