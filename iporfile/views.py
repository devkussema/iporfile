from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    hora_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'index.html', {'hora': hora_atual})