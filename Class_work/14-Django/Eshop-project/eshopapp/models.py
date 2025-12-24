from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="cat_image")

class product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price= models.FloatField()
    qty = models.IntegerField()
    decs = models.TextField()
    image = models.ImageField(upload_to="cat_image")



