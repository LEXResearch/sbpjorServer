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
        fields = ('imei', 'username', 'password', 'nome', 'telefone', 'email', 'data_nascimento', 'pk', 'cpf', 'rg')

class ContatoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=SBPJorUser.objects.all())

    class Meta:
        model = Contato
        fields = ('user', 'assunto', 'mensagem')

class FavoritoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=SBPJorUser.objects.all())

    trabalho = serializers.PrimaryKeyRelatedField(queryset=Trabalho.objects.all())


    class Meta:
        model = Favorito
        fields = ('user', 'trabalho')
