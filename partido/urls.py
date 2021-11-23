from django.urls import path

from . import views

urlpatterns = [
    path('partido', views.partido, name='partido')

]    