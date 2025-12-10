from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog_details(request):
    return render(request,"blog-details.html")

def blog(request):
    return render(request,"blog.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")

def main(request):
    return render(request,"main.html")

def shop_details(request):
    return render(request,"shop-details.html")

def shop(request):
    return render(request,"shop.html")

def shopping_cart(request):
    return render(request,"shopping-cart.html")

def login(requset):
    return render(requset,"login.html")

def user_register(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get("pass")
      
        u = User(username=name, email=email)
        u.set_password(password)
        u.save()
    
        return render(request, "login.html", {'meg': 'Successfully done!'})

    

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
                return render(request, "login.html", {'err': 'Invalid credentials!'})

    

 


       
