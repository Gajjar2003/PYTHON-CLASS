from django.db import models

class computer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    years = models.IntegerField()
    qty = models.IntegerField()
    price = models.FloatField()
    gst = models.FloatField()
    online = models.CharField(max_length=30)
    rating = models.CharField(max_length=40)
