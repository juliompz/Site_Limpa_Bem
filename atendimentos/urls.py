from django.urls import path

from . import views

urlpatterns = [
    path('', views.verAtendimentos, name='url_atendimentos'),
    path('atendimento/<int:id>/', views.AtendimentoEspecifico, name='url_ver-atendimento'),
    path('editar-atendimento/<int:id>/', views.EditarAtendimento, name='url_editar-atendimento'),
    path('adicionar-atendimento/', views.AdicionarAtendimento, name='url_adicionar-atendimentos'),
    path('gerar-pdf/', views.AtendimentosRelatorio, name='url_pdf-relatorio')
]