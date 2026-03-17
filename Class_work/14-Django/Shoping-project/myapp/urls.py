from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("category",category,name="category"),
    path("check-out",check_out,name="check-out"),
    path("contact",contact,name="contact"),
    path("product",product,name="product"),
    path("shopping-cart",shopping_cart,name="shopping-cart"),
    path("about",about,name="about"),
    path("blog",blog,name="blog")
]