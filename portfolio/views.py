from django.shortcuts import render
from .models import Projeto

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'index.html', {'projetos': projetos})