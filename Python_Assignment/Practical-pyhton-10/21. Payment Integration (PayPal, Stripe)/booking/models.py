from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name