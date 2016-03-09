from django.conf.urls import url
from .views import CreateView, CreateTonebotView, UpdateTonebotView, IndexView

urlpatterns = [
        url(r'^$', IndexView.as_view(), name='index'),
	url(r'^create$',  CreateView.as_view(), name='create'),
	url(r'^create/(?P<botid>[\w-]+)$',  CreateTonebotView.as_view(), name='createtonebot'),
        url(r'^update/(?P<botid>[\w-]+)$',  UpdateTonebotView.as_view(), name='updatetonebot'),
]
