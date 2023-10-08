# portfolio/serializers.py

from rest_framework import serializers
from .models import Projeto

class ProjetoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.SerializerMethodField()

    class Meta:
        model = Projeto
        fields = '__all__'

    def get_cliente_nome(self, obj):
        return obj.cliente.nome if obj.cliente else None
