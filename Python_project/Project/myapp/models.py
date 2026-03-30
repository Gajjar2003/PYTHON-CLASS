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
    qty = models.IntegerField(default=1)
    price = models.FloatField()
    image = models.ImageField(upload_to="image",default="test.jpg")

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField()
    
    def total_price(self):
        return self.qty * self.product.price 


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date= models.DateField()
    total = models.FloatField()
    status = models.CharField(max_length=50,default="Padding")
    paytype = models.CharField(max_length=50,default="Online")
    payid = models.CharField(max_length=50)


class Orderdetails(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()

    def total_price(self):
        return self.qty*self.price
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=100)


    
