from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse



@login_required(login_url="user-login")
def index(request):
    return render(request,"index.html")


@login_required(login_url="user-login")
def product(request):
    return render(request,"product.html")


@login_required(login_url="user-login")
def category(request):
    return render(request,"category.html",)




@login_required(login_url="user-login")
def contact(request):
    return render(request,"contact.html")




@login_required(login_url="user-login")
def check_out(request):
    return render(request,"check-out.html")


@login_required(login_url="user-login")
def shopping_cart(request):
    return render(request,"shopping-cart.html")


@login_required(login_url="user-login")
def about(request):
    return render(request,"about.html")


@login_required(login_url="user-login")
def blog(request):
    return render(request,"blog.html")

def register(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request,"user-register.html",{'err':'User already exists ??'})
        else:
        
            u = User.objects.create(first_name=name,email=email,username=username)
            u.set_password(password)
            u.save()

    return render(request,"user-register.html",{'meg':'User successfully done !!'})

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        u = authenticate(username=username,password=password)
        if u is None:
            return render(request,"user-login.html",{'err':'Invalid Username and Password ??'})
        else:
            login(request,u)
            return redirect('index')

    return render(request,"user-login.html")

def user_logout(request):
    logout(request)
    return redirect('user-login')  


def getcategory(request):
    category = Category.objects.all()
    return JsonResponse({'category':list(category.values())})

def getproduct(request):
    catid = request.GET.get('catid')
    if catid  and catid.isdigit() and int(catid) > 0:
        products = Product.objects.filter(category_id=catid)
        return JsonResponse({'products':list(products.values())})
    else:
        products = Product.objects.all()
        return JsonResponse({'products':list(products.values())})