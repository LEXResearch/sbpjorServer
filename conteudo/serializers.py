from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Mesa, Trabalho, Atividade, Cronograma, CategoriaAtividade, Evento, Dia
from social.models import Favorito

class CategoriaAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAtividade
        fields = ('titulo', 'cor_hex', 'cor_nome', 'cor_background')


class TrabalhoSerializer(serializers.ModelSerializer):
    evento = serializers.StringRelatedField()
    favorito = serializers.SerializerMethodField('is_favorite')
    mesa = serializers.PrimaryKeyRelatedField(read_only=True)

    def is_favorite(self, obj):
        user = self.context['request'].user
        trabalho = obj

        return Favorito.objects.filter(user=user, trabalho=trabalho).exists()

    class Meta:
        model = Trabalho
        fields = ('url', 'numero', 'evento', 'titulo', 'autores', 'favorito', 'pk', 'mesa')

class MesaSerializer(serializers.ModelSerializer):
    trabalhos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    atividade = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Mesa
        fields = ('numero', 'titulo', 'coordenada', 'trabalhos', 'descricao', 'atividade')

class AtividadeSerializer(serializers.ModelSerializer):
    mesas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    open = serializers.BooleanField(default='false')

    categoria = CategoriaAtividadeSerializer()

    class Meta:
        model = Atividade
        fields = ('titulo', 'descricao', 'local', 'hora', 'categoria', 'mesas', 'open')

class DiaSerializer(serializers.ModelSerializer):
    atividades = AtividadeSerializer(read_only=True, many=True)

    class Meta:
        model = Dia
        fields = ('dia', 'semana', 'atividades')


class CronogramaSerializer(serializers.ModelSerializer):
    dias = DiaSerializer(read_only=True, many=True)

    class Meta:
        model = Cronograma
        fields = ('titulo', 'data', 'is_active', 'dias')
