from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="cat_image")

    
    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="pro_image")

