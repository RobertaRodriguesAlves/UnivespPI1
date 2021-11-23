from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseTipoPessoa(models.TextChoices):
    MUNICIPE = 'MUNICIPE', _('Municipe')
    VEREADOR = 'VEREADOR', _('Vereador')
