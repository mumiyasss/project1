from django.conf.urls import url
from . import views

app_name = "diary"
urlpatterns = [
    url(r'^$', views.main_screen, name='main_screen'),
    # url(r'^chat(?P<chat_id>[0-9]+)/$', views.this_chat, name='this_chat'),
    # url(r'^chat(?P<chat_id>[0-9]+)/new_message/$', views.new_message, name='new_message')
]
