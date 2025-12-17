from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(requset):
    products = product.objects.all()
    categorys = Category.objects.all()
    if requset.method == 'POST':
        cat = requset.POST['cat']
        name = requset.POST['name']
        price = requset.POST['price']
        qty = requset.POST['qty']
        image = requset.FILES['image']
        category = Category.objects.get(pk=cat) 
        product.objects.create(name=name,price=price,qty=qty,image=image,category=category)
        return render(requset,"index.html",{'products':products,'categorys':categorys})
    else:
       
        return render(requset,"index.html",{'products':products,'categorys':categorys})
    

def delete(requset):
    id = requset.GET['id']
    p = product.objects.get(id=id)
    p.delete()
    return redirect("index")

def edit(requset):
    products = product.objects.all()
    categorys = Category.objects.all()
    if requset.method == 'POST':
        cat = requset.POST['cat']
        id = requset.POST['id']
        name = requset.POST['name']
        price = requset.POST['price']
        qty = requset.POST['qty']
       
        p = product.objects.get(pk=id)
        p.name=name
        p.price=price
        p.qty=qty
        p.category = Category.objects.get(pk=cat)
        if requset.FILES:
            p.image=requset.FILES['image']
        p.save()
        return render(requset,"index.html",{'products':products,'categorys':categorys})
    else:

        id = requset.GET['id']
        p = product.objects.get(id=id)
        return render(requset,"index.html",{'p':p,'products':products,'categorys':categorys})
    

