from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from eshopapp.models import *
from django.http import HttpResponse,JsonResponse

def index(request):
    # categorys = Category.objects.all()   

    # if request.GET.get('cid'):
    #     cid = request.GET.get('cid')
    #     products = Product.objects.filter(category_id=cid)
    # else:
    #     products = Product.objects.all()

    return render(request, 'index.html')



def get_products(request):
    catid = request.GET.get('catid')

    if int(catid) > 0:
        products = Product.objects.filter(category_id=catid).values()
    else:
        products = Product.objects.all().values()

    return JsonResponse({"products": list(products)})


def get_categorys(request):
    categorys = Category.objects.all().values()
    return JsonResponse({"categorys": list(categorys)})






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
    carts = Cart.objects.filter(user=request.user)
    return render(request,"shopping-cart.html",{'carts':carts})

def addtocard(requset):
    pid = requset.GET['pid']
    product = Product.objects.get(pk=pid)
    user = requset.user

    isexist = Cart.objects.filter(user=user,product=product)
   
    if user.is_anonymous:
            return HttpResponse(user)
    else:
            isexist = Cart.objects.filter(user=user,product=product)
            if(len(isexist)>=1):
                isexist[0].qty = isexist[0].qty+1
                isexist[0].save()
                return HttpResponse("Product added into cart")
            else:
                Cart.objects.create(product=product,user=user,qty=1)
                return HttpResponse("Product added into cart")
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





  

 


       
