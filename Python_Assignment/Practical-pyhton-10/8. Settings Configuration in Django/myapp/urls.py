from django.urls import path
from myapp.views import *



urlpatterns = [
    path('doctors/', DoctorListAPI.as_view()),
]
