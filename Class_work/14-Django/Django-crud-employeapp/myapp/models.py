from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    salary = models.FloatField()
    department = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image",default="jenil.png")
