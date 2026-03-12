from django.db import models

class Doctors(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
         return self.name
