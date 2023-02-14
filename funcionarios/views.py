from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

def CadastrarFuncionario(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    else:
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        email = request.POST.get('email', None)
        user = User.objects.filter(username=usuario).first()
        if user:
            return HttpResponse('Ja existe um usuario com esse nome')
    
    user = User.objects.create_user(username=usuario, email=email, password=senha)
    user.save()

    grupo = Group.objects.get(name ='Atendente')
    user.groups.add(grupo)
    return HttpResponse('Login')
