from django.urls import path
from . import views

urlpatterns = [
    path('', views.verServicos, name='url_servico'),
    path('adicionar-servico/', views.AdicionarServico, name='url_adicionar-servico'),
    path('excluir-servico/<int:id>', views.ExcluirServico, name='url_excluir-servico'),
    path('editar-servico/<int:id>', views.EditarServico, name='url_editar-servico')
]