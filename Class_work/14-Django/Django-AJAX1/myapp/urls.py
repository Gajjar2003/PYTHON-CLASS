from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index.html"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete,name="delete"),
    path("getbyid",getbyid,name="getbyid"),
    path("update",update,name="update"),
    path("search",search,name="search"),
   
   
]