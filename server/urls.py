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
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers

from conteudo.views import MesaList, TrabalhoList, CronogramaList
from social.views import ContatoCreate, SBPJorUserCreate, SBPJorUserRetrieveUpdate, FavoritoCreate, FavoritoDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', obtain_jwt_token),
    path('api/refresh-token/', refresh_jwt_token),

    # social urls
    path('api/contato/', ContatoCreate.as_view()),
    path('api/favorito/<int:pk>/', FavoritoDestroy.as_view()),
    path('api/favorito/', FavoritoCreate.as_view()),
    path('api/register/', SBPJorUserCreate.as_view()),
    path('api/user/<int:pk>/', SBPJorUserRetrieveUpdate.as_view()),


    # content urls
    path('api/mesa/', MesaList.as_view()),
    path('api/trabalho/', TrabalhoList.as_view()),
    path('api/cronograma/', CronogramaList.as_view()),

]
