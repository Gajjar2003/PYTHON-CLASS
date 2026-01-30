from django.db import models

class Coach(models.Model):
    name = models.CharField(max_length=30)
    team = models.CharField(max_length=50)


class CricketDept(models.Model):
    coach = models.ForeignKey(Coach,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)

class Cricketdetalis(models.Model):
    dept = models.ForeignKey(CricketDept,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    run = models.IntegerField()
    four = models.IntegerField()
    six = models.IntegerField()
