from django.urls import path
from eshopapp.views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("blog-details", blog_details, name="blog-details"),
    path("blog", blog, name="blog"),
    path("checkout", checkout, name="checkout"),
    path("contact", contact, name="contact"),
    path("main", main, name="main"),
    path("shop-details", shop_details, name="shop-details"),
    
    path("shopping-cart", shopping_cart, name="shopping-cart"),
    path("login1",login1,name="login1"),
    path("user-register",user_register,name="user-register"),
    path("user-login",user_login,name="user-login"),
    path("user-logout",user_logout,name="user-logout"),
    path("wishlist",wishlist,name="wishlist"),
   

    path('getproducts', get_products, name='getproducts'),
    path('getcategories',get_categorys, name='getcategories'),
    path("addtocard",addtocard,name="addtocard"),
    path("removecart",removecart,name="removecart"),
    path("changeqty", changeqty, name="changeqty"),
    path("payment",payment,name="payment"),
    path("makeorder",makeorder,name="makeorder"),
    path("placeorder",placeorder,name="placeorder"),

    path("forgotpass",forgotpass,name="forgotpass"),
    path("passwordsend-mail",passwordsend_mail,name="passwordsend-mail"),
  

   
    
     


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)