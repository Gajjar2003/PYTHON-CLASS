from rest_framework .urls import path
from myapp.views import *

urlpatterns = [
    path("view",view,name="view"),
    path("add",add,name="add"),
    path("getbyid/<id>",getbyid,name="getbyid"),
    path("put/<id>",put,name="put"),
    path("delete/<id>",delete,name="delete")
]