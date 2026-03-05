from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age  = models.IntegerField()
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    subject = models.CharField(max_length=50)
