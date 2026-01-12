from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.IntegerField()
    phone = models.IntegerField()
    dept = models.CharField(max_length=30)
    image = models.ImageField(upload_to="image" ,default="employee.PNG")
