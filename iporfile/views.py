from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'mensagem': 'Olá, mundo com template!'})