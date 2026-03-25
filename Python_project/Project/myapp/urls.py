from django.urls import path
from myapp.views import *

urlpatterns =[
    path("",index,name="index"),
    path("blog-details",blog_details,name="blog-details"),
    path("blog",blog,name="blog"),
    path("checkout",checkout,name="checkout"),
    path("contact",contact,name="contact"),
    path("shop",shop,name="shop"),
    path("shop-cart",shop_cart,name="shop-cart"),
    path("product-details",product_details,name="product-details")
]