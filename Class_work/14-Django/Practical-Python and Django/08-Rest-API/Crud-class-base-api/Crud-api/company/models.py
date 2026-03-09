from django.db import models

class Dept(models.Model):
    name = models.CharField(max_length=50)
    hod = models.CharField(max_length=50)

class Emp(models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    age = models.IntegerField()
