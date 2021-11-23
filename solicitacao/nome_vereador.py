from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseNomeVereador(models.TextChoices):
    JOAO = 'JOAO', _('Joao Silva')
    JOSE = 'JOSE', _('Jose')
    CAETANO = 'CAETANO', _('Caetano Veloso')
    MARCOS = 'MARCOS', _('Marcos Oliveira')
    MELISSA = 'MELISSA', _('Melissa Santos')
    MARTA = 'MARTA', _('Marta Feliciano')
    LAURA = 'LAURA', _('Laura Helena')
    CINTIA = 'CINTIA', _('Cintia Figueiredo')