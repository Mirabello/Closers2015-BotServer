from django.shortcuts import render
from django.views.generic import View
from .forms import BotForm

# Create your views here.

class IndexView(View):
	form = BotForm
	def get(self, request):
		context = {
			"form": self.form()
		}
		return render(request, 'bots/index.html', context)