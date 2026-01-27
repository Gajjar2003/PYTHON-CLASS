from django.db import models

# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=30)
    hod  = models.CharField(max_length=30)

class Employee(models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.IntegerField()
