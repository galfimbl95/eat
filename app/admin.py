from django.contrib import admin
from .models import Ingredient, Measure, Dish

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Measure)
admin.site.register(Dish)
