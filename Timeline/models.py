from django.db import models

# Create your models here.

class Users(models.Model):

    name = models.CharField(max_length= 30)
    password = models.CharField(max_length= 30)
    email = models.EmailField()

class Events(models.Model):

    name = models.CharField(max_length= 50)
    descript = models.CharField(max_length= 100)
    date = models.DateField()

class Periods(models.Model):

    name = models.CharField(max_length= 50)
    descript = models.CharField(max_length= 100)
    date1 = models.DateField()
    date2 = models.DateField()