from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from bots.forms import SingleForm


class ProfileIndex(LoginRequiredMixin, View):
	template="users/index.html"
	def get(self, request):
		profile = get_object_or_404(Profile, user=request.user)
		context = {"profile": profile,
					}
		return render(request, self.template, context)

class ToneSetting(LoginRequiredMixin, View):
	# user = request.user
	form = SingleForm
	template="users/index.html"
	def get(self, request, option):
		print(request.user)
		context = {
			"user": request.user,
			"form": self.form(),
			"option": option,
		}
		return render(request, self.template, context)


