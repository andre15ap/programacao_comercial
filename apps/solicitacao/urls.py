from django.conf.urls import url, include
from django.contrib import admin
#from apps.jogo import views
from apps.solicitacao import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^novo$', login_required(views.JogoCreate.as_view()), name='jogo_criar'),
    url(r'^listar$', login_required(views.SolicitacaoList.as_view()), name='solicitacao_listar'),
    # url(r'^buscar$', login_required(views.JogoBusca.as_view()), name='jogo_buscar'),
    # url(r'^editar/(?P<pk>\d+)$', login_required(views.JogoUpdate.as_view()), name='jogo_editar'),
    # url(r'^deletar/(?P<pk>\d+)$', login_required(views.JogoDelete.as_view()), name='jogo_deletar'),
    # url(r'^ver/(?P<pk>\d+)$', login_required(views.JogoVer.as_view()), name='jogo_ver'),
    # url(r'^veratual/(?P<pk>\d+)$', login_required(views.JogoVerAtual.as_view()), name='jogo_ver_atual'),

]
