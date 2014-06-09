from django.conf.urls import patterns, url

from nouns import views

urlpatterns = patterns('',
	url(r'^$', views.all_nouns, name='all_nouns'),
	url(r'^(?P<noun_id>\d+)/$', views.concrete_noun, name='concrete_noun'),
)