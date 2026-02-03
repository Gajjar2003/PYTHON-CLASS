from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("cart",cart,name="cart"),
    path("contact",contact,name="contact"),
    path("myaccount",myaccount,name="myaccount"),
    path("user-login",user_login,name="user-login"),
    path("user-logout",user_logout,name="user-logout"),
    path("getproducts",get_products,name="getproducts"),
    path("getcategorys",get_categorys,name="getcategorys"),
    path("searchproduct",searchproduct,name="searchproduct"),
    path("addtocart",addtocart,name="addtocart"),
    path("removecard",removecard,name="removecard"),
    path("changeqty",changeqty,name="changeqty"),
    path("payment",payment,name="payment"),
    path("makeorder",makeorder,name="makeorder"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)