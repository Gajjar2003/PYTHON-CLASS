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
    carts = Cart.objects.filter(user=request.user)
    return render(request,"shop-cart.html",{'carts':carts})




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
        catid = request.GET['catid']
        if int(catid) > 0 :
            products = Product.objects.filter(category_id=catid)
            return JsonResponse({'products':list(products.values())})
        else:
            products = Product.objects.all()
            return JsonResponse({'products':list(products.values())})

def addtocart(request):
    pid = request.GET['pid']
    product = Product.objects.get(pk=pid)
    user = request.user

    if user.is_anonymous:
        return HttpResponse(user)
    else:
        isexist = Cart.objects.filter(user=user,product=product)
        if(len(isexist)>=1):
            isexist[0].qty =  isexist[0].qty+1
            isexist[0].save()
            return HttpResponse("Product into cart successfully done !!!")
        else:
            Cart.objects.create(product=product,user=user,qty=1)
            return HttpResponse("Product into cart successfully done !!!")

def removeitems(request):
    cid = request.GET['cid']
    c = Cart.objects.get(pk=cid)
    c.delete()
    return HttpResponse("Products Deleted into Cart")