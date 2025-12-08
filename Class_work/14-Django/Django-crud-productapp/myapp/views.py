from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(requset):
    return render(requset,"index.html")

def register(requset):
    id = requset.GET.get('id')
    name = requset.POST.get('name')
    model = requset.POST.get('model')
    qty = requset.POST.get('qty')
    price = requset.POST.get('price')
    gst = requset.POST.get('gst')
    online =requset.POST.get('online')

    if not id:

        product.objects.create(name=name,model=model,qty=qty,price=price,gst=gst,online=online)
        return render(requset,"index.html",{'success':'successfully done !'})

    else:
         p = product.objects.get(id=id)
         p.name = name
         p.model = model
         p.qty = qty
         p.price = price
         p.gst = gst
         p.online = online
         p.save()

         return render(requset,"index.html",{'success':'successfully update done !'})


def display(request):

    products = product.objects.all()

    return render(request,"display.html",{'products': products})


def delete(requset):
    id = requset.GET.get("id")
    p = product.objects.get(id=id)
    p.delete()
    return redirect("display")

def edit(requset):
    id = requset.GET.get("id")
    p = product.objects.get(id=id)
    return render(requset,"index.html",{'p':p})
