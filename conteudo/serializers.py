from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Mesa, Trabalho, Atividade, Cronograma, CategoriaAtividade, Evento, Dia
from social.models import Favorito

class CategoriaAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaAtividade
        fiedls = ('titulo', 'cor_hex', 'cor_nome', 'cor_background')


class TrabalhoSerializer(serializers.ModelSerializer):
    evento = serializers.StringRelatedField()

    favorito = serializers.SerializerMethodField('is_favorite')

    def is_favorite(self, obj):
        user = self.context['request'].user
        trabalho = obj

        return Favorito.objects.filter(user=user, trabalho=trabalho).exists()



    # TODO: ADD FAVORITO FIELD TO JSON
    class Meta:
        model = Trabalho
        fields = ('url', 'numero', 'evento', 'titulo', 'autores', 'favorito', 'pk')

class MesaSerializer(serializers.ModelSerializer):
    trabalhos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Mesa
        fields = ('numero', 'titulo', 'coordenada', 'trabalhos', 'descricao')

class AtividadeSerializer(serializers.ModelSerializer):
    mesas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categoria = CategoriaAtividade()
    class Meta:
        model = Atividade
        fields = ('titulo', 'descricao', 'local', 'hora', 'categoria', 'mesas')

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
