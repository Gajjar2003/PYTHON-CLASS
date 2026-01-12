from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path("",index,name="index"),
   path("register",register,name="register"),
   path("home",home,name="home"),
   path("user-logout",user_logout,name="user-logout"),
   path("insert",insert,name="insert"),
   path("display",display,name="display"),
   path("delete",delete,name="delete"),
   path("edit",edit,name="edit"),
   path("show",show,name="show"),
   path("view1",view1 , name="view1"),
 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)