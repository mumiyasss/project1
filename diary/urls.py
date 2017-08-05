from django.conf.urls import url
from . import views

app_name = "diary"
urlpatterns = [
    url(r'^$', views.main_screen, name='main_screen'), 
    url(r'^cat_id(?P<cat_id>[0-9]+)/$', views.cat_posts_list, name='cat_list'),
    url(r'^post_id(?P<post_id>[0-9]+)/$', views.view_post, name='view_post'),

    # url(r'^chat(?P<chat_id>[0-9]+)/new_message/$', views.new_message, name='new_message')
]
