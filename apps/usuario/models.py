from django.db import models
from django.contrib.auth.models import User

# class Pessoa(models.Model):
# 	user = models.OneToOneField(User, related_name='perfil')
# 	sexo = models.CharField(max_length = 20)
# 	telefone = models.CharField(max_length = 20)
# 	foto = models.CharField(max_length = 50)
# 	endereco = models.TextField()
#
# 	def __str__(self):
# 		return '{}'.format(self.perfil.username)
