from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qty = models.IntegerField()
