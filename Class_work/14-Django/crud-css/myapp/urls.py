from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("",index,name="index"),
    path("delete",delete,name="delete"),
    path("edit",edit,name="edit")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)