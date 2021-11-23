from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User
from .tipo_pessoa import ClasseTipoPessoa

# Create your models here.

class Pessoa(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    tipo =  models.TextField(choices=ClasseTipoPessoa.choices,max_length=15, default=0)
    telefone = models.CharField(max_length=15, blank=True)
    cel = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=20, blank=True)
    cep = models.CharField(max_length=15, blank=True)
    rua = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=200, blank=True)
