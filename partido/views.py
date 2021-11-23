from django.shortcuts import render
from .models import Partido

# Create your views here.

def partido(request):
    partidos = Partido.objects.all
    return render(request, 'partido.html')