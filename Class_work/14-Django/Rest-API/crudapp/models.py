from django.db import models

# Create your models here.s

class student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    age = models.IntegerField()