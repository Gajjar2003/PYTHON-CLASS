from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from eshopapp.models import *
from django.http import HttpResponse,JsonResponse
import razorpay
import datetime

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
    orders = Order.objects.filter(user = request.user)
    return render(request,"checkout.html",{'orders':orders})

@login_required(login_url="login1")
def contact(request):
    return render(request,"contact.html")

def main(request):
    return render(request,"main.html")

@login_required(login_url="login1")
def shop_details(request):
    return render(request,"shop-details.html")


@login_required(login_url="login1")
def shopping_cart(request):
    carts = Cart.objects.filter(user=request.user)

    sum = 0
    for c in carts:
        sum+=c.total_price()

    return render(request, 'shopping-cart.html',{"carts":carts,"total":int(sum)})


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
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "login1.html", {'err': 'Username already exists!'})

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return render(request, "login1.html", {'meg': 'Registration successful Done !!'})

    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login1.html", {'err': 'Invalid username or password'})


def user_logout(requset):
    logout(requset)
    return redirect("index") 

def wishlist(requset):
        return render(requset,"wishlist.html")

def removecart(requset):
    cid = requset.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("Cart into delete")


def changeqty(request):
    cid = request.GET.get('cid')
    qty = request.GET.get('qty')
    cart = Cart.objects.get(id=cid)
    if int(qty)<=0:
        cart.delete()
    else:
        cart.qty = qty
        cart.save()

    return HttpResponse("Cart updated")

def payment(request):

    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    
    return JsonResponse(payment)

def makeorder(requset):
    payid = requset.GET['payid']
    date = datetime.datetime.now()
    user = requset.user

    carts = Cart.objects.filter(user=user)
    sum = 0
    for i in carts:
        sum += i.total_price()

    order = Order.objects.create(user=user,date=date,total=sum,payid=payid)

    for c in carts:
        Orderdetils.objects.create(order=order,product= c.product,qty=c.qty,price=c.product.price)
        c.delete()

    return HttpResponse("Order placed successfully done !")








  

 


       
