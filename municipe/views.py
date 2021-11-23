from django.shortcuts import render
from django.http import HttpResponse
from .models import Municipe

# Create your views here.

def index(request):

    dados = {
        'nome_do_municipe': 'teste'
    }
    return render(request, 'index.html')

def municipe(request):

    municipes = Municipe.objects.all()
    return render(request, 'municipe.html')

