from django.urls import path
from carapp.views import *

urlpatterns = [

    path("", index ,name="index")

]