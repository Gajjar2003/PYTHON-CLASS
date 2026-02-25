from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    dept = models.CharField(max_length=50,null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=50,null=True)
    pincode = models.IntegerField(null=True)
    image = models.ImageField(upload_to="image",default='test.png',null=True)
