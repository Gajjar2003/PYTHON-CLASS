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
    
    path("register",register,name="register"),
    path("user-login",user_login,name="user-login"),
    path("user-logout",user_logout,name="user-logout"),

    path("getcategory",getcategory,name="getcategory"),
    path("getproduct",getproduct,name="getproduct"),
    path("addtocart",addtocart,name="addtocart"),
    path("removeitems",removeitems,name="removeitems"),
    path("changeqty",changeqty,name="changeqty"),

    path("payment",payment,name="payment"),
    path("makeorder",makeorder,name="makeorder"),
    path('checkout', checkout, name='checkout'),

    path("addcontact",addcontact,name="addcontact"),
    path("diaplay",diaplay,name="diaplay")
]