from django.db import models

class product(models.Model):
    name = models.CharField(max_length=30)
    model   =  models.CharField(max_length=30)
    qty = models.IntegerField()
    price = models.FloatField()
    gst = models.FloatField()
    online = models.CharField(max_length=30)
