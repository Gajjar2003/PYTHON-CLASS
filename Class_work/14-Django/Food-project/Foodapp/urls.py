from django.urls import path
from Foodapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("blog/", blog, name="blog"),
    path("testimonial/", testimonial, name="testimonial"),
]
