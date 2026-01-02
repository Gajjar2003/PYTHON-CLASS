from django.db import models




class student(models.Model):
    
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")

def __str__(self):
        return self.username