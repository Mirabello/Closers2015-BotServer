from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User 

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	created = models.DateTimeField(auto_now_add=True)
	slack_token = models.CharField(max_length=60)


	def __str__(self):
		return str(self.user)

	@receiver(user_signed_up, sender=User)
	def user_signed_up(request, user, *args, **kwargs):
		if user:
			profile = Profile.objects.get_or_create(user=user)