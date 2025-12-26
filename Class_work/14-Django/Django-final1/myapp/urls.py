from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("home",home,name="home"),
    path("logout",user_logout,name="logout"),
    path("delete",delete,name="delete"),
    path("edit",edit,name="edit"),
]