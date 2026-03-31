from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import HttpResponse,JsonResponse
import razorpay,datetime
from django.core.mail import send_mail
from django.conf import settings


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
    orders = Order.objects.filter(user=request.user)

    return render(request,"checkout.html",{'orders':orders})

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
    total = 0

    for c in carts:
        total += c.total_price()

    return render(request, "shop-cart.html", {
        'carts': carts,
        'total': int(total)
    })



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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')   
        else:
            return render(request, 'user-login.html', {'err': 'Invalid Username or Password'})

    return render(request, 'user-login.html')


def user_logout(request):
    logout(request)
    return redirect('index')

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

def changeqty(request):
    cid = request.GET['cid']
    qty = request.GET['qty']
    c = Cart.objects.get(pk=cid)
    if int(qty)<=0:
        c.delete()
    else:
        c.qty = qty
        c.save()
    return HttpResponse("Cart update in Products")


def payment(request):
    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_STS6r0jEAzoi7U", "qd2x98bvF2IOQvAKgNv34Qi7"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 
    
    return JsonResponse(payment)

def makeorder(request):
    payid = request.GET['payid']
    date = datetime.datetime.now()
    user = request.user

    carts = Cart.objects.filter(user=user)
    sum = 0
    for i in carts:
        sum+=i.total_price()

    order = Order.objects.create(user=user,date=date,total=sum,payid=payid)

    for c in carts:
        Orderdetails.objects.create(order=order,product=c.product,qty=c.qty,price=c.product.price)
        c.delete()

    return HttpResponse("Oredr placed successfully !!")


def checkout(request):
    orders = Order.objects.all()  

    subtotal = 0
    for od in orders:
        for item in od.items.all():
            subtotal += item.total_price()

    total = subtotal

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        notes = request.POST.get('notes')

      
        message = f"""
==============================
        BILLING DETAILS
==============================
Name: {fname} {lname}
Address: {address}, {city}, {state} - {zip_code}
Phone: {phone}
Email: {email}
Notes: {notes}

==============================
        ORDER DETAILS
==============================
"""

        for od in orders:
            message += f"\nOrder ID: {od.id} | PayID: {od.payid}\n"

            order_total = 0

            for item in od.items.all():
                price = item.total_price()
                order_total += price

                message += f"{item.product.name} - Qty:{item.qty} - ₹{price}\n"

            message += f"Order Total: ₹{order_total}\n"
            message += "--------------------------\n"

        message += f"\nFINAL TOTAL: ₹{total}"

      
        send_mail(subject="Your Order Confirmation",message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[email],)

      
        for od in orders:
            od.items.all().delete()
        orders.delete()
        request.session['order_success'] = "Order placed successfully!"
        return redirect('index')

    # ================= SUCCESS MESSAGE =================
    success_msg = request.session.pop('order_success', None)

    return render(request, 'checkout.html', {
        'orders': orders,
        'subtotal': subtotal,
        'total': total,
        'success_msg': success_msg
    })


def addcontact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        message = request.POST.get('message')

        Contact.objects.create(name=name,email=email,message=message)
    return HttpResponse("Contact add into Website !!")


def diaplay(request):
    con = Contact.objects.all()
    return JsonResponse({'con':list(con.values())})

def forgotpass(request):
    return render(request,"forgotpass.html")

def password_sendmail(request):
    email = request.POST['email']
    try:
        user = User.objects.get(email=email)
        send_mail("Password Recovery",f"http://127.0.0.1:8000/setpassword?email={email}", settings.EMAIL_HOST_USER,[email])
        return render(request,'forgotpass.html',{'meg':'Mail send sucessfully !!'})
    except Exception as e:
        return render(request,'forgotpass.html',{'err':'Something went wrong ???'})
    
def setpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')

        print("EMAIL:", email)
        print("PASSWORD:", password)

        if password != cpassword:
            return render(request, "setpassword.html", {"err": "Passwords do not match","email": email})

        user = User.objects.filter(email=email).first()

        if user:
            user.set_password(password)
            user.save()
            return redirect('user-login')
        else:
            return render(request, "setpassword.html", {"err": "User not found","email": email})

    email = request.GET.get('email')
    return render(request, "setpassword.html", {"email": email})