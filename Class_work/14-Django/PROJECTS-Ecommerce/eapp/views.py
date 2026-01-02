from django.shortcuts import render

# Create your views here.
def  index(requset):
    return render(requset,"index.html")

def about(requset):
    return render(requset,"about.html")

def contact(requset):
    return render(requset,"contact.html")

def products(requset):
    return render(requset,"products.html")

def single_product(requset):
    return render(requset,"single-product.html")