from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField(help_text="Years of experience")
    availability = models.CharField(max_length=100)
    consultation_fee = models.IntegerField()

    def __str__(self):
        return self.name