from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    salary = models.IntegerField()
    date = models.DateField()
    