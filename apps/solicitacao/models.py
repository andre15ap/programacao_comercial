from django.db import models
from apps.jogo.models import Jogo
from django.contrib.auth.models import User
# Create your models here.


class Solicitacao(models.Model):

    jogo = models.ForeignKey(Jogo)
    solicitante = models.ForeignKey(User, related_name="solicitacoes")
    solicitado = models.ForeignKey(User, related_name="solicitados")
    estado = models.CharField(max_length = 50)
