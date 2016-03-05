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
	sad = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	angry = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	disgust = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	fear = forms.ChoiceField(choices=THRESHOLD_CHOICES)
	joy_responses = forms.CharField(widget=forms.Textarea)
	sad_responses = forms.CharField()
	angry_responses = forms.CharField()
	disgust_responses = forms.CharField()
	fear_responses = forms.CharField()

class CultureForm(forms.Form):
	responses = forms.CharField()


class FaqForm(forms.Form):
	pass