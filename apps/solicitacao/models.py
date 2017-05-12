from django.db import models
from apps.jogo.models import Jogo
from django.contrib.auth.models import User
# Create your models here.


class Solicitacao(models.Model):

    jogo_solicitado = models.ForeignKey(Jogo, related_name="jogosolicitante")
    jogo_escolhido = models.ForeignKey(Jogo,null=True, blank=True, related_name="jogosolicitados")
    solicitante = models.ForeignKey(User, related_name="solicitacoes")
    solicitado = models.ForeignKey(User, related_name="solicitados")
    estado = models.CharField(max_length = 50)
