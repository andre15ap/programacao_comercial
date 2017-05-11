from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.solicitacao.models import Solicitacao
from apps.jogo.models import Jogo
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class SolicitarList(View):
	def get(self, request):
		context = {
		'object_list': Solicitacao.objects.all()
		}
		return render(request, 'solicitacao/solicitacao_list.html', context)




class Solicitar(View):
	def get(self, request):

		jogo_id = self.request.GET.get('jogo', 0)

		jogo = Jogo.objects.get(id=jogo_id)


		solicitacao = Solicitacao(
			jogo=jogo,
			solicitante=self.request.user,
			solicitado=jogo.usuario,
			estado="teste"
		)
		solicitacao.save()


		context = {
			'solicitacao': solicitacao,
		}
		return render(request, 'solicitacao/solicitar.html', context)
