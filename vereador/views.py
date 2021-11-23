from django.shortcuts import render
from .models import Vereador
# Create your views here.

def vereador(request):
    vereadores = Vereador.objects.all()
    return render(request, 'vereador.html')