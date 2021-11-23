from django import forms
from datetime import datetime
from .classe_responsavel import ClasseResponsavel
from .models import Resposta

class RespostaForms(forms.ModelForm):

    class Meta:
        model = Resposta
        fields = '__all__'