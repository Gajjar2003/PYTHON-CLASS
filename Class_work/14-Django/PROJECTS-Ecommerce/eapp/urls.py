from django.urls import path
from eapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("products",products,name="products"),
    path("single-product",single_product,name="single-product")
]