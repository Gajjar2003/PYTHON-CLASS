from django.urls import path
from crudapp.views import *

urlpatterns = [

    path("", index ,name="index"),
    path("register/", register_student , name='register'),
    path("display/",display,name="display"),
    path("delete",delete ,name="delete"),
    path("edit",edit ,name="edit")

]