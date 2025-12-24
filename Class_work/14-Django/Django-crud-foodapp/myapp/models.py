from django.db import models

class food(models.Model):
    name = models.CharField(max_length=30)
    veg = models.CharField(max_length=30)
    qty = models.IntegerField()
    price = models.FloatField()
    gst = models.FloatField()
    rating = models.CharField(max_length=30)
    image = models.ImageField(upload_to="image", default="jenil.png")
