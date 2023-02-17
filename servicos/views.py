from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Servico
from .forms import ServicoForm


# Listar os serviços disponíveis
def verServicos(request):

    data = {}
    servico = Servico.objects.all()
    data['servico'] = servico

    return render(request, 'servicos.html', data)

# Adicionar serviços
@login_required
@user_passes_test(lambda user: user.is_superuser)
def AdicionarServico(request):

    data = {}
    servicoForm = ServicoForm(request.POST or None)
    if servicoForm.is_valid():
        servicoForm.save()
        return redirect('url_servico')
    data['servicoForm'] = servicoForm

    return render(request, 'formularioservico.html', data)

#Editar serviço
@login_required
@user_passes_test(lambda user: user.is_superuser)
def EditarServico(request, id):

    data = {}
    servico = Servico.objects.get(pk = id)
    servicoForm = ServicoForm(request.POST or None, instance= servico)
    if servicoForm.is_valid():
        servicoForm.save()
        return redirect('url_servico')
    data['servicoForm'] = servicoForm
    data['servico'] = servico
    return render(request, 'formularioservico.html', data)


# Excluir Serviços
@login_required
@user_passes_test(lambda user: user.is_superuser)
def ExcluirServico(request, id):

    servico = Servico.objects.get(pk = id)
    servico.delete()
    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('url_servico')



