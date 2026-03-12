from django.urls import path
from myapp.views import *

urlpatterns =[
   path("view/",doctorapi.as_view()),
   path("getbyid/<id>",doctoridapi.as_view())
]