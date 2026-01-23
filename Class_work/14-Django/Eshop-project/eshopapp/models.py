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
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    total = models.FloatField()
    status = models.CharField(max_length=50,default="Pending")
    pattype = models.CharField(max_length=50,default="online")
    payid = models.CharField(max_length=50)


class Orderdetils(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="detalis")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()


class Bils(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    town =  models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)

    
  



def total_price(self):
    return self.price * self.qty
