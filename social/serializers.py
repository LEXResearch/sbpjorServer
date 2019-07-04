from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Contato, SBPJorUser, Favorito
from conteudo.models import Trabalho

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class SBPJorUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = SBPJorUser
        fields = ('imei', 'username', 'password', 'nome', 'telefone', 'email', 'data_nascimento', 'cpf', 'rg')

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('assunto', 'mensagem')

class FavoritoSerializer(serializers.ModelSerializer):
    trabalho = serializers.PrimaryKeyRelatedField(queryset=Trabalho.objects.all())


    class Meta:
        model = Favorito
        fields = ('trabalho',)
