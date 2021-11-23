from django.urls import path

from . import views

urlpatterns = [
    path('solicitacao', views.solicitacao, name='solicitacao')

]    