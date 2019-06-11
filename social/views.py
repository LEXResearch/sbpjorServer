import os

from django.core.mail import send_mail

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializers import ContatoSerializer, SBPJorUserSerializer, FavoritoSerializer
from .models import Contato, SBPJorUser, Favorito


def email_org(request):
    org_email = os.getenv('EMAIL_ORG')

    id = request.POST.get('user')

    user = SBPJorUser.objects.get(id=id)

    assunto = request.POST.get('assunto')

    if user.nome:
        assunto += " mensagem de " + user.nome
    else:
        assunto += " mensagem de " + user.username

    mensagem = request.POST.get('mensagem')

    if user.telefone:
        mensagem += "\nMeu contato: " + str(user.telefone)

    return send_mail(assunto, mensagem, 'sbpjor-server@lex.ufsm.br', [org_email], fail_silently=False)

class ContatoCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

    def post(self, request, *args, **kwargs):
        email_org(request)
        return self.create(request, *args, **kwargs)

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
