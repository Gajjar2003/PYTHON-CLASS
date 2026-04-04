from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    name = request.POST.get('name')
    category = request.POST.get('category')
    price = request.POST.get('price')
    qty = request.POST.get('qty')

    Product.objects.create(name=name,category=category,price=price,qty=qty)

    return HttpResponse("Products Add into Tables !!")

def display(request):
    pro = Product.objects.all()
    return JsonResponse({'pro':list(pro.values())})

def delete(request):
    pid = request.GET.get('pid')
    p = Product.objects.get(pk=pid)
    p.delete()
    return HttpResponse("Product Deleted in Table")


def edit(request):
    pid = request.GET.get('pid')
    pro = Product.objects.filter(pk=pid)
    return JsonResponse({'pro':list(pro.values())})

def update(request):
   
        id = request.POST.get('id')
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        qty = request.POST.get('qty')

        p = Product.objects.get(pk=id)
        p.name = name
        p.category = category
        p.price = price
        p.qty = qty
        p.save()

        return HttpResponse("Product Updated Successfully!")
    
