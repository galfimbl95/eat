from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageUploadForm # new

# Create your views here.
def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

def uploadView(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})