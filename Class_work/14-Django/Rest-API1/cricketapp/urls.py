from django.urls import path
from cricketapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("dp",cricketAPI.as_view()),
    path("dp/<id>",cricketbyid.as_view()),

    path("cri/dp/<id>",addcricket,name="addcricket"),
    path("getcricket",getcricket,name="getcricket"),

      path('cricket/<id>', cricketbyid.as_view()),
      path("cri/dp/<id>/<cid>",updatecricket,name="updatecricket"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)