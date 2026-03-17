from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def product(request):
    return render(request,"product.html")

def category(request):
    return render(request,"category.html")

def contact(request):
    return render(request,"contact.html")

def check_out(request):
    return render(request,"check-out.html")

def shopping_cart(request):
    return render(request,"shopping-cart.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")