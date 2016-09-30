from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_all_polls, name='polls'),
    url(r'^$', views.poll_vote, name='detail_poll')
]

