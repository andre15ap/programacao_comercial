from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.solicitacao.models import Solicitacao
from apps.jogo.models import Jogo
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class SolicitarList(ListView):
	# aguardando minha aprovação
	model = Solicitacao
	template_name = 'solicitacao/solicitacao_list.html'
	def get_queryset(self):
		# Jogo.objects.exclude(usuario = self.request.user).order_by('nome')
		return Solicitacao.objects.filter(
			Q(estado ="solicitado") &
			Q(solicitado=self.request.user)

		)


class SolicitarAguardando(ListView):
	# aguardando a aprovação do solicitado
	model = Solicitacao
	template_name = 'solicitacao/solicitacao_aguardando.html'

	def get_queryset(self):

		return Solicitacao.objects.filter(
			Q(estado__icontains="solicitado") &
			Q(solicitante=self.request.user)

		)





class Solicitar(View):
	def get(self, request):

		jogo_id = self.request.GET.get('jogo', 0)

		jogo = Jogo.objects.get(id=jogo_id)

	
		solicitacao = Solicitacao(
			jogo_solicitado=jogo,
			solicitante=self.request.user,
			solicitado=jogo.usuario,
			estado="solicitado"
		)
		solicitacao.save()


		context = {
			'solicitacao': solicitacao,
		}
		return render(request, 'solicitacao/solicitar.html',context)

class Confirmar(View):
	def get(self, request):

		solicit_id = self.request.GET.get('solic',0)
		jogo_id = self.request.GET.get('jogo_id',0)
		solicitacao = Solicitacao.objects.get(id=solicit_id)
		jogo = Jogo.objects.get(id=jogo_id)

		solicitacao.jogo_escolhido = jogo
		solicitacao.estado = "trocado"
		solicitacao.save()

		jogo.usuario = solicitacao.solicitado #jogo escolhido pertencia ao solicitante

		jogo_solicitado = Jogo.objects.get(id=solicitacao.jogo_solicitado.id)
		jogo_solicitado.usuario = solicitacao.solicitante  #jogo solicitado pertencia ao solicitado

		jogo.save()
		jogo_solicitado.save()

		context = {
			'object_list': Jogo.objects.filter(usuario=self.request.user).order_by('nome'),
		}
		return render(request, 'inicial/index.html', context)

class Recusar(View):

	def get(self, request):
		solicit_id = self.request.GET.get('solicit',0)
		solicitacao = Solicitacao.objects.get(id=solicit_id)
		solicitacao.estado = "recusado"
		solicitacao.save()
		context = {
			'object_list': Jogo.objects.filter(usuario=self.request.user).order_by('nome'),
		}
		return render(request, 'inicial/index.html', context)



class SolicitacaoDelete(DeleteView):
	"""classe para Deletar jogos"""
	model = Solicitacao
	template_name = 'solicitacao/solicitacao_delete.html'
	success_url = reverse_lazy('solicitacao:aguardando_listar')
