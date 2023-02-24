from django.db import models

# Create your models here.

class Ware(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    img = models.CharField(max_length=300)
    