from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User
from .nome_vereador import ClasseNomeVereador



# Create your models here.

class Solicitacao(models.Model):
    municipe = models.ForeignKey(User, on_delete=models.CASCADE)
    vereador = models.TextField(choices=ClasseNomeVereador.choices,max_length=15, default=0)
    solicitacao = models.TextField(max_length=200, blank=True)
    foto_solicitacao = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

