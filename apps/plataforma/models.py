from django.db import models

# Create your models here.
class plataforma(models.Model):
	#id_console = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length = 50)
	descricao = models.CharField(max_length = 100)


	def __str__(self):
		return '{}'.format(self.nome)