from django.db import models

class Techer(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    phone= models.IntegerField()
    subject = models.CharField(max_length=50)
