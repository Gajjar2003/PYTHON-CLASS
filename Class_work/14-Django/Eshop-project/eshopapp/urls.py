from django.urls import path
from eshopapp.views import * 


urlpatterns = [

    path("", index ,name="index"),
    path("about", about,name="about"),
    path("blog-details",blog_details, name="blog-details"),
    path("blog", blog,name="blog"),
    path("checkout",checkout,name="checkout"),
    path("contact",contact,name="contact"),
    path("main",main,name="main"),
    path("shop-details",shop_details,name="shop-details"),
    path("shop",shop,name="shop"),
    path("shopping-cart",shopping_cart,name="shopping-cart")



]