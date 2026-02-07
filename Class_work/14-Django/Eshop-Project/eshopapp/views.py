from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from eshopapp.models import *
from django.http import HttpResponse,JsonResponse
import razorpay
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import random




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

    row = ""
    count = 0
    for c in carts:
        Orderdetils.objects.create(order=order,product= c.product,qty=c.qty,price=c.product.price)
        row+=f"<tr><td>{count}</td><td>{c.product.name}</td><td>{c.product.price}</td><td>{c.qty}</td><td>{c.total_price()}</td></tr>"
        c.delete()
        count+=1

        table = f"  <table border = '1'><thead><tr><th>PayID:{order.payid}</th><th>PayType:{order.pattype}</th><th>Total</th></tr><tr><th>Order-Date:{order.date}</th><th>Status:{order.status}</th><th>Total:{order.total}</th></tr><tr><th>ID</th><th>Name</th><th>Price</th><th>Qty</th><th>Total</th></tr></thead><tbody>{row}</tbody></table>"
           
        try:
            send_mail("Order confimation", "Your order placed successfully done", settings.EMAIL_HOST_USER, [user.email],html_message=table)
        except Exception as e:
            print(e)
    return HttpResponse("Order placed successfully done !")


def placeorder(request):
    if request.method == "POST":
        bill_no = generate_bill_no()

        bill = Bils.objects.create(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            country=request.POST.get('country'),
            address=request.POST.get('address'),
            town=request.POST.get('town'),
            state=request.POST.get('state'),
            code=request.POST.get('code'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
           
        )

     
        subject = f"Your Order Bill - {bill_no}"
        message = f"""
Hello {bill.fname},

Your order has been placed successfully.

Bill No : {bill_no}
Name    : {bill.fname} {bill.lname}
Address : {bill.address}, {bill.town}, {bill.state},{bill.code},
Phone   : {bill.phone},
Email : {bill.email},





Thank you for shopping with us!
"""

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [bill.email],
            fail_silently=False,
        )

        return render(request, "checkout.html", {
            'meg': f'Order placed & Bill sent to Email-Id'
        })

    return render(request, "checkout.html")



def generate_bill_no():
    return f"BILL-{random.randint(100000,999999)}"

def forgotpassword(requset):
    return render(requset,"forgotpassword.html")

def password_sendmail(requset):
    email = requset.POST['email']
    try : 
        user =User.objects.get(email=email)
        send_mail("Password Recovery", f"http://127.0.0.1:8000/setpassword?email={email}", settings.EMAIL_HOST_USER, [email])
        return render(requset,"forgotpassword.html",{'meg':'Successfully send mail !!'})
    except Exception as e:

        return render(requset,"forgotpassword.html",{'err':'something want wrong'})

def setpassword(requset):
    if  requset.method == 'GET':
        email = requset.GET['email']
    if requset.method == 'POST':
        email = requset.POST['email']
        password = requset.POST['password']
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return redirect('login1')
    return render(requset,"setpassword.html",{'email':email})











  

 


       
