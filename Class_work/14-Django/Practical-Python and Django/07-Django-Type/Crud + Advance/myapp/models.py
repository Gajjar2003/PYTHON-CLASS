from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.CharField(max_length=50)
    salary = models.IntegerField()
    gender = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    pincode  = models.IntegerField()
    address = models.TextField(null=True, blank=True)
    image  = models.ImageField(upload_to="image",default="test.png")
