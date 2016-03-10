from django.db import models
from users.models import Profile

# Create your models here.
class Bot(models.Model):
	BOT_CHOICES = (
		("FAQ Bot", "Faq"),
		("Tone Bot", "Tone"),
		("Culture Bot", "Culture"),
		)
	user_id = models.ForeignKey(Profile)
	bot_id = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	bot_type = models.CharField(max_length=9, choices=BOT_CHOICES)
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.bot_type