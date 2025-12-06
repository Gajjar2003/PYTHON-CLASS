from django.shortcuts import render
from myapp.models import *

# Create your views here.

def index(requset):
    return render(requset,"index.html")

def register(requset):
    name = requset.POST.get('name')
    model = requset.POST.get('model')
    qty = requset.POST.get('qty')
    price = requset.POST.get('price')
    gst = requset.POST.get('gst')
    online =requset.POST.get('online')

    product.objects.create(name=name,model=model,qty=qty,price=price,gst=gst,online=online)
    return render(requset,"index.html",{'success':'successfully done !'})


def display(request):

    products = product.objects.all()

    return render(request,"display.html",{'products': products})


