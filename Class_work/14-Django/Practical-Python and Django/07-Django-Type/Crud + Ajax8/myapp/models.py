from django.db import models

class Employes(models.Model):
    name = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    salary = models.FloatField()
    age = models.IntegerField()
