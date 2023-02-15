from django import forms

from .models import Atendimento

class AtendimentoForm(forms.ModelForm):

    class Meta:
        model = Atendimento
        fields = ['servico', 'atendente', 'helper' , 'formapgto', 'gerente_desc', 'data_agendada']