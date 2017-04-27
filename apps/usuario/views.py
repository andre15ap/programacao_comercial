from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from apps.usuario import forms

# Create your views here.
class RegistroUsuario(CreateView):
	"""docstring for RegistroUsuario"""
	model = User
	template_name = 'usuario/registrar.html'
	form_class = forms.RegistroForm
	success_url = reverse_lazy('login')

		
class UsuarioList(ListView):
	"""classe para listar jogos"""
	model = User
	template_name = 'usuario/listar.html'