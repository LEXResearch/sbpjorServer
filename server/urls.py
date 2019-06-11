"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers

from conteudo.views import MesaList, TrabalhoList, CronogramaList
from social.views import ContatoCreate, SBPJorUserCreate, SBPJorUserRetrieveUpdate, FavoritoCreate, FavoritoDestroy

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/login/', obtain_jwt_token),
    url(r'^api/refresh-token/', refresh_jwt_token),

    # social urls
    url(r'^api/contato/', ContatoCreate.as_view(), name='contato-create'),
    url(r'^api/favorito/', FavoritoCreate.as_view(), name='favorito-create'),
    url(r'^api/favorito/<int:pk>/', FavoritoDestroy.as_view(), name='favorito-destroy'),
    url(r'^api/register/', SBPJorUserCreate.as_view(), name='user-create'),
    url(r'^api/user/<int:pk>/', SBPJorUserRetrieveUpdate.as_view(), name='user-update'),


    # content urls
    url(r'^api/mesa/', MesaList.as_view(), name='mesa-list'),
    url(r'^api/trabalho/', TrabalhoList.as_view(), name='trabalho-list'),
    url(r'^api/cronograma/', CronogramaList.as_view(), name='cronograma-list'),

]
