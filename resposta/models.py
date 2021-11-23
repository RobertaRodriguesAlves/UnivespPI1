from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import User
from .classe_responsavel import ClasseResponsavel

# Create your models here.

class Resposta(models.Model):
    vereador = models.ForeignKey(User, on_delete=models.CASCADE)
    procedimento = models.TextField(max_length=200, blank=True)
    data_procedimento = models.DateField()
    responsavel = models.TextField(choices=ClasseResponsavel.choices,max_length=40, default=0)

  
