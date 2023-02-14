
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estilizacao.urls')),
    path('servicos/', include('servicos.urls')),
    path('atendimentos/', include('atendimentos.urls')),
    path('funcionario/', include('funcionarios.urls'))
]
