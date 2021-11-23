from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.

class Partido(models.Model):
    nome = CharField(max_length=200)
    sigla = CharField(max_length=20)
    dtfundacao = DateField
    coligacao = CharField(max_length=200)