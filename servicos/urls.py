from django.urls import path
from . import views

urlpatterns = [
    path('', views.Servico, name='url_servico'),
]