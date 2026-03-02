from django.db import models

class Student(models.Model):
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    marks = models.CharField(max_length=50)

