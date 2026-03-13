from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_appointment, name='book'),
    path('payment/', views.payment, name='payment'),
    path('success/', views.success, name='success'),
]