from django.urls import path
from .views import list_repos, create_repo

urlpatterns = [
    path('repos/', list_repos),
    path('create/', create_repo),
]