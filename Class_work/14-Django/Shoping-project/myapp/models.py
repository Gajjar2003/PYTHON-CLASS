from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image",default="test.jpg")

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")
    
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
  

    def total_price(self):
        return self.qty*self.product.price


class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    phone = models.IntegerField()




