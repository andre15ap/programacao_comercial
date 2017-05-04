from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from apps.jogo.forms import JogoForm
from apps.solicitacao.form import SolicitacaoForm
from apps.jogo.models import Jogo



class JogoList(ListView):
	"""classe para listar jogos"""
	model = Jogo
	template_name = 'jogo/jogo_list.html'

	def get_queryset(self):
		return Jogo.objects.exclude(usuario = self.request.user).order_by('nome')

class JogoBusca(ListView):
	model = Jogo
	template_name = 'jogo/jogo_list.html'

	def get_queryset(self):
		busca = self.request.GET.get('busca', '')
		print(busca)
		return Jogo.objects.filter(
			Q(nome__icontains=busca) |
			Q(categoria__icontains=busca)

		)

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
