from django.shortcuts import render
from django.views.generic import ListView
from apps.jogo.models import Jogo

# Create your views here.
class index(ListView):
	"""classe index da pagina"""
	model = Jogo
	template_name = 'inicial/index.html'

	def get_queryset(self):
		queryset = Jogo.objects.filter(usuario=self.request.user).order_by('nome')
		return queryset
