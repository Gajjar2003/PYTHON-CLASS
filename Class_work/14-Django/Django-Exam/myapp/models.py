from django.db import models


class employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    salary = models.FloatField()
    dept = models.CharField(max_length=30)
    image = models.ImageField(upload_to="image",default="test.png")