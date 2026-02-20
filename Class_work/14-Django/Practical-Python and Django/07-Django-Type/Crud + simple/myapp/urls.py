from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete,name="delete"),
    path("edit",edit,name="edit")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)