from django import forms

from apps.solicitacao import models

class SolicitacaoForm(forms.ModelForm):
	class Meta:
		model = models.Solicitacao
		exclude = []
	def __int__(self, *args, **kawargs):
		super(SolicitacaoForm, self).__init__(*args, **kwargs)
