from django.conf.urls import url, include
from django.contrib import admin
#from apps.jogo import views
from apps.solicitacao import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^listar$', login_required(views.SolicitarList.as_view()), name='solicitar_listar'),
    url(r'^solicitar$', login_required(views.Solicitar.as_view()), name='solicitar'),
    # url(r'^buscar$', login_required(views.JogoBusca.as_view()), name='jogo_buscar'),
    # url(r'^editar/(?P<pk>\d+)$', login_required(views.JogoUpdate.as_view()), name='jogo_editar'),
    # url(r'^deletar/(?P<pk>\d+)$', login_required(views.JogoDelete.as_view()), name='jogo_deletar'),
    #url(r'^ver/(?P<pk>\d+)$', login_required(views.SolicitacaoVer.as_view()), name='solicitacao_ver'),
    # url(r'^veratual/(?P<pk>\d+)$', login_required(views.JogoVerAtual.as_view()), name='jogo_ver_atual'),

]
