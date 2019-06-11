from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import ContatoSerializer, SBPJorUserSerializer, FavoritoSerializer
from .models import Contato, SBPJorUser, Favorito


class ContatoCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class SBPJorUserCreate(generics.CreateAPIView):
    queryset = SBPJorUser.objects.all()
    serializer_class = SBPJorUserSerializer

class SBPJorUserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SBPJorUser.objects.all()
    serializer_class = SBPJorUserSerializer

class FavoritoCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class FavoritoDestroy(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
