from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.index_list, name='index_list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_in_detail, name="detail" )
]