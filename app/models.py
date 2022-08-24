from turtle import title
from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image as Im

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


class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')

    def image_tag(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))

    def save(self): # new
        super().save()
        img = Im.open(self.photo.path)
        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)