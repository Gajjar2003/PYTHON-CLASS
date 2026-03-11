from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    specialization = models.CharField(max_length=50)
    years = models.FloatField()