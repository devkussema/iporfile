from django.shortcuts import render
from .models import Projeto

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ProjetoSerializer

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'index.html', {'projetos': projetos})

class ProjetoDetail(APIView):
    def get(self, request, id):
        projeto = get_object_or_404(Projeto, id=id)
        serializer = ProjetoSerializer(projeto, context={'request': request})
        return Response(serializer.data)