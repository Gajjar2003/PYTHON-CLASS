from django.urls import path
from Foodapp.views import index, about, blog, testimonial

urlpatterns = [
    path('', index, name='index'),
    path('index.html', index, name='index.html'),   
    path('about/', about, name='about.html'),
    path('blog/', blog, name='blog.html'),
    path('testimonial/', testimonial, name='testimonial.html'),
]

