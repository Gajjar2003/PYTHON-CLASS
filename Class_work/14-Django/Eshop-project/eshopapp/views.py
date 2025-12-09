from django.shortcuts import render

def index(requset):
    return render(requset,"index.html")

def about(requset):
    return render(requset,"about.html")

def blog_details(requset):
    return render(requset,"blog-details.html")

def blog(requset):
    return render(requset,"blog.html")

def checkout(requset):
    return render(requset,"checkout.html")

def contact(requset):
    return render(requset,"contact.html")

def main(requset):
    return render(requset,"main.html")

def shop_details(requset):
    return render(requset,"shop-details.html")

def shop(requset):
    return render(requset,"shop.html")

def shopping_cart(requset):
    return render(requset,"shopping-cart.html")
