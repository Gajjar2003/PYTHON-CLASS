from django.shortcuts import render,redirect
from myapp.models import *

def index(requset):
    return render(requset,"index.html")

def register(requset):
    id = requset.POST.get('id')
    name = requset.POST.get('name')
    veg = requset.POST.get('veg')
    qty =requset.POST.get('qty')
    price =requset.POST.get('price')
    gst = requset.POST.get('gst')
    rating = requset.POST.get('rating')

    if not id :
        food.objects.create(name=name,veg=veg,qty=qty,price=price,gst=gst,rating=rating)
        return render(requset,"index.html",{'success': 'successfully done !'})
    else:
        f = food.objects.get(id=id)
        f.name = name
        f.veg = veg
        f.qty = qty
        f.price =price
        f.gst = gst
        f.rating = rating
        f.save()
        return render(requset,"index.html",{'success': 'successfully update done !'})



def display(requset):

    foods = food.objects.all()

    return render(requset,"display.html",{'foods': foods})


def delete(requset):
    id = requset.GET.get("id")
    f = food.objects.get(id=id)
    f.delete()
    return redirect("display")

def edit(requset):
    id = requset.GET.get("id")
    f = food.objects.get(id=id)
    return render(requset,"index.html",{'f':f})
