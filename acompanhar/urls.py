from django.urls import path

from . import views

urlpatterns = [
    path('acompanhar', views.acompanhar, name='acompanhar')

]    