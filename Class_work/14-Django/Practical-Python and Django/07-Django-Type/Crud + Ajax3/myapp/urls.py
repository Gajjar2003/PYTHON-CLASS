from django.urls import path
from myapp.views import *



urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("view",view,name="view"),
    path("delete",delete,name="delete"),
    path("getbyid",getbyid,name="getbyid"),
    path("update/", update, name="update")
]