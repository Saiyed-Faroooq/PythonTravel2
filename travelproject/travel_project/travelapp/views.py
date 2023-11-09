from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Bg_image


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request, 'index.html', {'result': obj})


# def about(request):
#     return render(request, 'about.html')


# def contact(request):
#     return HttpResponse("This is contact page")

