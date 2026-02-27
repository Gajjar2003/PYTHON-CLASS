from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("add",add,name="add"),
    path("display",display,name="display")
]