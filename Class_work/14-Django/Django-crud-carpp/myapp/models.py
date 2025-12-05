from django.db import models

# Create your models here.

class car(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    price = models.FloatField()
