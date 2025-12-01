from django.urls import path
from Foodapp.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('testimonial/', testimonial, name='testimonial'),
]
