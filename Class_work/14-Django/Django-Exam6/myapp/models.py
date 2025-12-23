from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    age  = models.IntegerField()
    image = models.ImageField(upload_to="image",default="jenil.png")