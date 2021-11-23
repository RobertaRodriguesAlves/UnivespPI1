from django.urls import path

from . import views

urlpatterns = [
    path('resposta', views.resposta, name='resposta')

]    