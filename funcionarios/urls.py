from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-funcionario/', views.CadastrarFuncionario, name='url_cadastro'),
]