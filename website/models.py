from django.db import models
from django.utils import timezone

# Create your models here.

# Criando a classe Coach que será responsável por abrigar todos os dados registrados no HTML
class Coach(models.Model):

    # Criando a variável 'nome' que irá abrigar todos os nomes no input do HTML
    nome = models.CharField(max_length=255, verbose_name='Nome')

    # Essa váriavel irá abrigar todas as frases digitados no input com o apelido de frase no HTML
    frase = models.TextField()

    # Aqui também abriga todos os dados inseridos no input identificado como inspirador no HTML
    inspirador = models.CharField(max_length=255, null=True, blank=True)
    
    # Váriavel que irá gravar a data quando for pressionado o botão para dar submit
    criado_em =  models.DateTimeField(default=timezone.now)

    # Váriavel que irá determinar se o usuário está ativo
    ativo = models.BooleanField(default=True)