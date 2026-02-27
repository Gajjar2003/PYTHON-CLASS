from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponse,JsonResponse


# Create your views here.
def index(request):
    return render(request,"index.html")

def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        qty = request.POST.get("qty")
        price = request.POST.get('price')

        Product.objects.create(name=name,qty=qty,price=price )

        return HttpResponse("Product added successfully")
    
def display(request):
    p = Product.objects.all()
    return JsonResponse({'p':list(p.values())})