from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("login",login_user,name="login"),
    path("home",home,name="home")
   
]