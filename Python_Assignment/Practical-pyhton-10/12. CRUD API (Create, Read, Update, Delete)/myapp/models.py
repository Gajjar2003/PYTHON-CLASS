from django.db import models


class Jenil(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    age = models.IntegerField()
    
