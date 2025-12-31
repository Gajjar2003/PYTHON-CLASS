from django.db import models
from django.contrib.auth.models import User



class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")

