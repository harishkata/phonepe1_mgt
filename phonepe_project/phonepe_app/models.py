from django.db import models

# Create your models here.

class people(models.Model):
    name = models.CharField(max_length=15)
    salary = models.IntegerField()
    age = models.IntegerField()