from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    description = models.TextField()
    is_vegan = models.BooleanField()