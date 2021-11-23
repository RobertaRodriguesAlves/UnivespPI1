from django import forms
from datetime import datetime
from . import nome_vereador
from .models import Solicitacao

class SolicitacaoForms(forms.ModelForm):

    class Meta:
        model = Solicitacao
        fields = '__all__'