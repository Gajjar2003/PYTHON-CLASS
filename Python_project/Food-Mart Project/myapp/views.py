from django.shortcuts import render,redirect
from django .contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import HttpResponse,JsonResponse
import razorpay
import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(requset):

    # products = Product.objects.all()
    # categorys = Category.objects.all()

    return render(requset,"index.html")

def get_products(requset):

    catid = requset.GET['catid']
    if int(catid) > 0:
        products = Product.objects.filter(category_id =catid)
        return JsonResponse({'products':list(products.values())})
    else:
        products = Product.objects.all()
        return JsonResponse({'products':list(products.values())})
    
def searchproduct(requset):
    q = requset.GET['q']
    products = Product.objects.filter(name__startswith=q)
    return JsonResponse({'products':list(products.values())})

def get_categorys(requset):
    categorys = Category.objects.all()
    return JsonResponse({'categorys':list(categorys.values())})

login_required(login_url="myaccount")
def about(requset):
    return render(requset,"about.html")

login_required(login_url="myaccount")
def cart(requset):
    carts = Cart.objects.filter(user=requset.user)

    sum = 0
    for c in carts:
        sum+=c.total_price()

    return render(requset, 'cart.html',{"carts":carts,"total":int(sum)})

def addtocart(requset):
    pid = requset.GET['pid']
    product = Product.objects.get(pk=pid)
    user =requset.user
    if user.is_anonymous:
            return HttpResponse(user)
    else:
            isexist = Cart.objects.filter(user=user,product=product)
            if(len(isexist)>=1):
                isexist[0].qty =  isexist[0].qty+1
                isexist[0].save()  
                return HttpResponse("Products add into cart !!") 
            else:
                Cart.objects.create(product=product , user = user,qty =1)
                return HttpResponse("Products add into cart !!")

def contact(requset):
    return render(requset,"contact.html")

def myaccount(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email =request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "myaccount.html", {'err': 'Username already exists !!'})

       
        User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)

        return render(request, "myaccount.html", {'meg': 'Successfully registered!' })

    return render(request, "myaccount.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, "myaccount.html", {'err': 'Invalid username or password !!'})

        login(request, user)
        return redirect('index')   

    return render(request, "myaccount.html")

def user_logout(requset):
    logout(requset)
    return redirect('index')


def removecard(requset):
    cid = requset.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("Remove for Card")

def changeqty(requset):
    cid = requset.GET['cid']
    qty =requset.GET['qty']
    cart = Cart.objects.get(pk=cid)
    if int(qty) <= 0 :
        cart.delete()
    else:
        cart.qty=qty
        cart.save()
    return HttpResponse("Cart updated")


def payment(request):

    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_TMSVcZfJN8BbMO", "mADVC3C0iMVlurCrzpi90o7g"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 
    
    return JsonResponse(payment)

def makeorder(request):
    payid = request.GET['payid']
    date = datetime.datetime.now()
    user = request.user

    carts = Cart.objects.filter(user=user)
    total = 0

    for i in carts:
        total += i.total_price()

    order = Order.objects.create(
        user=user,
        payid=payid,
        date=date,
        total=total
    )

    rows = ""
    count = 1

    for c in carts:
        OredrDetails.objects.create(
            order=order,
            product=c.product,
            qty=c.qty,
            price=c.product.price
        )

        rows += f"""
        <tr>
            <td>{count}</td>
            <td>{c.product.name}</td>
            <td>₹{c.product.price}</td>
            <td>{c.qty}</td>
            <td>₹{c.total_price()}</td>
        </tr>
        """
        c.delete()
        count += 1

 
    table = f"""
    <table border="1" style="border-collapse:collapse;">
        <thead>
            <tr>
                <th>ID</th>
                <th>Product</th>
                <th>Price</th>
                <th>Qty</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """

    try:
        send_mail(
            "Order Confirmation",
            "Your Order Placed Successfully",
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=table
        )
    except Exception as e:
        print(e)

    return HttpResponse("Order Placed Successfully Done!")


@login_required(login_url="myaccount")
def checkout(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "checkout.html", {'orders': orders})


@login_required
def address(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        phone = request.POST.get('phone')
        house = request.POST.get('house')
        area = request.POST.get('area')
        city = request.POST.get('city')
        land = request.POST.get('land')
        code = request.POST.get('code')

      
        Address.objects.create(user=request.user,fname=fname,phone=phone,house=house,area=area,city=city,land=land,code=code)

        
        subject = "Food Mart - Address Added Successfully 🏠"
        message = f"""
Hello {request.user.username},

Your delivery address has been added successfully.

Name: {fname}
Mobile: {phone}
Address: {house}, {area}, {city}
Landmark: {land}
Pincode: {code}

Thank you for shopping with Food Mart 
"""
        recipient = [request.user.email]

      
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient,
            fail_silently=False,
        )

        return redirect('index')

    return render(request, "address.html")

def forgotpass(requset):
    return render(requset,"forgot.html")

def sendmail_password(requset):
    email = requset.POST['email']
    try : 
        user =  User.objects.get(email=email)
        send_mail("Password Recovery", f"http://127.0.0.1:8000/passwordset?email={email}", settings.EMAIL_HOST_USER, [email]) 
        return render(requset,"forgot.html",{"err":"Mail sent successfully"})
    except Exception as e:
        return render(requset,"forgot.html",{"err":"Something went wrong"})
    

def passwordset(request):
    email = request.GET.get('email')  

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            return redirect('myaccount')
        except User.DoesNotExist:
            return render(request, "passwordset.html", {
                "error": "User with this email does not exist",
                "email": email
            })

    return render(request, "passwordset.html", {"email": email})


       
 

