from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image",default="jenil.jpg")