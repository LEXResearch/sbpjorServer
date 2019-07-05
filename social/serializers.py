from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Contato, SBPJorUser, Favorito
from conteudo.models import Trabalho

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class SBPJorUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SBPJorUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = SBPJorUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('assunto', 'mensagem')

class FavoritoSerializer(serializers.ModelSerializer):
    trabalho = serializers.PrimaryKeyRelatedField(queryset=Trabalho.objects.all())


    class Meta:
        model = Favorito
        fields = ('trabalho',)
