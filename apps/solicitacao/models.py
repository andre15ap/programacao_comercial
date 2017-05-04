from django.db import models
from apps.jogo.models import Jogo
from django.contrib.auth.models import User
# Create your models here.


class Solicitacao(models.Model):

    jogo = models.ForeignKey(Jogo, null=False, blank=False, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    estado = models.CharField(max_length = 50)
