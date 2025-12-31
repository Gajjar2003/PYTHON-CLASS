from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name ="register"),
    path("display",display,name="display"),
    path("delete",delete,name="delete"),
    path("edit",edit,name="edit"),
    path("user-login",user_login,name="user-login"),
    path("home",home,name="home"),
    path("user-logout",user_logout,name="user-logout    ")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)