from django.urls import path
from .views import location

urlpatterns = [
    path('', location),
]