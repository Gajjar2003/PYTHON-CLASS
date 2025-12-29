from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index.html"),
    path("register",register,name="register"),
    path("display",display,name="display")
]