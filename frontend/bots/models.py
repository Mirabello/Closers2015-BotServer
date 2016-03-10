from django.db import models
from users.models import Profile

# Create your models here.
class Bot(models.Model):
	profile = models.ForeignKey(Profile)
	bot_id = models.CharField(max_length=50)
	bot_type = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
