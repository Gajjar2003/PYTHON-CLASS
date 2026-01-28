from django.urls import path
from cricketapp.views import *

urlpatterns = [

    path("dp",cricketAPI.as_view()),
    path("dp/<id>",cricketbyid.as_view()),

    path("cri/dp/<id>",addcricket,name="addcricket"),
    path("getcricket",getcricket,name="getcricket")

]