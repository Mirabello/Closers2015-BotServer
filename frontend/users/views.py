from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class ProfileIndex(LoginRequiredMixin, View):
	template="users/index.html"
	def get(self, request):
		profile = get_object_or_404(Profile, user=request.user)
		context = {"profile": profile}
		return render(request, self.template, context)
