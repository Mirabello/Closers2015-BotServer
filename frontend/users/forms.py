from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	class meta:
		model = Profile
		fields = []