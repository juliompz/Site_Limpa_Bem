from django.shortcuts import render
from django.http import HttpResponse

def Atendimento(request):
    return HttpResponse('Atendimentos')