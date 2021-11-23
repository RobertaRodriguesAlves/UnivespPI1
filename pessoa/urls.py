from django.urls import path

from . import views

urlpatterns = [
    path('pessoa', views.pessoa, name='pessoa'),
    path('cadastra_pessoa', views.cadastra_pessoa, name='cadastra_pessoa')

]    