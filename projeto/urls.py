"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.inicial import views
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jogo/', include('apps.jogo.urls', namespace='jogo')),
    url(r'^solicitacao/', include('apps.solicitacao.urls', namespace='solicitacao')),
    #url(r'^plataforma/', include('apps.plataforma.urls',namespace='plataforma')),
    url(r'^usuario/', include('apps.usuario.urls',namespace='usuario')),
    url(r'^$', login, {'template_name':'inicial/login.html'}, name='login'),
    url(r'^accounts/login/', login, {'template_name':'inicial/login.html'}, name='login2'),
    url(r'^index/', login_required(views.index.as_view()), name='index'),
    url(r'^logout/', logout_then_login, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
