from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.solicitacao import models
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class SolicitacaoList(ListView):
	"""classe para listar solicitações"""
	model = models.Solicitacao
	template_name = 'solicitacao/solicitacao_list.html'

	# def get_queryset(self):
	# 	return Jogo.objects.exclude(usuario = self.request.user).order_by('nome')

class SolicitacaoCreate(CreateView):
	"""classe para Criar novos solicitação"""
	model = models.Solicitacao
	# form_class = SolicitacaoForm
	template_name = 'solicitacao/solicitacao_create.html'
	success_url = reverse_lazy('index')

	# def form_valid(self, form):
	# 	obj = form.save(commit=False)
	# 	obj.usuario = self.request.user
	# 	obj.save()
	# 	return HttpResponseRedirect(self.success_url)
