
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from io import BytesIO

from django.template.loader import get_template
from xhtml2pdf import pisa

from atendimentos.utils import GerarPDF


from .models import Atendimento
from .forms import AtendimentoForm

# Ver atendimentos existentes
@login_required
def verAtendimentos(request):
    data = {}
    atendimento = Atendimento.objects.all().order_by('id')

    for atend in atendimento:
        if atend.gerente_desc == 'S':
            atend.valor = atend.valor - (atend.valor * 10/100)
    data['atendimento'] = atendimento

    return render(request, 'atendimentos.html', data)

# Ver atendimento específico
@login_required
def AtendimentoEspecifico(request, id):
    data = {}
    atendimento = get_object_or_404(Atendimento, pk=id)

    if atendimento.gerente_desc == 'S':
        atendimento.valor = atendimento.valor - (atendimento.valor * 10/100)
    data['atendimento'] = atendimento

    return render(request, 'verAtendimento.html', data)
# Adicionar novos atendimentos
@login_required
def AdicionarAtendimento(request):
    
    data = {}
    atendimentoForm = AtendimentoForm(request.POST or None)
    if atendimentoForm.is_valid():
        atendimentoForm.save()
        return redirect('url_atendimentos')
    data['atendimentoForm'] = atendimentoForm

    return render(request, 'formularioatendimento.html', data)

# Exluir atendimento
@login_required
def EditarAtendimento(request, id):

    data = {}
    atendimento = Atendimento.objects.get(pk = id)
    atendimentoForm = AtendimentoForm(request.POST or None, instance= atendimento)
    if atendimentoForm.is_valid():
        atendimentoForm.save()
        return redirect('url_atendimentos')
    data['atendimento'] = atendimento
    data['atendimentoForm'] = atendimentoForm
    return render(request, 'formularioatendimento.html', data)

# Excluir atendimento
@login_required
def ExcluirAtendimento(request, id):

    atendimento = Atendimento.objects.get(pk=id)
    atendimento.delete()
    messages.info(request, 'Atendimento deletado com sucesso!')
    return redirect('url_atendimentos')

# Gerar PDF
@login_required
@user_passes_test(lambda user: user.is_superuser)
def AtendimentosRelatorio(request):

    data = {}
    data_atual = timezone.now().date()
    atendimento = Atendimento.objects.filter(data_atendimento__date=data_atual)
    for atend in atendimento:
        if atend.gerente_desc == 'S':
            atend.valor = atend.valor - (atend.valor * 10/100)
    data = {
        'atendimento': atendimento,
        'data_atual': data_atual
    }
    pdf = GerarPDF()
    
    return pdf.render_to_pdf("relatorioatendimento.html", data) 

