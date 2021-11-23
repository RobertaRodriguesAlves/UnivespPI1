from django.shortcuts import render
from django.http import HttpResponse
from .models import Endereco

# Create your views here.

def endereco(request):
    enderecos = Endereco.objects.all()
    return render(request, 'endereco.html')