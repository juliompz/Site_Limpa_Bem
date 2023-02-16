from django.urls import path

from . import views

urlpatterns = [
    path('', views.verAtendimentos, name='url_atendimentos'),
    path('editar-atendimento/', views.EditarAtendimento, name='url_editar-atendimentos'),
    path('adicionar-atendimento/', views.AdicionarAtendimento, name='url_adicionar-atendimentos'),
    path('gerar-pdf/', views.AtendimentosRelatorio, name='url_pdf-relatorio')
]