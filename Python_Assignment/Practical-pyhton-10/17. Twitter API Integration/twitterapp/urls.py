from django.urls import path
from .views import latest_tweets

urlpatterns = [
    path('', latest_tweets),
]