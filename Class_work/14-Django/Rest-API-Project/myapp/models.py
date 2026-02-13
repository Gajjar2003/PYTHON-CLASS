from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="image",null=True)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product",null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=260)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="Item")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    total = models.IntegerField()
    status = models.CharField(max_length=50,default="pending")
    payment = models.CharField(max_length=50,default="online")
    created_at = models.DateTimeField(auto_now_add=True) 

class OredrItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="orderitem")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()

    def sub_total(self):
        return self.qty * self.price

    def __str__(self):
        return f"{self.product.name} - {self.qty}"