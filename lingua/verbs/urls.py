from django.conf.urls import patterns, url

from verbs import views

urlpatterns = patterns('',
	url(r'^$', views.all_verbs, name='all_verbs'),
)