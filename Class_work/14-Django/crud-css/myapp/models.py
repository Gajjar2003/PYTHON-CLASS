from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")
