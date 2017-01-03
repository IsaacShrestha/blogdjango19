from django.conf.urls import url
from django.contrib import admin

from .views import(
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^(?P<slug>\d+)/$', post_detail, name='detail'),
    url(r'^create/$', post_create),
    url(r'^$', post_list, name='list'),
    url(r'^(?P<slug>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>\d+)/delete/$', post_delete),
    #url(r'^$', "posts.views.post_home"),
]