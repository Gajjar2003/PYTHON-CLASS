from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):
    name  = models.CharField(max_length=50)
    image = models.ImageField(upload_to="cat_image")

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name  = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to="pro_image")

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField()



    def total_price(self):
        return self.qty * self.product.price
