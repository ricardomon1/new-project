from pyexpat import model
from turtle import title
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    title= models.CharField(max_length=128)
    url = models.URLField()
    views= models.IntegerField(default=0)

    def ___str___(self):
        return self.title