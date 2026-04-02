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