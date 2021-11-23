from django.shortcuts import render

from pessoa.forms import PessoaForms
from .models import Pessoa

# Create your views here.

def pessoa(request):
    pessoa_form = PessoaForms()
    contexto = {'pessoa_form':pessoa_form}
    return render(request, 'pessoa.html', contexto)  

def cadastra_pessoa(request):
    pessoa_form = PessoaForms(request.POST or None)
    if pessoa_form.is_valid():
        pessoa_form.save()

    contexto = {'pessoa_form':pessoa_form}
    return render(request, "pessoa.html", contexto)