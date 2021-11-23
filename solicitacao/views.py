from django.shortcuts import render
from .forms import SolicitacaoForms

def solicitacao(request):
    solicitacao_form = SolicitacaoForms()
    contexto = {'solicitacao_form':solicitacao_form}
    return render(request, 'solicitacao.html', contexto)