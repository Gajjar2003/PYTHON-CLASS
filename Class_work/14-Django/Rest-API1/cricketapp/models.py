from django.db import models


class CricketDept(models.Model):
    name = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)

class Cricketdetalis(models.Model):
    dept = models.ForeignKey(CricketDept,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    run = models.IntegerField()
    four = models.IntegerField()
    six = models.IntegerField()
