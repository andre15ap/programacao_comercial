from django.db import models

# Create your models here.
from django.conf.urls.static import static
from apps.plataforma.models import plataforma
from django.contrib.auth.models import User
from PIL import Image

class Jogo(models.Model):
	#id_jogo = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length = 50)
	categoria = models.CharField(max_length = 50)
	descricao = models.CharField(max_length = 100)
	solicitado = models.BooleanField()
	plataforma = models.ForeignKey(plataforma, null=False, blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
	image = models.ImageField('Imagem',upload_to='imagens',blank="True")
