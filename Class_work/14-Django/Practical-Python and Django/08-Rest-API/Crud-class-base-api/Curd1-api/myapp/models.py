from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()


class Student(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
