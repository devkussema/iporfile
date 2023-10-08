from django.contrib import admin
from .models import Projeto, Categoria, Cliente

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'cliente', 'data')
    list_filter = ('categoria', 'cliente', 'data')
    search_fields = ('titulo', 'pequena_descricao', 'conteudo')

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Categoria)
admin.site.register(Cliente)
