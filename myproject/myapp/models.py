from django.db import models


# Create your models here.
class Teacher(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    dep=models.CharField(max_length=100)


