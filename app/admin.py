from django.contrib import admin
from .models import Ingredient, Measure, Dish, Image

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Measure)
admin.site.register(Dish)

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "photo"] # new

admin.site.register(Image, imageAdmin)
