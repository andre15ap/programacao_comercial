from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from apps.jogo.forms import JogoForm
from apps.solicitacao.form import SolicitacaoForm
from apps.jogo.models import Jogo
from apps.solicitacao.models import Solicitacao



class JogoList(ListView):
	"""classe para listar jogos"""
	model = Jogo
	template_name = 'jogo/jogo_list.html'

	def get_queryset(self):
		return Jogo.objects.exclude(
			Q(usuario = self.request.user) |
			Q(solicitado = True)).order_by('nome')

class JogoBusca(ListView):
	model = Jogo
	template_name = 'jogo/jogo_list.html'

	def get_queryset(self):
		busca = self.request.GET.get('busca', '')
		print(busca)
		return Jogo.objects.filter(
			Q(nome__icontains=busca) |
			Q(categoria__icontains=busca)

		).exclude(solicitado = True)




# class JogoTroca(ListView):
# 	model = Jogo
# 	template_name = 'jogo/jogo_list.html'
#
# 	def get_queryset(self):
# 		solicit = self.request.GET.get('solici',0)
# 		solicitacao = Solicitacao.objects.get(id=solicit)
# 		return Jogo.objects.filter(usuario=solicitacao.solicitante)

class JogoTroca(View):
	def get(self, request):

		solicit = self.request.GET.get('solici',0)

		solicitacao = Solicitacao.objects.get(id=solicit)

		# solicit = Solicitacao.objects.get(jogo_solicitado)
		# jogos = Jogo.objects.filter(usuario=solicitacao.solicitante)

		context = {
			'solicitacao': solicitacao,
			'object_list': Jogo.objects.filter(usuario=solicitacao.solicitante),
		}
		return render(request, 'jogo/jogo_troca_list.html', context)


class JogoVerTroca(View):
	"""classe para detalhar jogos"""

	def get(self, request):
		solicit_id = self.request.GET.get('solic',0)
		jogo_id = self.request.GET.get('jogo_id',0)
		solicitacao = Solicitacao.objects.get(id=solicit_id)
		jogo = Jogo.objects.get(id=jogo_id)
		context = {
			'jogo': jogo,
			'solicitacao': solicitacao,
		}
		return render(request, 'jogo/jogo_ver_troca.html', context)


class JogoVer(DetailView):
	"""classe para detalhar jogos"""
	model = Jogo
	template_name = 'jogo/tela_jogo.html'


class JogoVerAtual(DetailView):
	"""classe para ver jogo a partir do index jogos"""
	model = Jogo
	form_class = SolicitacaoForm
	template_name = 'jogo/tela_jogo_atual.html'



class JogoCreate(CreateView):
	"""classe para Criar novos jogos"""
	model = Jogo
	form_class = JogoForm
	template_name = 'jogo/jogo_form.html'
	success_url = reverse_lazy('index')


	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.usuario = self.request.user
		obj.solicitado = False
		obj.save()
		return HttpResponseRedirect(self.success_url)




class JogoUpdate(UpdateView):
	"""classe para Editar jogos"""
	model = Jogo
	form_class = JogoForm
	template_name = 'jogo/jogo_form.html'
	success_url = reverse_lazy('index')


	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.usuario = self.request.user
		obj.save()
		return HttpResponseRedirect(self.success_url)


class JogoDelete(DeleteView):
	"""classe para Deletar jogos"""
	model = Jogo
	template_name = 'jogo/jogo_delete.html'
	success_url = reverse_lazy('index')
