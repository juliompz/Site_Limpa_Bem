from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Group


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
            return HttpResponse('Ja existe um usuario com esse nome')
    
    user = User.objects.create_user(username=usuario, email=email, password=senha)
    user.save()
    if cargo == str('Atendente'):
        grupo = Group.objects.get(name ='Atendente')
    elif cargo == str('Helper'):
        grupo = Group.objects.get(name ='Helper')
    user.groups.add(grupo)
    return HttpResponse('Login')

def verAtendentes(request):

    data = {}
    funcionarios = User.objects.all()

    return render(request, 'verAtendentes.html', data)