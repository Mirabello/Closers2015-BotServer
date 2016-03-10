from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Profile
from django.contrib.auth.models import User
from bots.models import Bot

class ProfileIndex(LoginRequiredMixin, View):
	template="users/index.html"
	def get(self, request):
		#filter by user/profile id
		all_bots = Bot.objects.all()
		print(len(all_bots))
		profile = get_object_or_404(Profile, user=request.user)
		context = {
			"profile": profile,
			"bots": all_bots,
		}
		return render(request, self.template, context)


class CreateTonebotView(View):
	template = 'bots/createtonebot.html'
	def get(self, request):
		return render(request, self.template)


class ProcessTonebotView(View):
	def get(self, request, botid):
	        	#if (request.user.is_authenticated()):
        		new_bot = Bot(
        			bot_id = botid,
        			profile = request.user.profile,
        			description = "new bot"
        		)
        		new_bot.save()
	        	return redirect("bots:index")

class UpdateTonebotView(View):
	template = 'bots/updatetonebot.html'
	def get(self, request, botid):
		context = {"botid": botid};
		return render(request, self.template, context)

class CreateFaqbotView(View):
	template = 'bots/createfaqbot.html'
	def get(self, request):
		return render(request, self.template)

class ProcessFaqbotView(View):
	def get(self, request, botid):
		if (request.user.is_authenticated()):
			pass