from django.urls import path

from . import views

urlpatterns = [
    path('endereco', views.endereco, name='endereco')

]    