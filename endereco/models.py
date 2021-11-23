from django.db import models

# Create your models here.

class Endereco(models.Model):
    cep = models.CharField(max_length=50)
    rua = models.CharField(max_length=300)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
