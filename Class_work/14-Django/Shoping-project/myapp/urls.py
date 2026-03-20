from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("category",category,name="category"),
    path("check-out",check_out,name="check-out"),
    path("contact",contact,name="contact"),
    
    path("shopping-cart",shopping_cart,name="shopping-cart"),
    path("about",about,name="about"),
    path("blog",blog,name="blog"),
    path("register",register,name="register"),
    path("user-login",user_login,name="user-login"),
    path("user-login",user_logout,name="user-logout"),
    path("getcategory",getcategory,name="getcategory"),
    path("getproduct",getproduct,name="getproduct"),
    path("addtocart",addtocart,name="addtocart"),
    path("remove",remove,name="remove"),
    path("changeqty",changeqty,name="changeqty"),
    path("addcontact",addcontact,name="addcontact"),
    path("displaycontact",displaycontact,name="displaycontact"),
      path("payment",payment,name="payment"),
      path("makeorder",makeorder,name="makeorder")
   
]