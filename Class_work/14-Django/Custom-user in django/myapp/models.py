from django.db import models
from myapp.manager import *
from django.contrib.auth.models import AbstractUser



class CustomeUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=20,unique=True)
    bio = models.TextField()

    USERNAME_FIELD = 'phone'
    objects = CustomUserManager()

