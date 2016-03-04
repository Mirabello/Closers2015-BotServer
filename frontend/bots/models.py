from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import FloatRangeField
from django.db import models
from users.models import Profile

# Create your models here.
class Bot(models.Model):
	user_id = models.ForeignKey(Profile)
	bot_id = models.CharField(max_length=50)