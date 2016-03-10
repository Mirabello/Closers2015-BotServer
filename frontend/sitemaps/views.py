from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from contacts.forms import ContactForm

class HomePage(View):
	form = ContactForm
	def get(self, request):
		print(request.user)
		context ={
			"contact_form": self.form(),

		}
		return render(request, 'index.html', context)

	def post(self, request):
		pass
