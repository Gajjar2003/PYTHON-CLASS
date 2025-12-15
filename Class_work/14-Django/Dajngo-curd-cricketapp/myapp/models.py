from django.db import models


class cricket(models.Model):
    no = models.IntegerField()
    name =  models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20)
    fromate = models.CharField(max_length=50)
    run = models.IntegerField()
    con = models.IntegerField()
    score = models.IntegerField()
    avg = models.FloatField()
    four = models.IntegerField()
    six = models.IntegerField()




