from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(requset):
    products = product.objects.all()
    if requset.method == 'POST':
    
        name = requset.POST['name']
        price = requset.POST['price']
        qty = requset.POST['qty']
        product.objects.create(name=name,price=price,qty=qty)
        return render(requset,"index.html",{'products':products})
    else:
       
        return render(requset,"index.html",{'products':products})
    

def delete(requset):
    id = requset.GET['id']
    p = product.objects.get(id=id)
    p.delete()
    return redirect("index")

def edit(requset):
    products = product.objects.all()
    if requset.method == 'POST':
        id = requset.POST['id']
        name = requset.POST['name']
        price = requset.POST['price']
        qty = requset.POST['qty']
        p = product.objects.get(id=id)
        p.name=name
        p.price=price
        p.qty=qty
        p.save()
        return render(requset,"index.html",{'products':products})
    else:

        id = requset.GET['id']
        p = product.objects.get(id=id)
        return render(requset,"index.html",{'p':p,'products':products})