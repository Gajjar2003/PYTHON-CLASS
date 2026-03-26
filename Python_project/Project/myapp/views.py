from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import HttpResponse,JsonResponse


def index(request):
    categorys = Category.objects.all()
    return render(request,"index.html",{'categorys':categorys})

@login_required(login_url="user-login")
def blog_details(request):
    return render(request,"blog-details.html")

@login_required(login_url="user-login")
def blog(request):
    return render(request,"blog.html")

@login_required(login_url="user-login")
def checkout(request):
    return render(request,"checkout.html")

@login_required(login_url="user-login")
def contact(request):
    return  render(request,"contact.html")

@login_required(login_url="user-login")
def shop(request):
    # categorys = Category.objects.all()
    # products = Product.objects.all()
    return render(request,"shop.html")

@login_required(login_url="user-login")
def shop_cart(request):
    return render(request,"shop-cart.html")

@login_required(login_url="user-login")
def product_details(request):
    return render(request,"product-details.html")


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
             return render(request,"register.html",{'err':'User already exists ???'})
        else:
            u = User.objects.create(first_name =fname,last_name = lname,email=email,username=username)
            u.set_password(password)
            u.save()
    return render(request,"register.html",{'meg':'successfully done !!'})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u = authenticate(username=username,password=password)

        if u is None:
            return render(request,"user-login.html",{'err':"Invalid Username and password ???"})
        else:
            login(request,u)
            return redirect('index')
    return render(request,"user-login.html")

@login_required(login_url="user-login")
def user_logout(request):
    logout(request)
    return render(request,"user-login.html")


def getcategory(request):
        categorys = Category.objects.all()
        return JsonResponse({'categorys':list(categorys.values())})

def getproduct(request):
        products = Product.objects.all()
        return JsonResponse({'products':list(products.values())})