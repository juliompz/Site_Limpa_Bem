from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-funcionario/', views.CadastrarFuncionario, name='url_cadastro'),
    path('ver-atendentes/', views.verAtendentes, name='url_ver-atendentes'),
    path('ver-helpers/', views.verHelpers, name='url_ver-helpers'),

]