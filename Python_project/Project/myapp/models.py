from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image",default="test.jpg")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    qty = models.IntegerField(default=1)
    price = models.FloatField()
    image = models.ImageField(upload_to="image",default="test.jpg")

    def __str__(self):
        return self.name