from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=30)


class Country(models.Model):
    name = models.CharField(max_length=30)


class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
