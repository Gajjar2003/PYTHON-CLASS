from django.urls import path
from myapp.views import *

urlpatterns = [
    path("get-api",get_api,name="get-api"),
    path("post-api",post_api,name="post-api"),
    path("put-api",put_api,name="put-api"),
    path("delete-api",delete_api,name="delete-api"),
]