from django.urls import path

from . import views

urlpatterns = [
    path('vereador', views.vereador, name='vereador')

]    