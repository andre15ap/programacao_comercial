from django.conf.urls import url, include
from django.contrib import admin
from apps.jogo import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^novo$', login_required(views.JogoCreate.as_view()), name='jogo_criar'),
    url(r'^listar$', login_required(views.JogoList.as_view()), name='jogo_listar'),
    url(r'^buscar$', login_required(views.JogoBusca.as_view()), name='jogo_buscar'),
    url(r'^editar/(?P<pk>\d+)$', login_required(views.JogoUpdate.as_view()), name='jogo_editar'),
    url(r'^deletar/(?P<pk>\d+)$', login_required(views.JogoDelete.as_view()), name='jogo_deletar'),
    url(r'^ver/(?P<pk>\d+)$', login_required(views.JogoVer.as_view()), name='jogo_ver'),
    url(r'^veratual/(?P<pk>\d+)$', login_required(views.JogoVerAtual.as_view()), name='jogo_ver_atual'),
    url(r'^troca$', login_required(views.JogoTroca.as_view()), name='jogo_troca'),
    url(r'^vertroca$', login_required(views.JogoVerTroca.as_view()), name='jogo_ver_troca'),


] + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
