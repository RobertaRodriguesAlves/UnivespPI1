from django.shortcuts import render
from .forms import RespostaForms

def resposta(request):
    resposta_form = RespostaForms()
  
    contexto = {'resposta_form':resposta_form}
    return render(request, 'resposta.html', contexto)