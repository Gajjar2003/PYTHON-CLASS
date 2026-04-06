from django.db import models

class Moblie(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
