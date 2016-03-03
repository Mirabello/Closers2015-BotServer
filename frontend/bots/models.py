from django.db import models
from users.models import Profile

# Create your models here.

class AzizBot(models.Model):
	team_id = models.CharField(max_length=255, default=1)
	token = models.CharField(max_length=255)
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	joy_threshold = models.FloatField()
	angry_threshold = models.FloatField()
	sad_threshold = models.FloatField()
	happy_threshold = models.FloatField()



# class OtherBot(models.Model):
# 	team_id = models.CharField(max_length=255)
# 	token = models.CharField(max_length=255)	created = models.DateTimeField(auto_now_add=True)


# class BotCollection(models.Model):
# 	aziz_bot = models.OneToOneField(AzizBot)
# 	bot = models.ForeignKey(Bot)