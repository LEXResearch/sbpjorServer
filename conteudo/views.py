from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import CronogramaSerializer, TrabalhoSerializer, MesaSerializer
from .models import Cronograma, Trabalho, Mesa

class TrabalhoList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Trabalho.objects.all()
    serializer_class = TrabalhoSerializer

class MesaList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class CronogramaList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer

class CronogramaRetrieve(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer
