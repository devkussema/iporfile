from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from portfolio.models import Projeto

def index(request):
    projetos = Projeto.objects.all()
    hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'projetos': projetos,
        'hora': hora_atual
    }
    return render(request, 'index.html', context)