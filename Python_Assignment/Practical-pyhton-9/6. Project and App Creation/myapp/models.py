from django.db import models

# Create your models here.
class Decotor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    hospital = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name