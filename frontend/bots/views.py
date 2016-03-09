from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class IndexView(View):
	template = 'bots/index.html'
	def get(self, request):
		return render(request, self.template)

class CreateView(View):
	template = 'bots/createtonebot.html'
	def get(self, request):
		return render(request, self.template)


class CreateTonebotView(View):
	def get(self, request, botid):
	        	if (request.user.is_authenticated()):
		            pass
		            #get user profile
		            #create new bot object with bot id and profile id as members
		            #save bot

class UpdateTonebotView(View):
	template = 'bots/updatetonebot.html'
	def get(self, request, botid):
		context = {"botid": botid};
		return render(request, self.template, context)

