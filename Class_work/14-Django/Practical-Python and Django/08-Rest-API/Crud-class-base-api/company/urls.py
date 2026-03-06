from rest_framework.urls import path
from company.views import *

urlpatterns = [
    path("dept",Deptapi.as_view()),
    path("dept/<id>",Deptbyid.as_view()),

    path("emp/dept/<id>",addemp,name="addemp"),
    path("emps",emps,name="emps"),
    path("delete/<id>",delete,name= "delete")
]