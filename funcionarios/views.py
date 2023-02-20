from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, Group
from atendimentos.models import Atendimento
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages



@login_required
@user_passes_test(lambda user: user.is_superuser)
def CadastrarFuncionario(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    else:
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        email = request.POST.get('email', None)
        cargo = request.POST.get('cargo', None)
        user = User.objects.filter(username=usuario).first()
        if user:
            messages.error(request, 'Já existe um usuário com esse nome')
            data = {
                'exibir_mensagem': True,
                'mensagem': 'Já existe um usuário com esse nome'}
            return render(request, 'registration/register.html', data)
    
    user = User.objects.create_user(username=usuario, email=email, password=senha)
    user.save()
    if cargo == str('Atendente'):
        grupo = Group.objects.get(name ='Atendente')
    elif cargo == str('Helper'):
        grupo = Group.objects.get(name ='Helper')
    user.groups.add(grupo)
    return redirect('url_servico')

#Ver atendentes
def verAtendentes(request):
    grupo = Group.objects.get(name='Atendente')
    atendentes = []
    for user in grupo.user_set.all():
        atendimentos = Atendimento.objects.filter(atendente=user)
        atendentes.append({
            'user': user,
            'atendimentos': atendimentos
        })
    data = {
        'atendentes': atendentes,
    }
    return render(request, 'verAtendentes.html', data)

#Ver helpers
def verHelpers(request):
    grupo = Group.objects.get(name='Helper')
    helpers = []
    for user in grupo.user_set.all():
        atendimentos = Atendimento.objects.filter(helper=user)
        helpers.append({
            'user': user,
            'atendimentos': atendimentos
        })
    data = {
        'helpers': helpers,
    }
    return render(request, 'verHelpers.html', data)