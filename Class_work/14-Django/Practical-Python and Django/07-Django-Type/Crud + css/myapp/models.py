from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.CharField(max_length=50)
    salary = models.IntegerField()
    address = models.TextField()