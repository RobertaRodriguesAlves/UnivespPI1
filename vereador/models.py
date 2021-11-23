from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Vereador(models.Model):
    id_pessoa : IntegerField
    id_partido: IntegerField
    cargo : CharField(max_length=100)
