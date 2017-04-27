from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.usuario import models
from django import forms



# Create your views here.
class RegistroForm(UserCreationForm):
	"""docstring for RegistroUsuario"""
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]

		labels = {
			'username' : 'Nome de usuario',
			'first_name':'Nome',
			'last_name':'Sobrenome',
			'email':'Email',
		}
