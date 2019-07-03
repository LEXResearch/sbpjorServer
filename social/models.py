from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from conteudo.models import Trabalho


class SBPJorUser(AbstractUser):
    imei = models.IntegerField(null=True)
    nome = models.CharField(max_length=50, null=True)
    cpf = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    rg = models.IntegerField(null=True)
    telefone = models.IntegerField(null=True)
    data_nascimento = models.DateField(null=True)
    data_criado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Favorito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " " + self.trabalho.titulo

class Contato(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=50)
    mensagem = models.TextField(max_length=5000)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assunto + " enviado " + self.user.username
