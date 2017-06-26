from django.conf.urls import url
from .views import (
	ChatListAPIView,
	ThisChatAPIView,
	)

app_name = "lowMesAPI"
urlpatterns = [
    url(r'^$', ChatListAPIView.as_view(), name='ChatListAPIView'),
    url(r'^chat(?P<chat>[0-9]+)/$', ThisChatAPIView.as_view(), name='ThisChatAPIView'),
]
