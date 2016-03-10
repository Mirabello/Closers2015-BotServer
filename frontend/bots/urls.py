from django.conf.urls import url
from .views import (
    IndexView,
    ProcessTonebotView,
    CreateTonebotView,
    UpdateTonebotView,
    CreateFaqbotView,
    ProcessFaqbotView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^create/tonebot$',  CreateTonebotView.as_view(), name='createtonebot'),
    url(r'^create/tonebot/(?P<botid>[\w-]+)$',  ProcessTonebotView.as_view(), name='processtonebot'),
    url(r'^update/tonebot/(?P<botid>[\w-]+)$',  UpdateTonebotView.as_view(), name='updatetonebot'),
    url(r'^create/faqbot$',  CreateFaqbotView.as_view(), name='createfaqbot'),
    url(r'^create/faqbot/(?P<botid>[\w-]+)$',  ProcessFaqbotView.as_view(), name='processfaqbot'),
    # url(r'^update/faqbot/(?P<botid>[\w-]+)$',  UpdateFaqbotView.as_view(), name='updatefaqbot'),
]
