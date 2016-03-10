from django.conf.urls import url
from .views import ProfileIndex, ToneSetting

urlpatterns = [
	url(r'^$',  ProfileIndex.as_view(), name='index'),
	url(r'^edit/(?P<option>[\w]+)$',  ToneSetting.as_view(), name='edit'),
]