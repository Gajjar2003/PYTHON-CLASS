from django.db import models


class student(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

class employee(models.Model):
    e_name = models.CharField(max_length=20)
    e_age = models.PositiveIntegerField()
    e_salary = models.PositiveIntegerField()
    e_email = models.EmailField(unique=True)
