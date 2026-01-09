from django.shortcuts import render,redirect
from django .contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import HttpResponse,JsonResponse

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
    return render(requset,"cart.html",{'carts':carts})

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
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "myaccount.html", {'err': 'Username already exists !!'})

       
        User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname)

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


        




       
 

