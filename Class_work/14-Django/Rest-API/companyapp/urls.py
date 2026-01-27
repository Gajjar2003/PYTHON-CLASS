from django.urls import path
from companyapp.views import *

urlpatterns = [

    path("depts",DeptAPI.as_view()),
    path("depts/<id>",DeptupdateAPI.as_view()),

    path("emps/dept/<id>",addemp,name="addemp"),
    path("emps",getemps,name="emps"),

]