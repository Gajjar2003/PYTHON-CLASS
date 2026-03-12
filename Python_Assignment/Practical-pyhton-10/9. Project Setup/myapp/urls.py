from django.urls import path
from myapp.views import *

urlpatterns = [
    path('doctors/',doctor_list),
      path('add/', add),
]