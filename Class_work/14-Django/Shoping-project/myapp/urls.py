from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("blog",blog,name="blog"),
    path("contact",contact,name="contact"),
    path("product",product,name="product"),
    
    path("shoping-cart",shoping_cart,name="shoping-cart")

   
]