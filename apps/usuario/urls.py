from django.conf.urls import url
from apps.usuario.views import RegistroUsuario, UsuarioList


urlpatterns = [
	 url(r'^novo/$', RegistroUsuario.as_view(), name='usuario_criar'),
	 url(r'^listar/$', UsuarioList.as_view(), name='usuario_listar')
]