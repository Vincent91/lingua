from django.conf.urls import patterns, url

from adjectives import views

urlpatterns = patterns('',
	url(r'^$', views.all_adjectives, name='all_adjectives'),
)