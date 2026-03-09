from rest_framework.urls import path
from myapp.views import *

urlpatterns = [
    path("subject/",Subjectapi.as_view()),
    path("subject/<id>",Subjectidapi.as_view()),

    path("subject/student/<id>",viewstudent,name="viewstudent"),
    path("studentview",studentview,name="studentview")
]