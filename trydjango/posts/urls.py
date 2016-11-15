from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls import url
from . import views
from .views import (
post_list,
post_create,
post_detail,
post_update,
post_delete,
UserFormView,
	)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^movies/$', TemplateView.as_view(template_name='movies.html'), name='movies'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^create/$', post_create, name='Create'), #posts is module and post_home 
	url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
	url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
	url(r'^delete/$', post_delete),
] 
