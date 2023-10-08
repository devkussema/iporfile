from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    pequena_descricao = models.CharField(max_length=200, default='')
    conteudo = RichTextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    tipo_projeto = models.CharField(max_length=100, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
