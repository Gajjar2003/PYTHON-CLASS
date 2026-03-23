from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
import razorpay
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


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
    orders =Order.objects.filter(user=request.user)
    return render(request,"check-out.html",{"orders":orders})



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
  
    payid = request.GET.get('payid')
    user = request.user

    carts = Cart.objects.filter(user=user)
   
    total = 0
    for i in carts:
        total += i.total_price()

    order = Order.objects.create( user=user,date=datetime.datetime.now(),total=total,payid=payid)
    rows = ""
    count = 0
    for c in carts:
        Orderdetalis.objects.create(order=order,product=c.product,qty=c.qty,price=c.product.price )
        rows +=f"<tr><td>{count}</td><td>{c.product.name}</td><td>{c.product.price}</td><td>{c.qty}</td><td>{c.total_price()}</td></tr>"
        count+=1


    carts.delete()
    table = f"Pay-ID: {order.payid} |Type: {order.paytype} | Status:{order.status}</span></div>| Date:</strong> {order.date}| Total:</strong> ₹{order.total}<table border='1px'<tr><th>ID</th><th>Product</th><th>Qty</th><th>Price</th><th>Total</th> </tr></thead><tbody>{rows} </tbody> </table>"

    try:
        send_mail("Order Confimations", "You Order placed successfully done !!", settings.EMAIL_HOST_USER, [user.email],html_message=table)
          
    except Exception as e:
            print(e)


    return HttpResponse("Order successfully done !!")

def address(request):
    if request.method == 'POST':
        user = request.user

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address_line = request.POST.get('address')
        app = request.POST.get('app')
        city = request.POST.get('city')
        country = request.POST.get('country')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')

        Address.objects.create(user=user,fname=fname,lname=lname,address=address_line, app=app,city=city,country=country,pincode=pincode,phone=phone)

        try:
            subject = "Order Confirmation"
            from_email = settings.EMAIL_HOST_USER
            to = [user.email]


            text_content = f"""
            Your order has been placed successfully!

            Name: {fname} {lname}
            Phone: {phone}
            Address: {address_line}, {city}, {country} - {pincode}
            """

            html_content = f"""
            <h2>Order Confirmation</h2>

            <p>Your order has been placed successfully! 🎉</p>

            <h3>Customer Details:</h3>
            <ul>
                <li><b>Name:</b> {fname} {lname}</li>
                <li><b>Email:</b> {user.email}</li>
                <li><b>Phone:</b> {phone}</li>
                <li><b>Address:</b> {address_line},
                  <li><b>City:</b> {city}, 
                    <li><b>Country:</b> {country} - {pincode}</li>
            </ul>

            <br>
            <p>Thank you for shopping with us ❤️</p>
            """

          
            email = EmailMultiAlternatives(subject, text_content, from_email, to)
            email.attach_alternative(html_content, "text/html")
            email.send()
        except Exception as e:
            print("Email Error:", e)
        return render(request, "check-out.html")
    return render(request, "check-out.html")

def forgotpass(request):
    return render(request,"forgot.html")





        