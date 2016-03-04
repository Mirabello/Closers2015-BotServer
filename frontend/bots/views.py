import json
import requests 
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import ToneForm

# Create your views here.

class IndexView(View):
	form = ToneForm
	template = 'bots/index.html'
	def get(self, request):
		context = {
			"form": self.form()
		}
		return render(request, self.template, context)

	def post(self, request):
		url="https://pacific-brushlands-11047.herokuapp.com/api/bots"
		omg =  {
		"properties": {
		  "anger": {
			"threshold": request.POST.get('anger'),
			"responses": [request.POST.get('anger_responses')]
		  },
		  "joy": {
			"threshold": request.POST.get('joy'),
			"responses": [request.POST.get('joy_responses')]
		  },
		  "sadness": {
			"threshold": request.POST.get('sadness'),
			"responses": [request.POST.get('sadness_responses')]
		  },
		  "disgust": {
			"threshold": request.POST.get('disgust'),
			"responses": [request.POST.get('disgust_responses')]
		  },
		  "fear": {
			"threshold": request.POST.get('fear'),
			"responses": [request.POST.get('fear_responses')]
		  }
		},
		"token": 'xoxb-22386467188-hVTzv9TXTIUnjsNJr2poZ82q',
		"teamID": "",
		"type": "tonebot",
		"service": "slack",
		"active": True
	  	}	
		data = {'bot': omg}
		data_json = json.dumps(data)
		print(data_json)

		bot_id = requests.post(url, data=data_json)
		print(bot_id)
		context = {
			"form": self.form()
		}
# print(request.POST)
		return  HttpResponse('')