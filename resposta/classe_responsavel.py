from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseResponsavel(models.TextChoices):
    SECRETARIA_OBRAS_SERVICOS = 'SECRETARIA_OBRAS_SERVICOS', _('Secretaria de Obras e Servicos')
    ASSUNTOS_JURIDICOS = 'ASSUNTOS_JURIDICOS', _('Assuntos Juridicos')
    ADMINISTRACAO_FINANCAS = 'ADMINISTRACAO_FINANCAS', _('Administracao e Financas')
    GABINETE_PREFEITO = 'GABINETE_PREFEITO', _('Gabinete do Prefeito')
    SECRETARIA_EDUCACAO_CULTURA = 'SECRETARIA_EDUCACAO_CULTURA', _('Secretaria de Educacao e Cultura')
    SECRETARIA_SAUDE = 'SECRETARIA_SAUDE', _('Secretaria da Saude')
    SECRETARIA_DESENVOLVIMENTO_SOCIAL = 'SECRETARIA_DESENVOLVIMENTO_SOCIAL', _('Secretaria de Desenvolvimento Social')
    SECRETARIA_DESENVOLVIMENTO_URBANO = 'SECRETARIA_DESENVOLVIMENTO_URBANO', _('Secretaria de Desenvolvimento Urbano')
