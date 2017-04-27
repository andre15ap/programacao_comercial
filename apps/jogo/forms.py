from django import forms

from apps.jogo.models import Jogo

class JogoForm(forms.ModelForm):
	class Meta:
		model = Jogo
		exclude = []
	def __int__(self, *args, **kawargs):
		super(JogoForm, self).__init__(*args, **kwargs)

		# fields = [
		# 	'nome',
		# 	'categoria',
		# 	'descricao',
		# 	'plataforma',
		# 	'usuario',
		# 	'image',
		#
		# ]
		#
		# labels = {
		# 	'nome':'Nome',
		# 	'categoria':'Categoria',
		# 	'descricao':'Descricao',
		# 	'plataforma':'Plataforma',
		# 	'usuario':'Usuario',
		# 	'image':'Imagem',
		#
		# }
		#
		# widgets = {
		# 	'nome': forms.TextInput(attrs={'required':'True',  'data-error':'wrong'}),
		# 	'categoria': forms.TextInput(attrs={'required':'True',  'data-error':'wrong'}),
		# 	'descricao': forms.TextInput(attrs={'required':'True',  'data-error':'wrong'}),
		# 	'plataforma': forms.Select(attrs={'required':'True',  'data-error':'wrong'}),
		#
		# }
