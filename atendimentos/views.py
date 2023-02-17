
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View

from atendimentos.utils import GerarPDF


from .models import Atendimento
from .forms import AtendimentoForm

# Ver atendimentos existentes
def verAtendimentos(request):
    data = {}
    atendimento = Atendimento.objects.all().order_by('id')

    for atend in atendimento:
        if atend.gerente_desc == 'S':
            atend.valor = atend.valor - (atend.valor * 10/100)
    data['atendimento'] = atendimento

    return render(request, 'atendimentos.html', data)

# Ver atendimento específico

def AtendimentoEspecifico(request, id):
    data = {}
    atendimento = get_object_or_404(Atendimento, pk=id)

    if atendimento.gerente_desc == 'S':
        atendimento.valor = atendimento.valor - (atendimento.valor * 10/100)
    data['atendimento'] = atendimento

    return render(request, 'verAtendimento.html', data)
# Adicionar novos atendimentos

def AdicionarAtendimento(request):
    
    data = {}
    atendimentoForm = AtendimentoForm(request.POST or None)
    if atendimentoForm.is_valid():
        atendimentoForm.save()
        return redirect('url_atendimentos')
    data['atendimentoForm'] = atendimentoForm

    return render(request, 'formularioatendimento.html', data)

# Exluir atendimento

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

def ExcluirAtendimento(request, id):

    atendimento = Atendimento.objects.get(pk=id)
    atendimento.delete()
    messages.info(request, 'Atendimento deletado com sucesso!')
    return redirect('url_atendimentos')

# Gerar PDF

def AtendimentosRelatorio(request):

    dados = {}
    atendimentos = Atendimento.objects.all()
    for atend in atendimentos:
        if atend.gerente_desc == 'S':
            atend.valor = atend.valor - (atend.valor * 10/100)
    dados = {
        'atendimentos': atendimentos,
    }

    pdf = GerarPDF()


    return pdf.render_to_pdf("relatorioatendimento.html", dados)