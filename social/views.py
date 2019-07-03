import os

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from rest_framework.response import Response


from .serializers import ContatoSerializer, SBPJorUserSerializer, FavoritoSerializer
from .models import Contato, SBPJorUser, Favorito


def email_org(request):
    org_email = os.getenv('EMAIL_ORG')

    assunto = request.POST.get('assunto')

    mensagem = request.POST.get('mensagem')

    return send_mail(assunto, mensagem, 'sbpjor-server@lex.ufsm.br', [org_email], fail_silently=False)

class ContatoCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

    def post(self, request, *args, **kwargs):
        email_org(request)
        return self.create(request, *args, **kwargs)

class SBPJorUserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)
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

    def post(self, request, format=None):
        serializer = FavoritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoritoDestroy(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
