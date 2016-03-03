from django import forms
from .models import AzizBot

class BotForm(forms.ModelForm):
	class Meta:
		model = AzizBot 
		fields = [ 'team_id',
					'token',
					'active'

		]
