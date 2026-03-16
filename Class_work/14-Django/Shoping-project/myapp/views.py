from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def product(request):
    return render(request,"product.html")

def shoping_cart(request):
    return render(request,"shoping-cart.html")


