from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
import razorpay
import datetime



@login_required(login_url="user-login")
def index(request):
    return render(request,"index.html")

@login_required(login_url="user-login")
def category(request):
    return render(request,"category.html",)


@login_required(login_url="user-login")
def contact(request):
    # c = Contact.objects.all()
    # if request.method == 'POST':
    #     fname = request.POST.get('fname')
    #     lname = request.POST.get('lname')
    #     email = request.POST.get('email')
    #     subject = request.POST.get('subject')
    #     area = request.POST.get('area')
    #     phone = request.POST.get('phone')

    #     con = Contact.objects.create(fname=fname,lname=lname,email=email,subject=subject,area=area,phone=phone)
    #     con.save()

    #     return render(request, "contact.html", {'meg': 'Message successfully done !!' })

    
    return render(request, "contact.html")

def addcontact(request):
        if request.method == 'POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            area = request.POST.get('area')
            phone = request.POST.get('phone')

            con = Contact.objects.create(fname=fname,lname=lname,email=email,subject=subject,area=area,phone=phone)
            con.save()

            return HttpResponse("Contact Save into website !!")
        
def displaycontact(request):
    co = Contact.objects.all()
    return JsonResponse({'co':list(co.values())})


@login_required(login_url="user-login")
def check_out(request):
    return render(request,"check-out.html")



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
    
def addtocart(request):
    pid = request.GET['pid']
    product=Product.objects.get(pk=pid)
    user = request.user

    if user .is_anonymous:
            return HttpResponse(user)
    else:
        isexist = Cart.objects.filter(user=user,product=product)
        if len(isexist) >= 1:
            isexist[0].qty = isexist[0].qty + 1
            isexist[0].save()  
            return HttpResponse("Product added into cart successfully !!")
                
        else:
                Cart.objects.create(product=product,qty=1,user=user)
                return HttpResponse("Product added into cart successfully !!")
    

@login_required(login_url="user-login")
def shopping_cart(request):
    carts = Cart.objects.filter(user=request.user)
    sum = 0
    for c in carts:
        sum+=c.total_price()
    return render(request,"shopping-cart.html",{'carts':carts,'total':int(sum)})

def remove(request):
    cid  = request.GET['cid']
    c = Cart.objects.get(pk=cid)
    c.delete()
    return HttpResponse("Remove items into cart")

def changeqty(request):
    cid  = request.GET['cid']
    qty = request.GET['qty']
    c = Cart.objects.get(pk=cid)
    if int(qty) <= 0:
        c.delete()
    else:
        c.qty = qty
        c.save()
    return HttpResponse("Cart updatetd in this items")


def payment(request):
    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_STS6r0jEAzoi7U", "qd2x98bvF2IOQvAKgNv34Qi7"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 
    
    return JsonResponse(payment)

def makeorder(request):
    payid = request.GET['payid']
    date  = datetime.datetime.now()
    user = request.user

    carts = Cart.objects.filter(user=user)
    sum = 0
    for i in carts:
        sum+=i.total_price()
        order = Order.objects.create(user=user,date=date,total=sum,payid=payid)

        for c in carts:
                Orderdetalis.objects.create(order=order,product=c.product,qty=c.qty,price =c.product.price)
                c.delete()
    return HttpResponse("Order placed successfully done !!")