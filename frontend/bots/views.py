from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import Profile
from django.contrib.auth.models import User
from bots.models import Bot

class IndexView(View):
	template = 'bots/index.html'
	def get(self, request):
		#filter by user/profile id
		all_bots = Bot.objects.all()
		context = {
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
		            #get user profile
		            #create new bot object with bot id and profile id as members
		            #save bot

# class UpdateFaqbotView(View):
	# template = 'bots/updateFaqbot.html'
	# def get(self, request, botid):
		# context = {"botid": botid};
		# return render(request, self.template, context)

