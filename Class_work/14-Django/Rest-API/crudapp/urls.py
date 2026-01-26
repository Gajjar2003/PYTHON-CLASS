from django.urls import path
from crudapp.views import *

urlpatterns = [

    path("view",view_student,name="view"),
    path("add",add_student,name="add"),
    path("viewbyid/<id>",view_byid,name="viewbyid/<id>"),
    path("edit/<id>",edit_student,name="edit/<id>"),
    path("delete/<id>",delete_student,name="delete/<id>")
]

