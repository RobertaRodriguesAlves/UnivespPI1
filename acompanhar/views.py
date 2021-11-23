from django.shortcuts import render, get_object_or_404
from resposta.models import Resposta

# Create your views here.


def acompanhar(request):
    respostas = Resposta.objects.order_by('vereador')

    dados = {
        'respostas' : respostas
    }
    return render(request, 'acompanhar.html', dados)

