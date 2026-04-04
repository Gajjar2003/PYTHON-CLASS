from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("displayitems",displayitems,name="displayitems"),
    path("deleteitems",deleteitems,name="deleteitems"),
    path("edititems",edititems,name="edititems"),
    path("update",update,name="update")
]