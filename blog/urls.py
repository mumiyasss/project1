from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.index_list, name='index_list'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_in_detail, name="detail" ),
    url(r'^(?P<post_id>[0-9]+)/like/$', views.post_like, name="like" ),
    url(r'^(?P<post_id>[0-9]+)/addcomment/$', views.add_comment, name="comment" ),
    url(r'^(?P<post_id>[0-9]+)/like/$', views.post_like, name="like" ),
    url(r'^page(?P<page_number>[0-9]+)/$', views.index_list, name='index_list'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^(?P<post_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/delete/$',
        views.delete_comment, name="delete_comment" ),

]

