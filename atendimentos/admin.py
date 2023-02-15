from django.contrib import admin

from .models import Atendimento

class ListandoAtendimento(admin.ModelAdmin):
    list_display = ('id', 'servico', 'valor', 'cliente', 'gerente_desc')

admin.site.register(Atendimento, ListandoAtendimento)