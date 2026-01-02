from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from eshopapp.models import *


def index(request):
      
      Categorys = Category.objects.all()
      products = product.objects.all()

      return render(request,"index.html",{'Categorys':Categorys,'products':products})

@login_required(login_url="login1")
def about(request):
    return render(request,"about.html")

@login_required(login_url="login1")
def blog_details(request):
    return render(request,"blog-details.html")

@login_required(login_url="login1")
def blog(request):
    return render(request,"blog.html")

@login_required(login_url="login1")
def checkout(request):
    return render(request,"checkout.html")

@login_required(login_url="login1")
def contact(request):
    return render(request,"contact.html")

def main(request):
    return render(request,"main.html")

@login_required(login_url="login1")
def shop_details(request):
    return render(request,"shop-details.html")

@login_required(login_url="login1")
def shop(request):
    return render(request,"shop.html")

@login_required(login_url="login1")
def shopping_cart(request):
    return render(request,"shopping-cart.html")

def login1(requset):
    return render(requset,"login1.html")

def user_register(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get("pass")
      
        u = User(username=name, email=email)
        u.set_password(password)
        u.save()
    
        return render(request, "login1.html", {'meg': 'Successfully done!'})

    

def user_login(request):
        if request.method == 'POST':
            data = request.POST
            name = data.get('name')
            password = data.get("pass")
            u = authenticate(username=name, password=password)

            if u is not None:
                login(request,u)
                return redirect("index")  
            else:
                return render(request, "login1.html", {'err': 'Invalid credentials!'})


def user_logout(requset):
    logout(requset)
    return redirect("index") 

def wishlist(requset):
        return render(requset,"wishlist.html")

def add(requset):
     return render(requset,"add.html")


  

 


       
