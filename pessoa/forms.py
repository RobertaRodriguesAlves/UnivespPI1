from django import forms
from .models import *

class PessoaForms(forms.ModelForm):

    class Meta:
        model = Pessoa
        exclude = ('pessoa',)
        labels = {'nome':'Nome','tipo':'Tipo','telefone':'Telefone','cel':'Celular','email':'E-mail','cpf':'CPF','cep':'CEP','rua':'Rua','bairro':'Bairro' }



