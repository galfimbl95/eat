from django.shortcuts import render
from .models import Dish

# Create your views here.


def index(request):
    data = Dish.objects.all()
    context = {
        'data': data
    }
    return render(request, "display.html", context)
