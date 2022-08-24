from turtle import title
from django.db import models

# Create your models here.

class Measure(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    sauce = models.BooleanField()
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Dish(models.Model):
    title = models.CharField(max_length=100)
    ingredient = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to= 'app/static/images', null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title