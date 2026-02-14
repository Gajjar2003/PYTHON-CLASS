from django.urls import path,include
from myapp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users",Userviewset)
router.register("categorys",Categoryviewset)
router.register("product",Productviewset)

urlpatterns = [
    path("",include(router.urls))
]