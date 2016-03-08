from django import forms

THRESHOLD_CHOICES = (
		(0.1, "Very-Low"),
		(0.3, "Low"),
		(0.5, "Moderate"),
		(0.7, "High"),
		(0.9, "Very-High"),
		)


class Token(forms.Form):
	slack = forms.CharField(max_length=100)


class ToneForm(forms.Form):
	joy = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	joy_responses = forms.CharField(widget=forms.Textarea)
	sad = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	sad_responses = forms.CharField(widget=forms.Textarea)
	angry = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	angry_responses = forms.CharField(widget=forms.Textarea)
	disgust = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	disgust_responses = forms.CharField(widget=forms.Textarea)
	fear = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	fear_responses = forms.CharField(widget=forms.Textarea)
	

class CultureForm(forms.Form):
	responses = forms.CharField()


class FaqForm(forms.Form):
	pass

class JoyForm(forms.Form):
	joy = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	joy_responses = forms.CharField(widget=forms.Textarea)

class SadForm(forms.Form):
	sad = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	sad_responses = forms.CharField(widget=forms.Textarea)

class AngryForm(forms.Form):
	angry = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	angry_responses = forms.CharField(widget=forms.Textarea)

class DisgustForm(forms.Form):
	disgust = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	disgust_responses = forms.CharField(widget=forms.Textarea)

class FearForm(forms.Form):
	fear = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	fear_responses = forms.CharField(widget=forms.Textarea)
