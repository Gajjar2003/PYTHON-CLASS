from django.urls import path
from myapp.views import * 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",user_register,name="user-register"),
    path("user-login",user_login,name="user-login"),
    path("user-add",user_add,name="user-add"),
    path("user-display",user_display,name="user-display"),
    path("user-delete",user_delete,name="user-delete"),
    path("user-edit",user_edit,name="user-edit"),
    path('user-logout',user_logout,name="user-logout")

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)